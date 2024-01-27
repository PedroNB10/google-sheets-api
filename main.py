# main.py
import pandas as pd
import os
from dotenv import load_dotenv
from pathlib import Path
from evaluation_strategy import AttendanceEvaluation, GradeEvaluation
from google_sheets_facade import GoogleSheetsFacade

# Load environment variables from .env file
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

SPREAD_SHEET_ID = os.getenv("SPREAD_SHEET_ID")
WORKSHEET_NAME = os.getenv("WORKSHEET_NAME")
JSON_KEY_PATH = os.getenv("JSON_KEY_PATH").replace('\\', '/')  # turn the string to a raw string

URL = f"https://docs.google.com/spreadsheets/d/{SPREAD_SHEET_ID}/gviz/tq?tqx=out:csv&sheet={WORKSHEET_NAME}"

# Set the environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = JSON_KEY_PATH


def get_column_data_from_sheets():
    # Read the CSV file (from Google Sheets)
    df = pd.read_csv(URL)
    return df


def update_google_sheets(spread_sheet_id, worksheet_name, data_frame, total_of_classes_in_semester):
    # Create an instance of Facade
    sheets_facade = GoogleSheetsFacade(spread_sheet_id, worksheet_name, JSON_KEY_PATH)

    # get the google spreadsheets
    worksheet = sheets_facade.open_worksheet()

    # Initialize the strategies
    attendance_strategy = AttendanceEvaluation()
    grade_strategy = GradeEvaluation()

    # Lists to store hte situation and the grades of each student
    situation_list = []
    grade_to_pass_list = []

    for i in range(len(data_frame['Aluno'])):
        missed_classes = data_frame['Faltas'][i]
        average = (data_frame['P1'][i] + data_frame['P2'][i] + data_frame['P3'][i]) / 3

        # Attendence Evaluation
        situation, grade = attendance_strategy.evaluate(missed_classes, total_of_classes_in_semester)
        if situation:
            situation_list.append(situation)
            grade_to_pass_list.append(grade)
            
            print(f"Aluno: {data_frame['Aluno'][i]}")
            print(f"Faltas: {missed_classes}")
            print(f"Porcentagem de faltas: {missed_classes / total_of_classes_in_semester * 100}%")
            print(f"Situacao: Reprovado por Falta")
            print(f"------------------------------------")
            continue
        
        

        # Grade Evaluation
        situation, grade = grade_strategy.evaluate(average)
        
        
        
        situation_list.append(situation)
        grade_to_pass_list.append(grade)
        
        print(f"Aluno: {data_frame['Aluno'][i]}")
        print(f"Faltas: {missed_classes}")
        print(f"Porcentagem de faltas: {missed_classes / total_of_classes_in_semester * 100}%")
        print(f"Nota final: {average}")
        print(f"Situacao: {situation_list[i]}")
        print(f"Nota para passar: {grade_to_pass_list[i]}")
        print(f"------------------------------------")

    # Update Google Sheets
    sheets_facade.update_sheets(worksheet, situation_list, grade_to_pass_list)


if __name__ == "__main__":
    data_frame = get_column_data_from_sheets()
    print("\n Antes da atualização:")
    print(data_frame)
    total_of_students = len(data_frame['Aluno'])
    total_of_classes_in_semester = 0

    for key in data_frame:
        if 'aulas' in key:
            total_of_classes_in_semester = int(
                key.replace('Engenharia de Software Total de aulas no semestre: ', '').replace(' Matricula', ''))
            break

    update_google_sheets(SPREAD_SHEET_ID, WORKSHEET_NAME, data_frame, total_of_classes_in_semester)

    data_frame = get_column_data_from_sheets()
    print("\n Depois da atualização:")
    print(data_frame)
