# Flask Weather Application

Welcome to the Flask Weather Application! This application allows users to retrieve weather information for a specific city using the OpenWeatherMap API and store the searched cities in a MongoDB database.

## Features

- **Weather Information**: Users can search for weather information for a specific city, including temperature (in Celsius), description, and weather icon.
- **City Database**: Searched cities are stored in a MongoDB database to prevent redundant queries.
- **Error Handling**: The application provides error handling for invalid city names and existing cities in the database.
- **User Interface**: Simple and intuitive user interface built using Flask and HTML templates.

## Installation

To run the application locally, follow these steps:

1. **Clone the Repository**: Clone this GitHub repository to your local machine using the following command:
   ```
   git clone https://github.com/yourusername/flask-weather-app.git
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies using pip:
   ```
   cd flask-weather-app
   pip install -r requirements.txt
   ```

3. **Set Up MongoDB**: Ensure that you have MongoDB installed and running on your local machine. Update the MongoDB connection string (`mongodb://localhost:27017/`) in the `app.py` file if necessary.

4. **Run the Flask Application**: Start the Flask server by running the following command:
   ```
   python app.py
   ```

5. **Access the Application**: Once the server is running, access the application in your web browser at [http://localhost:5000/](http://localhost:5000/).

## Usage

1. **Search for Weather**: Enter the name of the city you want to search for in the input field and click the "Search" button.
2. **View Weather Information**: Weather information for the specified city will be displayed, including temperature, description, and weather icon.
3. **Error Handling**: If the city is not found or already exists in the database, appropriate error messages will be displayed.

## Contributing

Contributions to improve and enhance the application are welcome! If you'd like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that the code follows the project's style and conventions.
4. Test your changes thoroughly.
5. Submit a pull request with a clear description of your changes.

## Support

If you encounter any issues or have questions about the application, please feel free to [open an issue](https://github.com/yourusername/flask-weather-app/issues). We'll do our best to assist you.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.