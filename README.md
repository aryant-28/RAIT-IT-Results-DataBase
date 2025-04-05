# IT Result Project

A Flask web application for analyzing and visualizing IT department exam results for semester 4 and 5.

## Overview

This project processes and analyzes student result data from Excel files, providing insights into performance metrics such as SGPA, CGPA, and result distributions. The application allows users to:

- View semester-wise performance statistics
- Analyze individual student results
- Compare performance across semesters

## Technologies Used

- **Backend**: Python, Flask
- **Data Processing**: Pandas
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript

## Project Structure

- **app/**: Flask application files
  - **static/**: CSS, JavaScript, and image files
  - **templates/**: HTML templates
  - **routes.py**: Application routes
- **data/**: Excel data files containing semester results
- **analyze_data.py**: Script for cleaning and analyzing result data
- **run.py**: Application entry point

## Setup and Installation

1. Clone the repository
```
git clone <repository-url>
cd IT-Result-Project
```

2. Create and activate a virtual environment
```
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. Install dependencies
```
pip install -r requirements.txt
```

4. Run the application
```
python run.py
```

5. Access the application at http://localhost:5000

## Features

- Data cleaning and preprocessing
- Statistical analysis of results
- Web interface for easy data exploration
- Performance comparison across semesters 