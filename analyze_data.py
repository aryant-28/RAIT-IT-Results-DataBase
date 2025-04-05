import pandas as pd
import os

def clean_excel_data(df, semester):
    # Skip the header rows and reset index
    df = df.iloc[2:].reset_index(drop=True)
    
    # Define column names based on the actual structure
    if semester == 4:
        columns = {
            'Unnamed: 1': 'Roll_No',
            'Unnamed: 2': 'Name',
            'Unnamed: 3': 'Gender',
            'Unnamed: 4': 'ITC401',
            'Unnamed: 5': 'ITC402',
            'Unnamed: 6': 'ITC403',
            'Unnamed: 7': 'ITC404',
            'Unnamed: 8': 'ITC405',
            'Unnamed: 9': 'ITL401',
            'Unnamed: 10': 'ITL402',
            'Unnamed: 11': 'ITL403',
            'Unnamed: 12': 'ITL404',
            'Unnamed: 13': 'ITSL402',
            'Unnamed: 14': 'ITMP402',
            'Unnamed: 15': 'SGPA',
            'Unnamed: 16': 'CGPA',
            'Unnamed: 17': 'Result'
        }
    else:
        columns = {
            'Unnamed: 1': 'Roll_No',
            'Unnamed: 2': 'Name',
            'Unnamed: 3': 'Gender',
            'Unnamed: 4': 'ITC501',
            'Unnamed: 40': 'SGPA',
            'Unnamed: 41': 'CGPA',
            'Unnamed: 42': 'Result'
        }
    
    # Rename columns
    for old_col, new_col in columns.items():
        if old_col in df.columns:
            df[new_col] = df[old_col]
    
    # Select only the columns we need
    df = df[list(columns.values())]
    
    return df

def analyze_excel_files():
    try:
        # Read both Excel files
        df_sem4 = pd.read_excel('data/results_sem4.xlsx')
        df_sem5 = pd.read_excel('data/results_sem5.xlsx')

        # Clean the data
        df_sem4_clean = clean_excel_data(df_sem4, 4)
        df_sem5_clean = clean_excel_data(df_sem5, 5)

        print("\n=== Cleaned Data Analysis ===\n")
        
        # Semester 4 Analysis
        print("Semester 4 Analysis:")
        print("-" * 20)
        print(f"Total Students: {len(df_sem4_clean)}")
        print("\nColumns:", df_sem4_clean.columns.tolist())
        print("\nSample Data (First 3 rows):")
        print(df_sem4_clean.head(3))
        
        print("\nSemester 5 Analysis:")
        print("-" * 20)
        print(f"Total Students: {len(df_sem5_clean)}")
        print("\nColumns:", df_sem5_clean.columns.tolist())
        print("\nSample Data (First 3 rows):")
        print(df_sem5_clean.head(3))

        # Performance Statistics
        print("\nPerformance Statistics:")
        print("-" * 20)
        print("\nSGPA Statistics:")
        print(f"Sem 4 - Average SGPA: {pd.to_numeric(df_sem4_clean['SGPA'], errors='coerce').mean():.2f}")
        print(f"Sem 5 - Average SGPA: {pd.to_numeric(df_sem5_clean['SGPA'], errors='coerce').mean():.2f}")
        
        print("\nCGPA Statistics:")
        print(f"Sem 4 - Average CGPA: {pd.to_numeric(df_sem4_clean['CGPA'], errors='coerce').mean():.2f}")
        print(f"Sem 5 - Average CGPA: {pd.to_numeric(df_sem5_clean['CGPA'], errors='coerce').mean():.2f}")

        # Result Analysis
        print("\nResult Analysis:")
        print("-" * 20)
        print("\nSemester 4 Results Distribution:")
        print(df_sem4_clean['Result'].value_counts())
        print("\nSemester 5 Results Distribution:")
        print(df_sem5_clean['Result'].value_counts())

        # Save cleaned data
        df_sem4_clean.to_excel('data/cleaned_sem4.xlsx', index=False)
        df_sem5_clean.to_excel('data/cleaned_sem5.xlsx', index=False)
        print("\nCleaned data saved to 'cleaned_sem4.xlsx' and 'cleaned_sem5.xlsx'")

    except Exception as e:
        print(f"Error analyzing files: {str(e)}")

if __name__ == "__main__":
    analyze_excel_files() 