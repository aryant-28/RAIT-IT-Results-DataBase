from flask import Blueprint, render_template, request, jsonify
import pandas as pd
import os

main = Blueprint('main', __name__)

def read_excel_data():
    try:
        df_sem4 = pd.read_excel('data/cleaned_sem4.xlsx')
        df_sem5 = pd.read_excel('data/cleaned_sem5.xlsx')
        
        # Calculate ranks for both dataframes
        df_sem4['Rank'] = df_sem4['CGPA'].rank(method='min', ascending=False)
        df_sem5['Rank'] = df_sem5['CGPA'].rank(method='min', ascending=False)
        
        return df_sem4, df_sem5
    except Exception as e:
        print(f"Error reading Excel files: {e}")
        return None, None

def calculate_results(roll_no=None, name=None):
    df_sem4, df_sem5 = read_excel_data()
    
    if df_sem4 is None or df_sem5 is None:
        return None

    # Filter data for the student
    if roll_no:
        # Clean the roll number input
        roll_no = str(roll_no).strip().upper()
        # Remove any newline characters from roll numbers in dataframe
        df_sem4['Roll_No'] = df_sem4['Roll_No'].str.replace(r'\n', '', regex=True)
        df_sem5['Roll_No'] = df_sem5['Roll_No'].str.replace(r'\n', '', regex=True)
        
        student_sem4 = df_sem4[df_sem4['Roll_No'].str.strip().str.upper() == roll_no]
        student_sem5 = df_sem5[df_sem5['Roll_No'].str.strip().str.upper() == roll_no]
    elif name:
        # Clean the name input
        name = name.strip().lower()
        student_sem4 = df_sem4[df_sem4['Name'].str.lower().str.contains(name)]
        student_sem5 = df_sem5[df_sem5['Name'].str.lower().str.contains(name)]
    else:
        return None

    if student_sem4.empty or student_sem5.empty:
        return None

    try:
        # Get student details
        student_name = student_sem4['Name'].iloc[0]
        student_roll = student_sem4['Roll_No'].iloc[0]
        student_gender = student_sem4['Gender'].iloc[0]

        # Calculate SGPA and CGPA
        sem4_sgpa = float(student_sem4['SGPA'].iloc[0])
        sem5_sgpa = float(student_sem5['SGPA'].iloc[0])
        sem4_cgpa = float(student_sem4['CGPA'].iloc[0])
        sem5_cgpa = float(student_sem5['CGPA'].iloc[0])

        sgpa_change = round(sem5_sgpa - sem4_sgpa, 2)
        cgpa_change = round(sem5_cgpa - sem4_cgpa, 2)

        # Get subject performance for Sem 4
        sem4_subjects = [col for col in df_sem4.columns if col.startswith(('ITC', 'ITL', 'ITS', 'ITM'))]
        subject_performance_sem4 = []
        for subject in sem4_subjects:
            score = student_sem4[subject].iloc[0]
            if pd.notna(score):  # Only add if score is not NaN
                subject_performance_sem4.append({
                    'subject': subject,
                    'score': float(score) if isinstance(score, (int, float)) else score
                })

        # Get rankings
        rank_sem4 = int(student_sem4['Rank'].iloc[0])
        rank_sem5 = int(student_sem5['Rank'].iloc[0])
        rank_change = rank_sem4 - rank_sem5  # Positive means improvement in rank
        total_students = len(df_sem4)

        return {
            'name': student_name,
            'roll_no': student_roll,
            'gender': student_gender,
            'sem4_sgpa': sem4_sgpa,
            'sem5_sgpa': sem5_sgpa,
            'sgpa_change': sgpa_change,
            'sem4_cgpa': sem4_cgpa,
            'sem5_cgpa': sem5_cgpa,
            'cgpa_change': cgpa_change,
            'rank_sem4': rank_sem4,
            'rank_sem5': rank_sem5,
            'rank_change': rank_change,
            'total_students': total_students,
            'subject_performance_sem4': subject_performance_sem4,
            'result_sem4': student_sem4['Result'].iloc[0],
            'result_sem5': student_sem5['Result'].iloc[0]
        }
    except Exception as e:
        print(f"Error calculating results: {e}")
        return None

@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@main.route('/search', methods=['POST'])
def search():
    roll_no = request.form.get('roll_no')
    name = request.form.get('name')
    
    if not roll_no and not name:
        return render_template('index.html', error="Please enter either Roll Number or Name")

    results = calculate_results(roll_no, name)
    
    if results is None:
        return render_template('index.html', error="Student not found or there was an error processing the results")
    
    return render_template('result.html', data=results) 