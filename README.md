# Car Data Analysis Project

This project analyzes a used car dataset and creates visualizations and a dashboard for data exploration.

## Project Structure

- `car_dataset.csv` - The main dataset containing used car information
- `data_analysis.py` - Script to analyze data and generate visualizations
- `dashboard.py` - Dash application to display an interactive dashboard
- `outputs/` - Directory containing generated files:
  - `metadata.json` - Dataset metadata
  - `data_extract.csv` - Summary statistics of the dataset
  - `data_sample.csv` - Sample of the first 50 records
  - Visualization files (PNG and HTML formats)
- `requirements.txt` - List of Python dependencies

## Dataset Information

This dataset contains information about used cars including:
- Year of manufacture
- Car model
- Price
- Mileage
- Color
- Transmission type

The dataset was sourced from GitHub (Machine Learning with R datasets).

## Running the Analysis

1. Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

2. Run the data analysis script:
   ```
   python data_analysis.py
   ```
   This will generate metadata and visualizations in the `outputs` directory.

3. Run the dashboard:
   ```
   python dashboard.py
   ```
   This will start a local web server at http://127.0.0.1:8050/

## Visualizations

1. **Price Distribution by Year** - Shows how car prices vary by manufacturing year
2. **Price vs Mileage by Transmission Type** - Explores the relationship between price and mileage
3. **Car Color Distribution** - Shows the distribution of car colors in the dataset
4. **Top 10 Car Models** - Displays the most common car models in the dataset

## Publishing to Netlify

To deploy this dashboard to Netlify:

1. Create a `netlify.toml` file for configuration
2. Push the repository to GitHub
3. Connect Netlify to your GitHub repository
4. Set up the build command and publish directory

## Created for

Data Analysis Capstone Project, 2025
