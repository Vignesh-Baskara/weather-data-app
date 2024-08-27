# Weather Forecast App

This project is a weather forecasting application built with Streamlit and Plotly. It allows users to view weather data (temperature and sky conditions) for a specified location and forecast period.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd your-repository
    ```
3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## How It Works
main.py: The main script that sets up the Streamlit interface. It includes a title, text input, slider, selectbox, and subheader to let users interact with the weather forecast data. It uses get_data from backend.py to fetch weather information and displays either temperature plots or sky condition images.
backend.py: Contains a function get_data that fetches weather data from the OpenWeatherMap API based on the user’s input. It returns a filtered list of forecast data.

## Features
Real-time weather forecasting
Visual representation of temperature trends using Plotly
Image-based display of sky conditions
Adjustable forecast period and location
## Project Structure
main.py: The main script that sets up the Streamlit interface and visualizes the weather data.
backend.py: Contains the get_data function for fetching weather data from the OpenWeatherMap API.
requirements.txt: List of Python packages required to run the project.
## Technologies Used
Python 3.10
Streamlit
Plotly
Requests for API interaction

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your changes. For major changes, open an issue first to discuss what you would like to change.

## Contact
For questions or suggestions, you can reach me at vigneshbaskar1407@gmail.com.
## Usage

To run the application, use the following command:
```bash
streamlit run main.py

