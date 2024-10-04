# CSV Analysis Django App
Requirements:
1. Django Setup:
Create a Django project and a Django app within the project.
Configure the project with a with which you are comfortable with.
2. File Upload Feature:
Implement a form that allows users to upload CSV files.
Store the uploaded files temporarily for processing.
3. Data Processing:
Use pandas to read the uploaded CSV file.
Perform basic data analysis tasks such as:
Displaying the first few rows of the data.
Calculating summary statistics (mean, median, standard deviation) for numerical
columns.
Identifying and handling missing values.
4. Data Visualization:
Generate basic plots using matplotlib or seaborn (integrated with pandas) such as:
Histograms for numerical columns.
Display the plots on the web page.
5. User Interface:
Use Django templates to create a simple and user-friendly interface.
Display the data analysis results and visualizations in a clear and organized manner

## Setup Instructions

1. Clone the repository
2. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
3. Run the development server:
    ```
    python manage.py runserver
    ```

## Features
- Upload CSV files
- Perform basic data analysis
- Visualize data using histograms
