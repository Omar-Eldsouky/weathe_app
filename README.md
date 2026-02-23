# Shopify Shipping App - Enhancement Requirements Document

**Document Version:** 1.0  
**Date:** February 10, 2026  
**Project:** Shipping App Enhancement - COD & Manual Shipment Features

---

## Executive Summary

**Company Context:** We are a shipping/logistics company providing shipping services to Shopify merchants through our Shopify app integration.

This document outlines the requirements to enhance our existing Shopify shipping app with Cash on Delivery (COD) support, manual shipment creation, and additional features to improve our merchant customers' operational efficiency and their end-customer experience.

### Current State (Our App Features)
- ✅ Live shipping rates displayed at merchant checkout (our rates)
- ✅ Shipment creation through our platform (checkout flow only)
- ✅ Shipping label printing for our shipping service

### Project Goals
- Enable Cash on Delivery payment method for our shipping service
- Allow merchants to create shipments from admin panel (not just checkout)
- Provide rate fetching capability outside checkout flow
- Improve merchant operational efficiency with bulk operations (100+ orders)
- Provide data-driven insights through Performance Dashboard (our service performance)
- Enhance end-customer experience with branded tracking page
- Increase merchant conversions through shipping promotions (on our rates)
- **Grow our shipping volume** by making our service more valuable to merchants

### Critical New Features (Competitive Differentiators for Our Shipping Service)

**1. Performance & SLA Dashboard** 🎯 **HIGH IMPACT - TRANSPARENCY ADVANTAGE**
- **What Competing Carriers Don't Provide:** Real-time delivery performance metrics visible to merchants
- **Business Value for Merchants:** Validate our service quality, make data-driven decisions
- **Business Value for Us:** Transparency builds trust, shows our superior performance, justifies our rates
- **Key Metrics:** Avg delivery time per city (our deliveries), our failure rate per route, COD collection time
- **Competitive Impact:** Merchants can see we deliver faster/more reliably than competitors

**2. Bulk Operations at Scale** ⚡ **EFFICIENCY MULTIPLIER - MERCHANT RETENTION**
- **Merchant Pain Point:** Processing hundreds of orders with our service is manual and slow
- **Solution:** Select and process 100+ shipments with our carrier in 10 minutes
- **Features:** Bulk shipment creation, batch label printing, queue management
- **Impact for Merchants:** 90% time reduction processing shipments with us
- **Impact for Us:** Merchants ship more volume through our service, reduce churn, higher satisfaction

**3. Branded Tracking Page** 🎨 **CUSTOMER EXPERIENCE - WHITE LABEL VALUE**
- **Current Pain:** End-customers track on generic pages, merchants have no control
- **Solution:** Merchants get fully branded tracking (powered by our tracking data)
- **Features:** Real-time updates from our system, delivery instructions, product recommendations
- **Impact for Merchants:** 60% reduction in "where's my order" tickets, professional brand experience
- **Impact for Us:** Better end-customer experience = more merchants choose our service

**4. Shipping Promotions Engine** 💰 **CONVERSION DRIVER - COMPETITIVE RATES**
- **What Merchants Need:** Flexibility to offer promotional shipping rates (using our service)
- **Solution:** Merchants can create promotions on our shipping rates
- **Examples:** "Free shipping with [Our Company]," "Discounted express with [Our Service]"
- **Impact for Merchants:** 25% cart conversion increase when offering our promotional rates
- **Impact for Us:** More shipments through our service, competitive advantage over other carriers

### Why This Matters - Our Business Context

**Current State (Our Challenges):**
- ❌ Merchants use multiple carriers - we need to be their preferred choice
- ❌ Competitors offer similar rates - we need differentiation beyond price
- ❌ Manual processing limits merchant volume through our service
- ❌ No visibility into our performance - merchants can't validate our quality
- ❌ Can't offer flexible promotional rates - lose price-sensitive shipments

**With Enhanced App (Our Advantages):**
- ✅ **Volume Growth:** Easier bulk processing = merchants send more through us
- ✅ **Differentiation:** Only carrier with performance transparency + promotions
- ✅ **Merchant Retention:** Better tools = stickier relationship
- ✅ **Competitive Moat:** Tracking page + analytics = hard to switch away
- ✅ **Premium Positioning:** Advanced features justify our rates
- ✅ **Market Expansion:** COD enables new merchant segments

---

## 1. CRITICAL REQUIREMENTS (Must Have)

### 1.1 Cash on Delivery (COD) Support

#### Business Requirements
- **What:** Enable customers to choose "Cash on Delivery" as a payment method at checkout
- **Why:** Expand market reach to customers who prefer COD, especially in regions where it's common
- **Who Benefits:** Customers without credit cards, business in cash-preferred markets

#### Functional Requirements
| Feature | Description | User Story |
|---------|-------------|------------|
| COD Payment Option | Display COD as payment method during checkout | As a customer, I want to select COD so I can pay when I receive my order |
| COD Fee Configuration | Admin can set COD handling fees (fixed or %) | As a store owner, I want to charge a COD fee to cover collection costs |
| COD Amount Tracking | System tracks COD amount to be collected | As a fulfillment team, I need to know how much cash to collect |
| COD Label Generation | Labels include "COD" indicator and amount | As a courier, I need to see the COD amount clearly on the label |
| COD Order Identification | Orders marked with COD badge in admin | As a manager, I want to quickly identify COD orders |

#### Technical Requirements
- Integrate with Shopify Payment Gateway API
- Store COD amount in order metadata
- Add COD flag to shipment data structure
- Update label template to include COD information
- Create webhook listener for COD payment confirmation

---

### 1.2 Manual Shipment Creation

#### Business Requirements
- **What:** Create shipments directly from admin panel for any order
- **Why:** Handle exceptions, backorders, partial shipments, and manual processing
- **Who Benefits:** Operations team, customer service, warehouse staff

#### Functional Requirements
| Feature | Description | User Story |
|---------|-------------|------------|
| Admin Shipment Interface | UI to create shipments from order details page | As an admin, I want to create a shipment for any order with one click |
| Manual Rate Selection | Choose carrier and service level manually | As a fulfillment agent, I want to select the best shipping option for special cases |
| Partial Shipment Support | Create multiple shipments for single order | As a warehouse manager, I want to ship available items immediately |
| Bulk Shipment Creation | Select multiple orders and create shipments | As an operations manager, I want to process 50 orders at once |
| Shipment Preview | Review shipment details before finalizing | As an admin, I want to verify details before creating the shipment |

#### Technical Requirements
- Build admin panel UI for shipment creation
- API endpoint: `POST /api/shipments/create`
- Support for line item selection (partial shipments)
- Bulk processing queue for multiple orders
- Validation for address, weight, dimensions
- Error handling and rollback mechanism

---

### 1.3 Rate Fetching Outside Checkout

#### Business Requirements
- **What:** Get shipping rates for any order on-demand
- **Why:** Quote customers, compare carriers, make informed shipping decisions
- **Who Benefits:** Customer service, sales team, operations

#### Functional Requirements
| Feature | Description | User Story |
|---------|-------------|------------|
| Rate Calculator Tool | Widget in admin to get rates for any order | As a CS rep, I want to quote shipping costs to a customer |
| Multi-Carrier Comparison | Display rates from all available carriers | As an operations manager, I want to compare all carrier options |
| Rate Refresh | Re-fetch rates if order details change | As an admin, I want updated rates when I change package weight |
| Rate History | View previously fetched rates for an order | As a manager, I want to see rate changes over time |

#### Technical Requirements
- API endpoint: `GET /api/rates/fetch?order_id={id}`
- Cache rates for 15 minutes to reduce API calls
- Support for multiple carrier APIs
- Response format: standardized rate object
- Rate logging for audit trail

---

## 2. HIGH-PRIORITY ENHANCEMENTS (Should Have)

### 2.1 Performance & Visibility Dashboard (CRITICAL - What Merchants Don't Get Today)

**Context:** This dashboard shows **our shipping company's performance metrics** to our merchant customers, demonstrating our service quality and building trust through transparency.

This is a game-changing feature that provides data-driven insights merchants currently don't have access to from shipping carriers.

| Feature | Description | Business Value | Effort |
|---------|-------------|----------------|--------|
| Carrier SLA Dashboard | Real-time performance metrics of OUR service by city/region | Demonstrate our superior service quality to merchants | High |
| Delivery Time Analytics | Average delivery time for OUR service per city | Prove we're faster than competitors, set accurate expectations | Medium |
| Failure Rate Tracking | Monitor OUR failed deliveries by route and reason | Show our reliability, identify problem routes to fix | Medium |
| COD Collection Time Metrics | Track OUR average time from delivery to cash collection | Demonstrate efficient COD service for merchants | Medium |
| Cost vs Performance Analysis | Show merchants the value they get for our rates | Justify premium pricing with superior performance data | Medium |

**Dashboard Components:**
- City-wise delivery heatmap (our delivery speeds by destination)
- Service performance comparison charts (our different service levels)
- Real-time failure alerts (our deliveries needing attention)
- COD collection timeline visualization (our collection efficiency)
- Monthly performance reports (exportable for merchant records)

**Key Metrics Displayed (All About Our Service):**
- Average delivery time (our promised vs actual performance)
- On-time delivery percentage (our reliability rate)
- Failed delivery rate with reasons (our service quality)
- Average COD collection time (our cash collection efficiency)
- Cost per delivery by zone (our rate transparency)
- Return to origin (RTO) rate (our success rate)

**Strategic Value for Our Business:**
- **Transparency Differentiator:** No other carrier shows this level of detail
- **Trust Building:** Merchants see real data, not just promises
- **Competitive Proof:** Merchants can validate we're better than alternatives
- **Problem Resolution:** We identify and fix issues before merchants complain
- **Retention Tool:** Transparency creates stickiness, harder to switch carriers
- **Premium Justification:** Performance data justifies higher rates

### 2.2 Order Management Improvements

| Feature | Description | Business Value | Effort |
|---------|-------------|----------------|--------|
| Shipment Tracking Integration | Auto-update order status with tracking events | Reduces customer inquiries by 40% | Medium |
| Automated Tracking Emails | Send tracking info to customers automatically | Improves customer satisfaction | Low |
| Return Shipment Creation | Generate return labels from admin | Streamlines returns process | Medium |
| Address Validation | Verify addresses before shipment creation | Reduces failed deliveries by 25% | Medium |

### 2.3 Label & Document Enhancements

| Feature | Description | Business Value | Effort |
|---------|-------------|----------------|--------|
| Batch Label Printing (Enhanced) | Print labels for 100+ orders simultaneously | Saves 4-5 hours daily for high-volume stores | Medium |
| Label Print Queue Management | Queue, prioritize, and manage large print jobs | Handle enterprise-level volumes efficiently | Medium |
| Packing Slip Generation | Auto-generate packing slips with labels | Professional customer experience | Low |
| Custom Label Templates | Customize label layout and branding | Brand consistency | Medium |
| Commercial Invoice (International) | Generate customs documents | Enable international shipping | High |
| Multi-Format Export | Export labels as PDF, PNG, ZPL (thermal printers) | Support various printer types | Low |

**Batch Printing Capabilities:**
- Process 100+ orders in a single batch
- Print queue with status tracking (queued, processing, completed, failed)
- Pause/resume functionality for large batches
- Automatic retry for failed label generations
- Print preview for entire batch
- Support for thermal printers (ZPL format)
- Download all labels as single PDF or individual files

### 2.4 Bulk & Scale Operations (CRITICAL)

| Feature | Description | Business Value | Effort |
|---------|-------------|----------------|--------|
| Bulk Shipment Creation (100+) | Select and process 100+ orders at once | Process 500 orders in 10 minutes vs 3 hours manually | High |
| Smart Batch Processing | Intelligent queuing system for large volumes | Handle enterprise-level order volumes | High |
| Filter-Based Bulk Selection | Auto-select orders by criteria (date, location, weight) | Quick selection of relevant orders | Medium |
| Bulk Action Templates | Save common bulk operation settings | Repeat daily workflows in one click | Low |
| Progress Tracking | Real-time progress bar with ETA | Transparency during large operations | Low |
| Partial Success Handling | Continue processing even if some orders fail | Don't lose entire batch due to one error | Medium |
| Bulk Operation History | Log all bulk operations with details | Audit trail and troubleshooting | Low |

**Bulk Processing Workflow:**
1. Select orders (filters, date range, manual selection, or "Select All")
2. Configure batch settings (carrier, service level, package defaults)
3. Preview and validate (see potential issues before processing)
4. Execute with progress tracking
5. Review results (success count, failed orders with reasons)
6. Print all labels in single action

### 2.5 Analytics & Reporting

| Feature | Description | Business Value | Effort |
|---------|-------------|----------------|--------|
| Shipping Cost Dashboard | Visualize shipping expenses by period | Identify cost-saving opportunities | Medium |
| COD Collection Report | Track COD amounts collected vs pending | Financial reconciliation | Low |
| Delivery Performance Metrics | Track on-time delivery rates by carrier | Optimize carrier selection | Medium |
| Failed Delivery Tracking | Monitor and manage failed deliveries | Reduce delivery failures | Low |

### 2.6 Branded Tracking Page (CRITICAL - Customer Experience)

**What:** A fully customizable tracking page hosted on your domain where customers check their order status.

**Why:** Replace generic carrier tracking pages with your branded experience, reduce "where's my order" support tickets by 60%, and build customer trust.

| Feature | Description | Business Value | Effort |
|---------|-------------|----------------|--------|
| Custom Domain Tracking | Host tracking page on merchant's domain (track.yourstore.com) | Professional branded experience | Medium |
| Real-Time Status Updates | Live tracking updates from carrier APIs | Reduce customer anxiety and support inquiries | Medium |
| Estimated Delivery Date | Show accurate delivery date predictions | Set proper expectations, reduce complaints | Medium |
| Order Details Display | Show items, quantities, images on tracking page | Complete order visibility for customers | Low |
| Delivery Instructions | Allow customers to add delivery notes | Reduce failed deliveries by 15% | Low |
| Branded Design | Customize colors, logo, fonts to match store | Consistent brand experience | Low |
| Multi-Language Support | Display tracking info in customer's language | Better international customer experience | Medium |
| Marketing Integration | Show product recommendations on tracking page | 5-10% additional revenue from upsells | Low |
| SMS/Email Notifications | Auto-notify customers of status changes | Proactive communication | Medium |
| Delivery Proof | Display proof of delivery (signature, photo) | Reduce delivery disputes | Low |

**Tracking Page Features:**
- Clean, mobile-responsive design
- Timeline view of shipment journey with milestones
- Map showing current package location (if available)
- Expected delivery window with countdown
- Delivery exception notifications with clear next steps
- Direct contact options for issues (chat, email, phone)
- Related order history for repeat customers
- Product recommendations based on order items
- Social sharing (for excited customers)

**Business Impact:**
- 60% reduction in "where's my order" support inquiries
- Customers self-serve tracking instead of contacting support
- Proactive notifications reduce anxiety
- Clear exception messaging prevents confusion
- Additional revenue from tracking page upsells

### 2.7 Shipping Rate Promotions (NEW - Competitive Advantage)

**Context:** This allows merchants to offer discounts/promotions on **OUR shipping rates** to their customers, making our service more attractive and driving more volume through our shipping company.

**What:** Allow merchants to offer discounts, promotions, or free shipping using our service to influence customer behavior at checkout.

**Why:** Drive cart conversions for merchants, increase our shipping volume, enable competitive pricing strategies, and make our service the preferred choice over other carriers.

| Feature | Description | Business Value | Effort |
|---------|-------------|----------------|--------|
| Rate Discount Engine | Apply percentage or fixed discounts to our shipping rates | Merchants increase conversion, we get more volume | Medium |
| Conditional Promotions | Trigger promotions based on rules (cart value, location, product) | Strategic shipping offers with our service boost merchant AOV | High |
| Free Shipping Campaigns | Merchants offer free shipping using our service | Proven 20-30% cart conversion increase, more shipments for us | Medium |
| Express Shipping Discounts | Discount our express service to move inventory | Clear stock faster, upsell to our premium service | Low |
| Service-Specific Promotions | Promote our specific service levels with better rates | Shift volume to our preferred/profitable services | Medium |
| Multi-Tier Thresholds | Different rates for different cart values | Encourage higher order values, more valuable shipments | Medium |
| Promo Code Integration | Shipping discounts via merchant promo codes | Marketing campaign flexibility using our service | Medium |
| A/B Testing Support | Test different promotion strategies with our rates | Optimize shipping promotions for mutual benefit | High |
| Geographic Targeting | Different promotions by region/country we serve | Region-specific marketing for our coverage areas | Medium |
| Time-Based Promotions | Flash sales on our shipping (e.g., free express before 2pm) | Create urgency, boost our daily volumes | Medium |

**Business Impact for Our Shipping Company:**
- **Volume Growth:** Promotional rates drive more checkouts using our service
- **Service Mix Optimization:** Promote our most profitable service levels
- **Competitive Advantage:** Merchants can't offer these promotions with other carriers
- **Merchant Acquisition:** Promotional capability attracts new merchant customers
- **Market Penetration:** Geographic promos help us expand into new regions
- **Merchant Stickiness:** Custom promotions create lock-in to our platform

**Promotion Types (All Using Our Service):**
1. **Percentage Discount:** "25% off [Our Company] shipping"
2. **Fixed Amount Discount:** "$5 off [Our Company] express shipping"
3. **Free Shipping:** "Free [Our Company] standard shipping on orders $50+"
4. **Buy-One-Get-Shipping-Free:** "Free [Our Company] shipping when you buy 2+ items"
5. **Upgrade Discount:** "[Our Company] express for the price of standard"
6. **Conditional Free Shipping:** "Free [Our Company] shipping to [cities we serve well]"
7. **Loyalty Rewards:** "Free [Our Company] shipping for VIP customers"
8. **Time-Limited:** "Free [Our Company] express if ordered before 2pm today"

**Strategic Use Cases:**
- **New Market Entry:** "Free shipping to [new city]" to build volume
- **Service Level Promotion:** Discount express to build premium service adoption
- **Competitive Defense:** Match competitor pricing in key markets
- **Merchant Incentives:** "Free shipping month" to attract new merchant signups
- **Capacity Management:** Promote off-peak shipping with discounts

**Promotion Configuration Interface:**
- Promotion name and description
- Discount type (percentage, fixed, free)
- Applicable carriers/service levels
- Trigger conditions:
  - Minimum cart value
  - Specific products/collections
  - Customer tags/segments
  - Shipping destination (city, state, country)
  - Date/time range
  - Promo code requirement
- Display settings (how promotion appears at checkout)
- Usage limits (total uses, per customer)
- Analytics tracking

**Customer-Facing Display:**
- Clear messaging at checkout: "🎉 You've unlocked free express shipping!"
- Strikethrough original price with promotional price
- Promotional badge on discounted shipping options
- Savings amount displayed: "You're saving $8.99 on shipping"
- Dynamic cart updates when thresholds are met

**Merchant Benefits:**
- Increase average order value with shipping thresholds
- Clear slow-moving inventory with promotional shipping
- Drive sales during slow periods
- Reward loyal customers automatically
- Compete with Amazon/big retailers on shipping
- Test what shipping offers drive conversions

**Example Use Cases:**
1. "Free shipping on orders over $75" → Increases AOV from $60 to $80
2. "50% off express shipping this weekend" → Weekend sales boost
3. "Free shipping to NYC customers" → Geographic expansion
4. "Free shipping on first order" → Customer acquisition
5. "Express shipping for $5 (save $10)" → Upgrade to faster delivery

---

## 3. NICE-TO-HAVE FEATURES (Could Have)

### 3.1 Automation Features

| Feature | Business Value | Implementation Complexity |
|---------|----------------|---------------------------|
| Auto-Fulfill Based on Rules | Saves manual processing time | Medium |
| Smart Carrier Selection | Automatically choose cheapest/fastest | Medium |
| Scheduled Shipment Creation | Process orders at optimal times | Low |
| Auto-Address Correction | Fix common address errors | High |

### 3.2 Advanced Features

| Feature | Business Value | Implementation Complexity |
|---------|----------------|---------------------------|
| Multi-Location Shipping | Ship from nearest warehouse | High |
| Shipping Insurance Options | Additional revenue + customer protection | Medium |
| Branded Tracking Page | Better customer experience | Medium |
| Estimated Delivery Dates | Reduces "where's my order" inquiries | Medium |

---

## 4. TECHNICAL SPECIFICATIONS

### 4.1 System Architecture

```
┌─────────────────┐
│  Shopify Store  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────┐
│   Shipping App Backend          │
│                                 │
│  ┌──────────────────────────┐  │
│  │  API Layer               │  │
│  │  - Rate Fetching         │  │
│  │  - Shipment Creation     │  │
│  │  - Label Generation      │  │
│  │  - COD Management        │  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐  │
│  │  Business Logic          │  │
│  │  - Validation            │  │
│  │  - Rate Calculation      │  │
│  │  - COD Fee Calculation   │  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐  │
│  │  Database Layer          │  │
│  │  - Orders                │  │
│  │  - Shipments             │  │
│  │  - Rates                 │  │
│  │  - COD Transactions      │  │
│  └──────────────────────────┘  │
└──────────┬──────────────────────┘
           │
           ▼
┌─────────────────────────────────┐
│   External Integrations         │
│  - Carrier APIs (FedEx, UPS...) │
│  - Address Validation           │
│  - Payment Gateways             │
└─────────────────────────────────┘
```

### 4.2 Database Schema Additions

#### New Tables

**`cod_transactions`**
- `id` (Primary Key)
- `order_id` (Foreign Key)
- `shipment_id` (Foreign Key)
- `cod_amount` (Decimal)
- `cod_fee` (Decimal)
- `collection_status` (Enum: pending, collected, failed)
- `collected_at` (Timestamp)
- `notes` (Text)
- `created_at` (Timestamp)

**`manual_shipments`**
- `id` (Primary Key)
- `order_id` (Foreign Key)
- `created_by_user_id` (Foreign Key)
- `carrier_id` (String)
- `service_level` (String)
- `is_partial` (Boolean)
- `line_items` (JSON)
- `created_at` (Timestamp)

**`rate_quotes`**
- `id` (Primary Key)
- `order_id` (Foreign Key)
- `carrier` (String)
- `service` (String)
- `rate` (Decimal)
- `quoted_at` (Timestamp)
- `expires_at` (Timestamp)

**`carrier_performance_metrics`** (NEW - for SLA Dashboard)
- `id` (Primary Key)
- `carrier_id` (String)
- `service_level` (String)
- `destination_city` (String)
- `destination_state` (String)
- `destination_country` (String)
- `avg_delivery_time_hours` (Integer)
- `on_time_percentage` (Decimal)
- `failure_rate` (Decimal)
- `total_shipments` (Integer)
- `failed_shipments` (Integer)
- `period_start` (Date)
- `period_end` (Date)
- `updated_at` (Timestamp)

**`shipment_events`** (NEW - for tracking and performance)
- `id` (Primary Key)
- `shipment_id` (Foreign Key)
- `event_type` (Enum: picked_up, in_transit, out_for_delivery, delivered, failed, returned)
- `event_timestamp` (Timestamp)
- `location` (String)
- `description` (Text)
- `carrier_status_code` (String)
- `created_at` (Timestamp)

**`delivery_failures`** (NEW - for failure tracking)
- `id` (Primary Key)
- `shipment_id` (Foreign Key)
- `order_id` (Foreign Key)
- `carrier_id` (String)
- `failure_reason` (Enum: wrong_address, customer_unavailable, refused, damaged, other)
- `failure_details` (Text)
- `failed_at` (Timestamp)
- `resolution_status` (Enum: pending, rescheduled, returned, cancelled)
- `resolved_at` (Timestamp)

**`shipping_promotions`** (NEW - for rate promotions)
- `id` (Primary Key)
- `merchant_id` (Foreign Key)
- `name` (String)
- `description` (Text)
- `promotion_type` (Enum: percentage, fixed_amount, free_shipping)
- `discount_value` (Decimal)
- `applicable_carriers` (JSON Array)
- `applicable_services` (JSON Array)
- `conditions` (JSON: min_cart_value, product_ids, customer_tags, destinations, etc.)
- `promo_code` (String, nullable)
- `start_date` (Timestamp)
- `end_date` (Timestamp)
- `usage_limit` (Integer, nullable)
- `usage_count` (Integer, default: 0)
- `per_customer_limit` (Integer, nullable)
- `is_active` (Boolean)
- `created_at` (Timestamp)
- `updated_at` (Timestamp)

**`promotion_usage`** (NEW - track promotion usage)
- `id` (Primary Key)
- `promotion_id` (Foreign Key)
- `order_id` (Foreign Key)
- `customer_id` (Foreign Key)
- `discount_applied` (Decimal)
- `original_rate` (Decimal)
- `final_rate` (Decimal)
- `carrier` (String)
- `service` (String)
- `used_at` (Timestamp)

**`tracking_page_views`** (NEW - analytics for tracking page)
- `id` (Primary Key)
- `shipment_id` (Foreign Key)
- `order_id` (Foreign Key)
- `customer_id` (Foreign Key, nullable)
- `ip_address` (String)
- `user_agent` (String)
- `viewed_at` (Timestamp)

**`bulk_operations`** (NEW - track bulk shipment creation)
- `id` (Primary Key)
- `operation_type` (Enum: bulk_shipment_creation, bulk_label_print)
- `initiated_by_user_id` (Foreign Key)
- `total_orders` (Integer)
- `successful_count` (Integer)
- `failed_count` (Integer)
- `status` (Enum: queued, processing, completed, failed)
- `settings` (JSON)
- `error_log` (JSON)
- `started_at` (Timestamp)
- `completed_at` (Timestamp)

### 4.3 API Endpoints

#### New Endpoints Required

**Shipment Management**
```
POST   /api/v1/shipments/create
GET    /api/v1/shipments/:id
PUT    /api/v1/shipments/:id
DELETE /api/v1/shipments/:id

POST   /api/v1/shipments/bulk-create
POST   /api/v1/shipments/bulk-validate
GET    /api/v1/shipments/bulk-status/:operation_id
```

**Rate Management**
```
GET    /api/v1/rates/fetch
POST   /api/v1/rates/compare
GET    /api/v1/rates/apply-promotions
```

**COD Management**
```
POST   /api/v1/cod/enable
GET    /api/v1/cod/transactions
PUT    /api/v1/cod/transactions/:id/mark-collected
GET    /api/v1/cod/reports/collection-summary
```

**Label Operations**
```
GET    /api/v1/labels/generate/:shipment_id
POST   /api/v1/labels/batch-print
GET    /api/v1/labels/batch-status/:batch_id
GET    /api/v1/labels/download/:shipment_id
POST   /api/v1/labels/queue-print
```

**Performance & Analytics (NEW)**
```
GET    /api/v1/analytics/carrier-performance
GET    /api/v1/analytics/carrier-performance/by-city
GET    /api/v1/analytics/delivery-times
GET    /api/v1/analytics/failure-rates
GET    /api/v1/analytics/cod-collection-times
POST   /api/v1/analytics/export-report
```

**Tracking Page (NEW)**
```
GET    /api/v1/tracking/:tracking_number
GET    /api/v1/tracking/:tracking_number/events
POST   /api/v1/tracking/:tracking_number/delivery-instructions
GET    /api/v1/tracking/page-config/:merchant_id
PUT    /api/v1/tracking/page-config/:merchant_id
POST   /api/v1/tracking/:tracking_number/notify-customer
```

**Shipping Promotions (NEW)**
```
POST   /api/v1/promotions/create
GET    /api/v1/promotions
GET    /api/v1/promotions/:id
PUT    /api/v1/promotions/:id
DELETE /api/v1/promotions/:id
POST   /api/v1/promotions/:id/activate
POST   /api/v1/promotions/:id/deactivate
GET    /api/v1/promotions/applicable
POST   /api/v1/promotions/validate
GET    /api/v1/promotions/:id/analytics
```

**Bulk Operations (NEW)**
```
POST   /api/v1/bulk/operations/create
GET    /api/v1/bulk/operations/:id/status
GET    /api/v1/bulk/operations/:id/results
POST   /api/v1/bulk/operations/:id/retry-failed
GET    /api/v1/bulk/operations/history
```

**Reports**
```
GET    /api/v1/reports/shipping-costs
GET    /api/v1/reports/cod-collections
GET    /api/v1/reports/delivery-performance
GET    /api/v1/reports/carrier-sla
GET    /api/v1/reports/failed-deliveries
GET    /api/v1/reports/promotion-performance
```

### 4.4 Integration Requirements

| Integration | Purpose | API Documentation Needed |
|-------------|---------|-------------------------|
| Shopify Admin API | Order management, fulfillment | ✅ Available |
| Shopify Payments API | COD payment processing | ✅ Available |
| **Our Shipping API** | Create shipments, track packages, get rates (OUR INTERNAL SYSTEM) | ✅ Internal documentation |
| **Our Label Generation System** | Generate shipping labels for our service | ✅ Internal documentation |
| **Our Tracking System** | Real-time tracking updates from our logistics network | ✅ Internal documentation |
| **Our Performance Analytics** | Pull delivery performance data from our systems | 🔨 Needs to be built/exposed |
| **Our COD Collection System** | Track COD payments through our network | 🔨 Needs to be built/exposed |
| Address Validation Service | Verify shipping addresses | Recommended: SmartyStreets or internal solution |
| Webhook System | Real-time order updates from Shopify | ✅ Shopify webhooks available |
| **Our Routing System** | Optimize delivery routes (optional integration) | Internal |
| **Our Driver App** | Sync delivery status, COD collection (optional) | Internal |

**Critical Internal Integrations Needed:**
1. **Our Core Shipping Platform API**
   - Create shipments
   - Generate tracking numbers
   - Assign to routes
   - Update delivery status

2. **Our Performance Data Warehouse**
   - Query historical delivery times
   - Failure rate statistics
   - COD collection metrics
   - Route performance data

3. **Our Label Printing System**
   - Generate labels in required formats
   - Support for thermal printers
   - Batch label generation

4. **Our Customer Tracking Portal**
   - Expose tracking data via API
   - Real-time status updates
   - Delivery proof images

**Data Flow:**
```
Shopify Store → Our App → Our Shipping API → Our Logistics Network
                    ↓
              Performance Analytics ← Our Delivery Data
                    ↓
              Merchant Dashboard
```

---

## 5. USER INTERFACE REQUIREMENTS

### 5.1 Admin Panel Screens

#### Screen 1: Manual Shipment Creation
**Location:** Order Details Page  
**Components:**
- "Create Shipment" button
- Shipment creation modal with:
  - Line item selector (for partial shipments)
  - Carrier dropdown
  - Service level dropdown
  - Package details (weight, dimensions)
  - Rate display with promotional pricing if applicable
  - COD toggle and amount field
  - Preview pane
  - "Create & Print Label" button

#### Screen 2: Rate Calculator
**Location:** Standalone page + widget  
**Components:**
- Order selector
- Carrier filter
- Rate comparison table with promotional rates highlighted
- "Refresh Rates" button
- Export rates to CSV

#### Screen 3: COD Management Dashboard
**Location:** New menu item  
**Components:**
- COD orders list (pending collection)
- Collection status filter
- Total COD pending amount
- "Mark as Collected" bulk action
- COD reconciliation report
- Average collection time metric

#### Screen 4: Bulk Shipment Creation (ENHANCED)
**Location:** Orders page  
**Components:**
- Multi-select checkbox on orders list
- Advanced filter panel:
  - Date range selector
  - Order status filter
  - Shipping destination filter
  - Weight/value range
  - Tag filter
- "Select All" / "Select Filtered" buttons (handles 100+ orders)
- Bulk action bar with order count
- "Bulk Create Shipments" button
- Bulk processing modal:
  - Default carrier/service selection
  - Package template application
  - Preview validation warnings
  - Start processing button
- Progress tracking interface:
  - Real-time progress bar
  - Current/total count (e.g., "Processing 127 of 250")
  - Estimated time remaining
  - Live log of completed orders
  - Pause/Resume controls
- Results summary screen:
  - Success count with green badge
  - Failed count with red badge
  - Downloadable error report
  - "Print All Labels" button
  - "Retry Failed" button

#### Screen 5: Batch Label Printing Queue
**Location:** Standalone page  
**Components:**
- Print queue table showing:
  - Batch ID
  - Order count
  - Status (queued, processing, completed, failed)
  - Creation time
  - Completion time
  - Actions (download, retry, cancel)
- "New Print Batch" button
- Print job configuration:
  - Label format selector (PDF, PNG, ZPL)
  - Printer selection (for direct printing)
  - Packing slip inclusion toggle
  - Commercial invoice for international
- Queue management actions:
  - Pause/Resume batch
  - Reorder priority
  - Cancel batch
  - Download all as ZIP

#### Screen 6: Performance & SLA Dashboard (NEW - CRITICAL)
**Location:** Main navigation - "Analytics" or "Performance"  
**Components:**

**Overview Section:**
- Key metrics cards:
  - Overall on-time delivery %
  - Average delivery time
  - Active shipments
  - Failed deliveries this week
  
**Carrier Performance Comparison:**
- Side-by-side carrier comparison table:
  - Carrier name with logo
  - Avg delivery time
  - On-time %
  - Failure rate
  - Cost per delivery
  - Total shipments
  - Performance trend (↑↓)
- Sortable by any metric
- Date range selector

**City-Wise Performance Map:**
- Interactive map showing delivery performance by city
- Color-coded by delivery speed (green=fast, yellow=medium, red=slow)
- Click city for detailed breakdown
- Filter by carrier

**Delivery Time Analysis:**
- Line chart showing average delivery times over time
- Multiple carriers plotted for comparison
- Breakdown by service level (standard, express, etc.)

**Failure Analysis:**
- Pie chart of failure reasons
- Table of top failing destinations
- Carrier-specific failure rates
- Actionable insights (e.g., "Switch carrier for NYC deliveries")

**COD Collection Time Metrics:**
- Average days from delivery to collection
- Histogram of collection timeframes
- By carrier comparison
- By destination analysis
- Cash flow impact calculator

**Export Options:**
- Download as PDF report
- Export raw data to CSV/Excel
- Schedule automated reports
- Share report link with team

#### Screen 7: Tracking Page Configuration (NEW)
**Location:** Settings > Tracking Page  
**Components:**

**Branding Settings:**
- Logo upload
- Color picker for primary/secondary colors
- Font family selector
- Custom CSS editor (advanced)

**Domain Settings:**
- Custom subdomain configuration (track.yourstore.com)
- SSL certificate status

**Display Options:**
- Toggle map display
- Toggle estimated delivery
- Toggle order items display
- Toggle product recommendations
- Toggle delivery instructions
- Choose notification preferences

**Content Configuration:**
- Welcome message editor
- Delivery instructions text
- Contact information display
- Social media links
- Footer content

**Marketing Integration:**
- Product recommendation rules
- Upsell product selector
- Banner content editor

**Notification Settings:**
- Email template customization
- SMS template editor
- Notification triggers (shipped, out for delivery, delivered)
- Timing configuration

**Preview Pane:**
- Live preview of tracking page
- Mobile/desktop view toggle
- Sample tracking data

#### Screen 8: Shipping Promotions Manager (NEW - CRITICAL)
**Location:** Main navigation - "Marketing" > "Shipping Promotions"  
**Components:**

**Promotions List View:**
- Table showing all promotions:
  - Promotion name
  - Type (%, fixed, free)
  - Status (active, scheduled, expired, draft)
  - Conditions summary
  - Usage count / limit
  - Conversion impact
  - Actions (edit, duplicate, activate/deactivate, delete)
- "Create Promotion" button
- Filter by status, type, date range
- Search by name/description

**Create/Edit Promotion Modal:**

*Basic Info Tab:*
- Promotion name
- Description (shown to customers)
- Promotion type selector:
  - Percentage discount
  - Fixed amount discount
  - Free shipping
  - Upgrade discount
- Discount value input

*Applicability Tab:*
- Carrier selection (multi-select)
- Service level selection
- "Apply to all" checkbox

*Conditions Tab:*
- Minimum cart value
- Maximum cart value
- Product/collection selector
- Customer segment selector (VIP, first-time, returning)
- Shipping destination builder:
  - Country selector
  - State/province selector
  - City input (comma-separated)
  - ZIP code ranges
- Time-based conditions:
  - Start date/time
  - End date/time
  - Recurring schedule (e.g., every weekend)
  - Time-of-day restrictions

*Promo Code Tab:*
- Require promo code toggle
- Promo code input
- Auto-generate code button
- Code usage limits
- Per-customer limit

*Display Settings Tab:*
- Badge text (e.g., "🎉 Free Shipping!")
- Badge color
- Highlight style
- Savings message format
- Threshold messaging (e.g., "Add $15 more for free shipping")

*Limits & Rules Tab:*
- Total usage limit
- Per-customer usage limit
- Combine with other promotions toggle
- Priority level (if multiple promotions apply)

*Preview Pane:*
- Checkout preview showing how promotion appears
- Example calculations
- Mobile view

**Promotion Analytics View:**
- Performance metrics:
  - Total uses
  - Conversion rate impact
  - Revenue attributed
  - Average order value change
  - Total discount given
  - Top performing regions
- Chart of promotion usage over time
- Order list of promotion users
- Export analytics

**Promotion Templates:**
- Quick-start templates:
  - "Free shipping over $X"
  - "Weekend free express"
  - "First order free shipping"
  - "Geographic promo"
  - "Clearance sale shipping"
- One-click template application with customization

### 5.2 Customer-Facing UI

#### Checkout Page (ENHANCED)
- COD payment option radio button
- COD fee display
- COD terms and conditions checkbox
- **Promotional rate display:**
  - Original rate with strikethrough
  - Promotional rate highlighted
  - Savings badge (e.g., "Save $8.99!")
  - Promotional message (e.g., "🎉 You've unlocked free express shipping!")
  - Threshold indicator (e.g., "Add $12 more for free shipping")
  - Progress bar towards free shipping threshold

#### Tracking Page (NEW - Customer-Facing)
**URL:** track.merchantstore.com/[tracking_number] or merchantstore.com/pages/track/[tracking_number]

**Header:**
- Merchant logo
- Store branding
- Order number
- "Need help?" link

**Tracking Timeline:**
- Visual timeline/progress bar
- Current status highlighted
- Completed steps with checkmarks
- Future steps grayed out
- Timestamps for each event
- Estimated delivery date prominently displayed
- Countdown to delivery (if arriving today/tomorrow)

**Order Details:**
- Product images
- Product names and quantities
- Order total
- Shipping address (partial for privacy)

**Delivery Information:**
- Carrier name and logo
- Service level
- Tracking number (copyable)
- Estimated delivery window
- Current location (if available)
- "View on carrier site" link

**Map Display (optional):**
- Package current location
- Destination marker
- Route visualization

**Delivery Instructions:**
- "Add delivery instructions" button
- Text input for special instructions
- Common options (leave at door, ring bell, etc.)

**Notifications:**
- SMS/Email notification signup
- Preferred notification settings

**Customer Actions:**
- "Report an issue" button
- "Contact support" button
- Live chat integration

**Marketing Section:**
- "You might also like" product recommendations
- Related products carousel
- Special offers banner
- Newsletter signup

**Footer:**
- Store contact info
- Social media links
- Return policy link
- Privacy policy
- Powered by branding (optional)

**Mobile Optimized:**
- Responsive design
- Swipeable timeline
- Tap-to-call support
- Easy instruction submission

---

## 6. SECURITY & COMPLIANCE

### 6.1 Security Requirements

| Requirement | Description | Priority |
|-------------|-------------|----------|
| API Authentication | OAuth 2.0 for all API calls | Critical |
| Data Encryption | Encrypt sensitive data at rest and in transit | Critical |
| Role-Based Access | Limit shipment creation to authorized users | High |
| Audit Logging | Log all shipment and COD transactions | High |
| PCI Compliance | Ensure COD flow doesn't violate PCI requirements | Critical |

### 6.2 Data Privacy

- GDPR compliance for customer address data
- Data retention policy (keep shipment data for 7 years)
- Secure deletion of customer data upon request
- Privacy policy update to include COD data handling

---

## 7. PERFORMANCE REQUIREMENTS

| Metric | Target | Current |
|--------|--------|---------|
| Rate Fetching Response Time | < 3 seconds | N/A |
| Label Generation Time | < 2 seconds | ~1.5 seconds |
| Bulk Shipment Processing | 100 orders/minute | N/A |
| System Uptime | 99.9% | 99.5% |
| API Rate Limit Handling | Graceful degradation | N/A |

---

## 8. TESTING REQUIREMENTS

### 8.1 Test Scenarios

**COD Testing:**
- ✓ COD option appears at checkout
- ✓ COD fee calculated correctly (fixed and percentage)
- ✓ COD amount shows on label
- ✓ Order marked as COD in admin
- ✓ COD collection workflow works end-to-end
- ✓ COD reconciliation report accuracy

**Manual Shipment Testing:**
- ✓ Create shipment from admin for any order
- ✓ Create partial shipment with selected line items
- ✓ Bulk create 100+ shipments successfully
- ✓ Error handling for invalid data
- ✓ Label prints correctly
- ✓ Rate selection works for manual shipments
- ✓ Address validation prevents bad addresses

**Rate Fetching Testing:**
- ✓ Rates fetched for domestic order
- ✓ Rates fetched for international order
- ✓ Multi-carrier comparison works
- ✓ Rate caching functions properly (15-minute TTL)
- ✓ Handle carrier API failures gracefully
- ✓ Promotional rates calculated correctly

**Bulk Operations Testing:**
- ✓ Select and process 100 orders
- ✓ Select and process 250+ orders
- ✓ Filter-based selection works correctly
- ✓ Progress tracking updates in real-time
- ✓ Partial success handling (some succeed, some fail)
- ✓ Error reporting shows specific failures
- ✓ Retry failed orders functionality
- ✓ Pause/resume bulk operations
- ✓ Batch label printing for 100+ labels
- ✓ Queue management works correctly

**Performance Dashboard Testing:**
- ✓ Carrier metrics calculated accurately
- ✓ City-wise data displays correctly
- ✓ Delivery time averages match reality
- ✓ Failure rates calculated correctly
- ✓ COD collection time tracking works
- ✓ Date range filtering functions properly
- ✓ Export reports generate correctly
- ✓ Dashboard loads within 3 seconds
- ✓ Data refreshes automatically

**Tracking Page Testing:**
- ✓ Custom domain setup works
- ✓ Tracking data displays correctly
- ✓ Real-time updates from carrier APIs
- ✓ Branded design renders properly
- ✓ Mobile responsiveness
- ✓ Delivery instructions submission works
- ✓ Notifications sent correctly
- ✓ Product recommendations display
- ✓ Customer analytics tracking
- ✓ Multi-language support (if applicable)

**Shipping Promotions Testing:**
- ✓ Promotion creation saves correctly
- ✓ Percentage discount calculates accurately
- ✓ Fixed amount discount applies correctly
- ✓ Free shipping applies when conditions met
- ✓ Cart threshold triggers work
- ✓ Geographic targeting works (city, state, country)
- ✓ Product/collection conditions work
- ✓ Customer segment targeting works
- ✓ Promo code requirement enforces correctly
- ✓ Usage limits respected
- ✓ Per-customer limits enforced
- ✓ Multiple promotions priority works
- ✓ Time-based activation/expiration
- ✓ Checkout display shows promotions correctly
- ✓ Savings message displays accurately
- ✓ Threshold messaging shows correctly
- ✓ Promotion analytics track accurately

**Integration Testing:**
- ✓ Shopify checkout integration works
- ✓ Carrier API calls succeed
- ✓ Webhook processing works
- ✓ Payment gateway integration (for COD)
- ✓ Address validation service integration
- ✓ Email/SMS notification delivery

**Performance & Load Testing:**
- ✓ 100 concurrent users on tracking page
- ✓ Bulk processing 500 orders simultaneously
- ✓ Dashboard loads with 10,000+ historical shipments
- ✓ Rate API handles 1000 requests/minute
- ✓ Label generation under load (100 labels/minute)
- ✓ Database query performance optimized

### 8.2 Test Environments

- Development environment (isolated testing)
- Staging environment (Shopify test store)
- Production environment (gradual rollout)

---

## 9. DEPLOYMENT & ROLLOUT PLAN

### Phase 1: Foundation (Weeks 1-4)
**Core Features:**
- ✅ COD payment integration
- ✅ Manual shipment creation (single order)
- ✅ Rate fetching API
- ✅ Basic performance tracking infrastructure

**Deliverables:**
- COD enabled for test store
- Admin can create shipments manually
- Rate calculator functional
- Database schema deployed
- Basic analytics collection started

**Testing Focus:**
- COD payment flow end-to-end
- Manual shipment creation
- Rate fetching accuracy

### Phase 2: Bulk Operations & Tracking (Weeks 5-8)
**Core Features:**
- ✅ Bulk shipment creation (100+ orders)
- ✅ Batch label printing with queue management
- ✅ Partial shipment support
- ✅ Address validation
- ✅ Shipment tracking integration
- ✅ Basic tracking page (unbranded)

**Deliverables:**
- Bulk operations working for high-volume merchants
- Print queue functional
- Tracking page beta deployed
- Performance metrics collection active

**Testing Focus:**
- Load testing with 250+ orders
- Batch printing stress test
- Tracking API reliability

### Phase 3: Performance Dashboard & Promotions (Weeks 9-12)
**Core Features:**
- ✅ Carrier SLA Dashboard
- ✅ City-wise performance analytics
- ✅ Failure rate tracking
- ✅ COD collection time metrics
- ✅ Shipping promotions engine
- ✅ Promotion management UI
- ✅ Branded tracking page

**Deliverables:**
- Full performance dashboard live
- Merchants can create shipping promotions
- Tracking page fully customizable
- Comprehensive reporting available

**Testing Focus:**
- Dashboard performance with large datasets
- Promotion calculation accuracy
- Tracking page customization

### Phase 4: Advanced Features & Optimization (Weeks 13-16)
**Core Features:**
- ✅ Automated tracking emails/SMS
- ✅ Advanced promotion rules (A/B testing)
- ✅ Multi-language tracking page support
- ✅ Analytics export automation
- ✅ Performance optimizations
- ✅ User feedback incorporation

**Deliverables:**
- Full feature set deployed
- Documentation complete
- Training materials ready
- Performance benchmarks met
- Production-ready app

**Testing Focus:**
- End-to-end integration testing
- User acceptance testing
- Performance tuning
- Security audit

### Beta Testing Program (Weeks 8-12)
**Participants:**
- 5 low-volume merchants (< 50 orders/day)
- 3 medium-volume merchants (50-200 orders/day)
- 2 high-volume merchants (200+ orders/day)

**Beta Features:**
- Bulk operations
- Tracking page
- Performance dashboard
- Shipping promotions

**Feedback Collection:**
- Weekly surveys
- Usage analytics
- Bug reports
- Feature requests

### Gradual Rollout Strategy
1. **Internal Testing** (Week 1-2): Anthropic/development team
2. **Alpha Testing** (Week 3-4): 2-3 friendly merchants
3. **Beta Testing** (Week 8-12): 10 selected merchants
4. **Limited Release** (Week 13): 100 existing users
5. **General Availability** (Week 16): All users

### Feature Flags
Enable gradual feature rollout:
- `enable_bulk_operations`
- `enable_performance_dashboard`
- `enable_shipping_promotions`
- `enable_branded_tracking_page`
- `enable_cod_advanced_features`

### Rollback Plan
- Database migration rollback scripts ready
- Feature flags allow instant disable
- Previous version maintained for 2 weeks
- Automated backup before each deployment

---

## 10. SUCCESS METRICS

### Key Performance Indicators (KPIs)

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| COD Adoption Rate | 15% of orders | Orders with COD / Total orders |
| Manual Shipment Usage | 25% of shipments | Manual shipments / Total shipments |
| Bulk Operation Usage | 60% of high-volume merchants | Merchants using bulk features weekly |
| Time Saved per Shipment | 2 minutes | Before/after time study |
| Time Saved per Bulk Operation | 90% reduction | Manual vs automated time comparison |
| Failed Delivery Rate | < 2% | Failed deliveries / Total deliveries |
| Tracking Page Usage | 70% of customers | Unique tracking page views / Orders |
| Promotion Conversion Impact | +25% cart conversion | A/B test with/without promotions |
| User Satisfaction | 4.5/5 stars | User survey and app reviews |
| Support Tickets Reduction | 40% decrease | Shipping-related tickets (tracking inquiries) |
| Dashboard Engagement | 80% of merchants use weekly | Weekly active dashboard users / Total merchants |
| Promotion Usage | 50% of merchants create promotions | Merchants with active promotions |

### Business Impact Goals

**Revenue Impact:**
- Enable $50K+ in COD orders within 3 months
- Generate $25K+ in additional revenue from promotion-driven conversions
- Increase average order value by 15% through shipping threshold promotions

**Operational Efficiency:**
- Process 60% more orders with same staff (via bulk operations)
- Reduce label printing time from 5 hours/day to 30 minutes/day
- Reduce manual shipment creation time by 90%
- Save 10+ hours/week for operations teams

**Customer Satisfaction:**
- Reduce shipping complaints by 45%
- Reduce "where's my order" support tickets by 60%
- Increase repeat purchase rate by 20% (better tracking experience)
- Achieve 4.5+ star rating on tracking page experience

**Cost Savings:**
- Reduce failed deliveries saving $15K/year (via address validation)
- Optimize carrier selection saving $20K/year (via performance dashboard)
- Reduce support costs by $30K/year (via self-service tracking)
- Identify and switch from underperforming carriers

**Merchant Engagement:**
- 80% of merchants use performance dashboard weekly
- 90% of high-volume merchants use bulk operations
- 50% of merchants create at least one shipping promotion
- 70% of merchants customize tracking page

### Feature-Specific Metrics

**Bulk Operations:**
- Average batch size: 50+ orders
- Batch success rate: >95%
- Time per 100 orders: <10 minutes
- Daily bulk operations: 200+ across all merchants

**Performance Dashboard:**
- Average time to identify carrier issues: <1 day
- Carrier switches based on data: 10+ per month
- Cost savings identified: $2K+ per merchant annually

**Tracking Page:**
- Page load time: <2 seconds
- Mobile traffic: >60%
- Average time on page: 45+ seconds
- Upsell conversion rate: 2-3%

**Shipping Promotions:**
- Average AOV increase: 18%
- Free shipping threshold hit rate: 65%
- Promo code usage rate: 30%
- Promotion-influenced conversions: 25%+

### Analytics Dashboard Metrics
Track and display to merchants:
- Total shipments created (daily, weekly, monthly)
- Average shipping cost per order
- Carrier distribution (% by carrier)
- Service level distribution (% express vs standard)
- COD order percentage and total value
- Failed delivery rate trend
- On-time delivery percentage
- Customer tracking engagement
- Promotion performance
- Cost savings from app usage

---

## 11. RISKS & MITIGATION

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| Carrier API downtime | High | Medium | Implement fallback carriers, cache rates, show cached rates with timestamp |
| COD fraud | High | Low | Address verification, order value limits, fraud detection, merchant verification |
| Poor user adoption of new features | Medium | Medium | Comprehensive training, in-app tutorials, promotional campaigns, beta program |
| Performance issues at scale (bulk operations) | High | Medium | Load testing with 1000+ orders, horizontal scaling plan, queue-based processing |
| Integration bugs | Medium | High | Extensive testing, staged rollout, feature flags for quick disable |
| Security vulnerabilities | High | Low | Security audit, penetration testing, code review, regular dependency updates |
| Tracking page performance under load | High | Medium | CDN implementation, caching strategy, database optimization |
| Promotion calculation errors | High | Medium | Comprehensive test suite, dry-run mode, manual review for complex rules |
| Data accuracy in performance dashboard | High | Medium | Data validation, reconciliation checks, carrier API reliability monitoring |
| Bulk operations overwhelming carrier APIs | Medium | Medium | Rate limiting, intelligent batching, carrier API quota management |
| Promotion abuse (users gaming system) | Medium | Medium | Usage limits, fraud detection, anomaly monitoring, merchant alerts |
| Privacy concerns with tracking page | Medium | Low | Anonymize data, GDPR compliance, clear privacy policy, opt-out options |
| Complexity overwhelming merchants | Medium | High | Simplified UI/UX, wizard-based setup, templates, good defaults |
| Carrier contract conflicts | High | Low | Legal review of promotion terms, carrier agreement compliance check |
| Database performance degradation | High | Medium | Query optimization, proper indexing, archival strategy, monitoring |
| Failed label generation in bulk | Medium | High | Retry mechanism, partial success handling, clear error reporting |
| Promotion conflicts (multiple active) | Medium | Medium | Priority system, conflict detection, merchant warnings |
| International shipping complexity | High | Medium | Phase international features separately, extensive testing per country |

---

## 12. SUPPORT & MAINTENANCE

### 12.1 Documentation Required

- ✓ Admin user guide (how to create shipments, manage COD)
- ✓ Technical API documentation
- ✓ Troubleshooting guide
- ✓ Video tutorials for common tasks
- ✓ FAQ section

### 12.2 Training Plan

**For Admins/Operations:**
- 2-hour training session on new features
- Hands-on workshop with test orders
- Quick reference guides

**For Customer Service:**
- COD policy and procedures
- How to assist customers with COD orders
- Tracking and shipment status updates

### 12.3 Ongoing Maintenance

- Weekly monitoring of system performance
- Monthly review of COD transactions
- Quarterly feature enhancement reviews
- Annual security audit

---

## 13. BUDGET & RESOURCES

### 13.1 Development Team Requirements

| Role | Time Allocation | Responsibility |
|------|----------------|----------------|
| Backend Developer | Full-time (12 weeks) | API development, integrations |
| Frontend Developer | Full-time (8 weeks) | Admin UI, checkout modifications |
| QA Engineer | Full-time (6 weeks) | Testing, quality assurance |
| DevOps Engineer | Part-time (4 weeks) | Deployment, infrastructure |
| Product Manager | Part-time (12 weeks) | Requirements, coordination |
| UI/UX Designer | Part-time (3 weeks) | Interface design, user flows |

### 13.2 External Costs

| Item | Estimated Cost | Notes |
|------|---------------|-------|
| Carrier API access fees | $200/month | For testing and development |
| Address validation service | $100/month | SmartyStreets or similar |
| Additional hosting resources | $150/month | Increased server capacity |
| Payment gateway fees (COD) | Variable | Based on transaction volume |
| Testing tools & services | $300 one-time | Load testing, security scanning |

### 13.3 Total Estimated Budget

- **Development:** 12 weeks × team costs
- **Infrastructure:** $450/month ongoing
- **One-time costs:** ~$5,000 (tools, setup, testing)

---

## 14. APPROVAL & SIGN-OFF

### Stakeholder Approval Required

| Stakeholder | Role | Approval Status | Date |
|-------------|------|-----------------|------|
| Product Owner | Final requirements approval | ⬜ Pending | |
| Technical Lead | Technical feasibility | ⬜ Pending | |
| Finance Manager | Budget approval | ⬜ Pending | |
| Operations Manager | Workflow approval | ⬜ Pending | |
| Security Officer | Security review | ⬜ Pending | |

---

## 15. APPENDICES

### Appendix A: User Stories (Detailed)

**Epic 1: Cash on Delivery**
1. As a customer, I want to select COD at checkout so I can pay when my order arrives
2. As a store owner, I want to configure COD fees so I can cover collection costs
3. As a courier, I want to see COD amounts on labels so I know what to collect
4. As an accountant, I want to track COD collections so I can reconcile payments
5. As a finance manager, I want to see COD collection time metrics so I can forecast cash flow

**Epic 2: Manual Shipment Creation**
1. As an admin, I want to create shipments from any order so I can handle special cases
2. As a warehouse manager, I want to create partial shipments so I can ship available items first
3. As an operations manager, I want to bulk create shipments so I can process orders faster
4. As a fulfillment agent, I want to manually select carriers so I can choose the best option for special deliveries
5. As a customer service rep, I want to create shipments for customer-requested carriers

**Epic 3: Rate Management**
1. As a CS rep, I want to fetch shipping rates on-demand so I can quote customers
2. As an operations manager, I want to compare carrier rates so I can choose the best option
3. As a store owner, I want to see promotional rates so I can understand discounts being offered

**Epic 4: Bulk Operations & Scale**
1. As a warehouse manager, I want to select 100+ orders at once so I can process high volumes efficiently
2. As an operations manager, I want to print 250 labels in one batch so I can save hours daily
3. As a fulfillment supervisor, I want to see progress when processing large batches so I know when to expect completion
4. As an admin, I want to retry failed shipments in a bulk operation so I don't have to start over
5. As a high-volume merchant, I want to filter and select orders by criteria so I can target specific order types
6. As an operations lead, I want to pause bulk operations so I can handle urgent interruptions

**Epic 5: Performance & Visibility Dashboard**
1. As a store owner, I want to see which carrier performs best in each city so I can optimize delivery
2. As an operations manager, I want to track failure rates by carrier so I can switch underperformers
3. As a logistics coordinator, I want to see average delivery times so I can set accurate customer expectations
4. As a finance manager, I want to track COD collection times so I can improve cash flow
5. As a director, I want to export performance reports so I can share with stakeholders
6. As a merchant, I want to see cost per delivery by zone so I can optimize pricing
7. As an analyst, I want historical performance data so I can identify trends

**Epic 6: Branded Tracking Page**
1. As a customer, I want to track my order on the merchant's website so I have a seamless experience
2. As a merchant, I want to customize my tracking page so it matches my brand
3. As a customer, I want to add delivery instructions so my package arrives safely
4. As a merchant, I want to show product recommendations on tracking pages so I can drive additional sales
5. As a customer, I want to receive automatic notifications so I know when my package arrives
6. As a merchant, I want to see tracking page analytics so I understand customer engagement
7. As a customer, I want to see estimated delivery dates so I can plan to be home
8. As an international customer, I want tracking in my language so I can understand the status

**Epic 7: Shipping Promotions**
1. As a merchant, I want to offer free shipping over $50 so I can increase average order value
2. As a marketing manager, I want to create weekend free express shipping so I can boost weekend sales
3. As a store owner, I want to offer free shipping to specific cities so I can expand to new markets
4. As a merchant, I want to give first-time customers free shipping so I can acquire new customers
5. As an operations manager, I want to discount specific carriers so I can shift volume to preferred partners
6. As a marketing director, I want to run A/B tests on shipping promotions so I can optimize conversions
7. As a merchant, I want to show "Add $X more for free shipping" so I can encourage larger carts
8. As a store owner, I want to reward VIP customers with free shipping so I can increase loyalty
9. As a merchant, I want to see promotion analytics so I can measure ROI
10. As a seasonal business, I want time-based promotions so I can clear inventory during peaks

### Appendix B: Glossary

**Shipping & Logistics Terms:**
- **COD:** Cash on Delivery - payment collected at delivery
- **Fulfillment:** Process of preparing and shipping an order
- **Carrier:** Shipping company (e.g., FedEx, UPS, USPS, DHL)
- **Service Level:** Shipping speed tier (e.g., Standard, Express, Overnight)
- **Partial Shipment:** Shipping some items from an order separately
- **Rate:** Shipping cost quote from a carrier
- **Label:** Physical shipping label affixed to package
- **Webhook:** Automated notification sent when an event occurs
- **SLA:** Service Level Agreement - carrier's promised delivery standards
- **RTO:** Return to Origin - package returned to sender due to delivery failure
- **Proof of Delivery:** Evidence that package was delivered (signature, photo)
- **Tracking Number:** Unique identifier for a shipment
- **Last Mile:** Final step of delivery (carrier facility to customer door)
- **Zone:** Geographic pricing area used by carriers

**App-Specific Terms:**
- **Bulk Operation:** Processing multiple orders simultaneously (100+)
- **Batch Printing:** Printing multiple labels in one job
- **Print Queue:** System for managing large print jobs
- **Manual Shipment:** Shipment created by admin (not automatically at checkout)
- **Rate Promotion:** Discount or offer on shipping rates
- **Tracking Page:** Branded customer-facing page for order tracking
- **Performance Dashboard:** Analytics view of carrier performance
- **Carrier SLA Dashboard:** Specific view of carrier delivery metrics
- **Promotional Rate:** Discounted shipping rate from merchant promotion
- **Threshold Promotion:** Free/discounted shipping above cart value
- **Promotion Engine:** System that calculates and applies shipping promotions

**Technical Terms:**
- **API:** Application Programming Interface - how systems communicate
- **JSON:** JavaScript Object Notation - data format
- **Enum:** Enumeration - predefined list of values
- **Foreign Key:** Database field linking to another table
- **Cache:** Temporary storage for faster access
- **Rate Limiting:** Restricting number of API calls
- **Queue:** Ordered list of tasks to be processed
- **CDN:** Content Delivery Network - faster global content delivery
- **Feature Flag:** Toggle to enable/disable features
- **A/B Testing:** Comparing two versions to see which performs better

### Appendix C: Reference Documents

- Shopify Admin API Documentation: https://shopify.dev/docs/api/admin
- Shopify Fulfillment API: https://shopify.dev/docs/api/admin-rest/resources/fulfillment
- Carrier API Documentation: [To be added based on carrier selection]

---

## Document Control

**Last Updated:** February 10, 2026  
**Next Review Date:** February 24, 2026  
**Document Owner:** Product Manager  
**Distribution:** Development Team, Management, Stakeholders

---

## Feedback & Questions

For questions or clarifications about this requirements document, please contact:
- Product Manager: [Contact info]
- Technical Lead: [Contact info]

To provide feedback or suggest changes, please use the comments section or submit a change request form.

---

**END OF DOCUMENT**
