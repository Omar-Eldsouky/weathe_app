# Development Ticket: Zajel Merchant API Integration

## Ticket ID: DEV-2025-001
**Priority:** High  
**Type:** Feature/Integration  
**Estimated Effort:** 13-21 Story Points (2-3 Sprints)  
**Assignee:** Backend Team Lead  
**Reporter:** Product Owner  
**Created:** February 19, 2026

---

## 📋 Overview

Implement full integration with Zajel Merchant API v1.8 to enable automated shipment creation, tracking, and management for domestic and international deliveries.

---

## 🎯 Business Objectives

- Automate shipment creation and label generation
- Enable real-time shipment tracking
- Reduce manual data entry and errors
- Support both domestic (UAE) and international shipping
- Receive automated status updates via webhooks

---

## 📝 Requirements

### Functional Requirements

#### 1. API Authentication
- [ ] Implement API key authentication mechanism
- [ ] Store API credentials securely (environment variables/secrets manager)
- [ ] Support both staging and production environments
- [ ] Handle authentication errors (401, 403)

#### 2. Shipment Creation

**Domestic Shipments:**
- [ ] Implement `CreateShipment` endpoint integration
- [ ] Validate all mandatory fields before API call
- [ ] Support optional fields (COD, dimensions, multi-piece)
- [ ] Handle phone number validation for UAE format
- [ ] Map internal customer codes to Zajel customer codes

**International Shipments:**
- [ ] Implement `CreateShipment/v2` endpoint integration
- [ ] Support OUTBOUND and INBOUND directions
- [ ] Validate HS codes for NON-DOCUMENT shipments
- [ ] Handle declared value and currency requirements
- [ ] Support DDP/DDU Incoterms

**Common Features:**
- [ ] Auto-generate or accept custom reference numbers
- [ ] Validate city codes and area values against Zajel data
- [ ] Store shipment creation responses (reference numbers, pieces)
- [ ] Implement retry logic for failed shipment creation
- [ ] Log all API requests/responses for debugging

#### 3. Reference Data Management
- [ ] Implement `GetCities` endpoint integration
- [ ] Implement `GetAreas` endpoint integration
- [ ] Cache city/area data locally (refresh daily/weekly)
- [ ] Provide city/area dropdown/autocomplete in UI
- [ ] Support international country lookups

#### 4. Shipment Tracking
- [ ] Implement `TrackShipment` endpoint integration
- [ ] Store tracking history in database
- [ ] Display current status in UI
- [ ] Support bulk tracking queries (if needed)
- [ ] Handle tracking for non-existent shipments (404)

#### 5. Label Generation
- [ ] Implement `GetShipmentLabel` endpoint integration
- [ ] Download and store labels as PDF
- [ ] Provide "Download Label" button in UI
- [ ] Support batch label printing
- [ ] Handle label generation errors

#### 6. Shipment Cancellation
- [ ] Implement `CancelShipment` endpoint integration
- [ ] Validate shipment status before cancellation
- [ ] Only allow cancellation of `pickup_awaited` shipments
- [ ] Update internal shipment status after cancellation
- [ ] Provide cancellation confirmation to users

#### 7. Webhook Implementation
- [ ] Create webhook endpoint to receive Zajel status updates
- [ ] Implement authentication for webhook (API Key or Basic Auth)
- [ ] Parse and validate incoming webhook payloads
- [ ] Update shipment status in real-time
- [ ] Store webhook event history
- [ ] Handle the following statuses:
  - pickup_awaited, pickup_completed
  - inscan_at_hub, reachedathub
  - outfordelivery, attempted, delivered
  - on_hold, cancelled
  - rto, rto_attempted, rto_delivered
  - softdata_upload, softdata_update
- [ ] Send notifications to users on status changes
- [ ] Implement retry mechanism for failed webhook processing

---

## 🏗️ Technical Requirements

### API Integration Layer
```
- Language: [Your preferred language - Node.js/Python/Java/etc.]
- HTTP Client: [Axios/Fetch/Requests/etc.]
- Error Handling: Comprehensive try-catch with logging
- Timeout: 30 seconds per API call
- Retry Logic: 3 attempts with exponential backoff
```

### Data Models

**Shipment Entity:**
```javascript
{
  id: UUID,
  reference_number: String,
  customer_reference_number: String,
  customer_code: String,
  service_type_id: String,
  product_type: Enum['DOCUMENT', 'NON-DOCUMENT'],
  status: String,
  weight_in_kg: Decimal(10,2),
  cod_amount: Decimal(10,2),
  origin: Address,
  destination: Address,
  created_at: Timestamp,
  updated_at: Timestamp,
  tracking_history: Array<TrackingEvent>
}
```

**TrackingEvent Entity:**
```javascript
{
  id: UUID,
  shipment_id: UUID,
  status: String,
  event_date_time: Timestamp,
  description: String,
  received_by: String,
  delivery_courier: String,
  failure_reason: String,
  created_at: Timestamp
}
```

### Database Schema
- [ ] Create `shipments` table
- [ ] Create `tracking_events` table
- [ ] Create `webhook_logs` table
- [ ] Create `api_request_logs` table (optional, for debugging)
- [ ] Add appropriate indexes for performance

### Configuration
- [ ] Store base URLs (staging/production) in config
- [ ] Environment-based configuration switching
- [ ] API key storage in secrets manager
- [ ] Customer code mapping configuration

---

## 🔒 Security Requirements

- [ ] Never log API keys in plain text
- [ ] Use HTTPS for all API communications
- [ ] Validate and sanitize all webhook inputs
- [ ] Implement rate limiting on webhook endpoint
- [ ] Secure webhook endpoint with authentication
- [ ] Encrypt sensitive data at rest
- [ ] Implement proper error messages (no sensitive data exposure)

---

## ✅ Validation Rules

### Phone Number Validation (UAE Origin):
```
Accepted formats:
- +9715 followed by 8 digits
- +971[1-46-9] followed by 7 digits
- 9715 followed by 8 digits
- 971[1-46-9] followed by 7 digits
- 0[1-46-9] followed by 7 digits
- 05 followed by 8 digits
- 5 followed by 8 digits
- 009715 followed by 8 digits
- 00971[1-46-9] followed by 7 digits
```

### Field Length Limits:
```
- reference_number: 30 chars
- customer_reference_number: 30 chars
- description: 150 chars
- name: 100 chars
- address_line_1: 255 chars
- address_line_2: 255 chars
- area: 100 chars
- city: 50 chars
- country: 50 chars (Alpha-3 code for international)
- email: 100 chars
```

### Numeric Validations:
```
- weight_in_kg: 0.01 - 999.99 (2 decimals)
- dimensions (L/W/H): 0 - 10000 cm (2 decimals)
- cod_amount: 0 - 9999.99 (2 decimals)
- num_of_pieces: 0 - 100
```

---

## 🧪 Testing Requirements

### Unit Tests
- [ ] Test all API client methods
- [ ] Test validation logic
- [ ] Test data transformation/mapping
- [ ] Test error handling scenarios
- [ ] Test webhook payload parsing
- [ ] Target: 80%+ code coverage

### Integration Tests
- [ ] Test against Zajel staging environment
- [ ] Test shipment creation flow (domestic)
- [ ] Test shipment creation flow (international)
- [ ] Test tracking functionality
- [ ] Test label generation
- [ ] Test cancellation
- [ ] Test webhook endpoint
- [ ] Test error scenarios (401, 403, 404, 500)

### End-to-End Tests
- [ ] Complete shipment lifecycle test
- [ ] Create → Track → Download Label → Cancel
- [ ] Webhook status update flow

### Test Data
- [ ] Create test customer codes
- [ ] Use Zajel staging API key
- [ ] Prepare valid/invalid test payloads
- [ ] Document test scenarios

---

## 📚 Documentation Requirements

- [ ] API integration documentation
- [ ] Architecture diagrams (sequence, component)
- [ ] Database schema documentation
- [ ] Error code reference guide
- [ ] Webhook setup instructions
- [ ] Deployment guide
- [ ] User guide for shipment creation
- [ ] Troubleshooting guide
- [ ] Postman collection (already created)

---

## 🚀 Deployment Requirements

### Pre-Deployment Checklist
- [ ] All tests passing
- [ ] Code review completed
- [ ] Security review completed
- [ ] API credentials configured in production
- [ ] Database migrations ready
- [ ] Rollback plan documented

### Staging Deployment
- [ ] Deploy to staging environment
- [ ] Run integration tests against staging
- [ ] Perform manual QA testing
- [ ] Validate webhook endpoint accessibility

### Production Deployment
- [ ] Deploy during maintenance window
- [ ] Run smoke tests
- [ ] Monitor error logs
- [ ] Verify webhook is receiving events
- [ ] Create sample shipments for validation

---

## 📊 Monitoring & Observability

- [ ] Set up API request/response logging
- [ ] Track API success/failure rates
- [ ] Monitor webhook delivery success rate
- [ ] Set up alerts for API failures
- [ ] Dashboard for shipment status distribution
- [ ] Performance metrics (API response times)

---

## 🔄 Error Handling

### HTTP Status Codes to Handle:
```
200 - Success (GET requests)
201 - Created (POST requests)
400 - Bad Request (validation errors)
401 - Unauthorized (invalid API key/customer code)
403 - Forbidden (access not granted)
404 - Not Found (shipment doesn't exist)
500 - Internal Server Error
```

### Error Response Strategy:
- [ ] Log all errors with context
- [ ] Display user-friendly error messages
- [ ] Retry transient failures (500, network errors)
- [ ] Alert on critical failures
- [ ] Store failed requests for manual review

---

## 📅 Implementation Phases

### Phase 1: Foundation (Sprint 1) - 5 days
- [ ] Set up project structure
- [ ] Implement authentication
- [ ] Create data models and database schema
- [ ] Implement basic API client wrapper
- [ ] Set up logging infrastructure

### Phase 2: Core Features (Sprint 1-2) - 8 days
- [ ] Implement domestic shipment creation
- [ ] Implement international shipment creation
- [ ] Implement tracking
- [ ] Implement GetCities/GetAreas
- [ ] Implement label download
- [ ] Implement cancellation

### Phase 3: Webhooks (Sprint 2) - 3 days
- [ ] Create webhook endpoint
- [ ] Implement webhook authentication
- [ ] Implement status update logic
- [ ] Test webhook with Zajel team

### Phase 4: Testing & Polish (Sprint 3) - 5 days
- [ ] Write comprehensive tests
- [ ] UI integration
- [ ] Documentation
- [ ] Bug fixes
- [ ] Performance optimization

---

## 🧑‍💻 Dependencies

### External Dependencies
- Zajel API credentials (API key, customer code)
- Zajel staging environment access
- Webhook URL publicly accessible (or tunneling solution for dev)

### Internal Dependencies
- Database access
- Secrets management system
- Email/notification service
- User authentication system

### Team Dependencies
- DevOps for deployment pipeline
- QA for testing
- Product team for UAT
- Zajel support team for API questions

---

## ✋ Risks & Mitigation

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| API key exposure | High | Low | Use secrets manager, code reviews |
| Webhook endpoint unreachable | High | Medium | Health checks, monitoring, fallback polling |
| API rate limiting | Medium | Medium | Implement rate limiting, caching |
| Data validation failures | Medium | High | Comprehensive validation, user feedback |
| Staging environment instability | Medium | Medium | Coordinate with Zajel, have rollback plan |

---

## 📖 Reference Materials

- API Documentation: Zajel_Merchant_API_Document_v_1_8_3.pdf
- Postman Collection: Zajel-Merchant-API-v1.8.postman_collection.json
- Staging URL: https://api-stg.zajel.com/services/integration
- Production URL: https://api.zajel.com:8443/services/integration

---

## ✅ Definition of Done

- [ ] All acceptance criteria met
- [ ] Code reviewed and approved
- [ ] Unit tests written and passing (80%+ coverage)
- [ ] Integration tests passing on staging
- [ ] Documentation complete
- [ ] Security review passed
- [ ] Deployed to staging and validated
- [ ] Product owner acceptance
- [ ] Deployed to production
- [ ] Monitoring and alerts configured
- [ ] Post-deployment smoke tests passed

---

## 💬 Notes

- Coordinate with Zajel support team for webhook URL registration
- Consider implementing a shipment dashboard for visibility
- Plan for future enhancements (bulk operations, analytics)
- Keep Postman collection updated as API evolves

---

## 🔗 Related Tickets

- INFRA-XXX: Set up secrets manager for API credentials
- QA-XXX: Create test plan for Zajel integration
- DOC-XXX: Update user documentation with shipping features
- OPS-XXX: Configure monitoring for Zajel API integration

---

**Last Updated:** February 19, 2026  
**Version:** 1.0
