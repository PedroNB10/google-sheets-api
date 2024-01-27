import pandas as pd
import gspread
import os
import math
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from .env file
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)


SPREAD_SHEET_ID = os.getenv("SPREAD_SHEET_ID")
WORKSHEET_NAME = os.getenv("WORKSHEET_NAME")
JSON_KEY_PATH = os.getenv("JSON_KEY_PATH").replace('\\', '/') # turn the string to a raw string


URL = f"https://docs.google.com/spreadsheets/d/{SPREAD_SHEET_ID}/gviz/tq?tqx=out:csv&sheet={WORKSHEET_NAME}"

# Set the environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = JSON_KEY_PATH



def get_column_data_from_sheets():
    # Read the CSV file (from Google Sheets)
    df = pd.read_csv(URL)
    return df




def update_google_sheets(spread_sheet_id, worksheet_name, data_frame):
    dictionary = data_frame.to_dict()

    total_of_students = len(dictionary['Aluno'])
    total_of_classes_in_semester = 0
    
    for key in dictionary:
        if 'aulas' in key:
            total_of_classes_in_semester = int(key.replace('Engenharia de Software Total de aulas no semestre: ', '').replace(' Matricula', ''))
            break
            
    # Authenticate using the signed key
    gc = gspread.service_account(
        filename=JSON_KEY_PATH)

    # Open the Google Sheets document
    sh = gc.open_by_key(spread_sheet_id)
    worksheet = sh.worksheet(worksheet_name)


    # verify if the dictionary is not empty
    if dictionary:
        
        situation_list = []
        grade_to_pass_list = []
        
        
        for i in range(total_of_students):
            missed_classes = dictionary['Faltas'][i]
            
            if missed_classes > total_of_classes_in_semester * 0.25 and total_of_classes_in_semester > 0:
                
                
                situation_list.append('Reprovado por Falta')
                grade_to_pass_list.append(0)
                
                print(f"Aluno: {dictionary['Aluno'][i]}")
                print(f"Faltas: {missed_classes}")
                print(f"Porcentagem de faltas: {missed_classes / total_of_classes_in_semester * 100}%")
                print(f"Situacao: Reprovado por Falta")
                print(f"------------------------------------")
                
                continue
            
            
            average = (dictionary['P1'][i] + dictionary['P2'][i] + dictionary['P3'][i]) / 3
            
            
            if average < 50:
                situation_list.append('Reprovado por Nota')
                grade_to_pass_list.append(0)  
            
            elif average >= 50 and average < 70:
                situation_list.append('Exame Final')
                grade_to_pass_list.append(math.ceil(100 - average))
   
            else:
                situation_list.append('Aprovado')
                grade_to_pass_list.append(0)
                
            print(f"Aluno: {dictionary['Aluno'][i]}")
            print(f"Faltas: {missed_classes}")
            print(f"Porcentagem de faltas: {missed_classes / total_of_classes_in_semester * 100}%")
            print(f"Nota final: {average}")
            print(f"Situacao: {situation_list[i]}")
            print(f"Nota para passar: {grade_to_pass_list[i]}")
            print(f"------------------------------------")
            
        # update the google sheets
        worksheet.update('G4:G27', [[situation] for situation in situation_list])
        worksheet.update('H4:H27', [[grade] for grade in grade_to_pass_list])




if __name__ == "__main__":

    data_frame = get_column_data_from_sheets()
    print(data_frame)
    update_google_sheets(SPREAD_SHEET_ID, WORKSHEET_NAME, data_frame)
    