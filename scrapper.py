import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# --- CONFIGURATION ---
BASE_URL = "http://117.239.28.178:8081/OLDRESULT/view_TR.asp"
START_ROLL = 1300001
TOTAL_STUDENTS = 5000
YEAR = "2018"
EXAM_TYPE = "SEC_MAIN"

def fetch_student_data(roll_no):
    """Fetches data for a single roll number using the provided keys."""
    # The exact payload you provided
    payload = {
        'cmb_year': YEAR,
        'cmb_exam': EXAM_TYPE,
        'txt_roll': str(roll_no),
        'b1': 'Submit'
    }

    try:
        response = requests.post(BASE_URL, data=payload, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table containing the marks
        table = soup.find('table')
        if not table:
            return None

        # Extract all text from the table to ensure we get all available data
        rows = table.find_all('tr')
        data_points = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            for col in cols:
                text = col.text.strip()
                if text: # Only add non-empty values
                    data_points.append(text)

        # Return as a string separated by pipes (to keep it SQL friendly)
        return " | ".join(data_points)

    except Exception as e:
        print(f"\n[Error] Roll No {roll_no}: {e}")
        return None

def main():
    # Using a dictionary to prevent duplicates. 
    # Key = Roll Number, Value = Data. This automatically overwrites duplicates.
    student_records = {}

    print(f"Starting data extraction for {TOTAL_STUDENTS} students...")

    for i in range(TOTAL_STUDENTS):
        current_roll = START_ROLL + i
        data = fetch_student_data(current_roll)
        
        if data:
            # Store in dictionary: if roll exists, it just updates (no duplicates)
            student_records[current_roll] = data
        
        # Progress tracker
        print(f"Processed: {i+1}/{TOTAL_STUDENTS} | Current Roll: {current_roll}", end="\r")
        time.sleep(0.3) # Small delay to be polite to the server

    # Convert dictionary to a list for Pandas
    final_data = [{"roll_no": k, "details": v} for k, v in student_records.items()]
    df = pd.DataFrame(final_data)

    # 1. Save as CSV (Best for SQL Import Wizards)
    df.to_csv("rbse_results.csv", index=False)
    
    # 2. Generate a raw .sql file with INSERT statements
    with open("insert_students.sql", "w", encoding="utf-8") as f:
        f.write("-- SQL Script to import RBSE Data\n")
        f.write("CREATE TABLE IF NOT EXISTS student_results (roll_no INT PRIMARY KEY, details TEXT);\n\n")
        for record in final_data:
            # Escape single quotes for SQL safety
            clean_details = record['details'].replace("'", "''")
            sql_line = f"INSERT INTO student_results (roll_no, details) VALUES ({record['roll_no']}, '{clean_details}') ON DUPLICATE KEY UPDATE details='{clean_details}';\n"
            f.write(sql_line)

    print(f"\n\nDone! Processed {len(student_records)} unique records.")
    print("Files created: 'rbse_results.csv' and 'insert_students.sql'")

if __name__ == "__main__":
    main()
               
