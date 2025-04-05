# RAIT IT Results Database

## Project Overview
A Flask web application for analyzing and managing IT department exam results across different semesters.

## Features
- Data cleaning and preprocessing for Excel result files
- Analysis of student performance across semesters
- Web interface for result visualization

## Prerequisites
- Python 3.8+
- pip
- Virtual Environment

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/aryant-28/RAIT-IT-Results-DataBase.git
cd RAIT-IT-Results-DataBase
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python run.py
```

## Project Structure
- `app/`: Main Flask application
- `data/`: Excel result files
- `instance/`: SQLite database
- `analyze_data.py`: Data analysis script
- `run.py`: Application entry point

## Data Analysis
The project includes a script `analyze_data.py` for processing and analyzing result data from Excel files.

## Deployment
Recommended platforms:
- PythonAnywhere
- Render
- Heroku

## Contributing
1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
[Specify your license here]

## Contact
[Your contact information] 