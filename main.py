import pandas as pd
import os


SHEET_NAME = "engenharia_de_software"
SPREAD_SHEET_ID = "1TZwVaYCUX_JtLQWNzr-PXib2xQZKzltdCejzr8io4k0"
WORKSHEET_NAME = "engenharia_de_software"

URL = f"https://docs.google.com/spreadsheets/d/{SPREAD_SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# Set the path to your service account JSON file
json_keyfile_path = r'C:\Users\pedro\AppData\gspread\service_account.json'


# Set the environment variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json_keyfile_path



def get_column_data_from_sheets():
    # Read the CSV file (from Google Sheets)
    df = pd.read_csv(URL)
    return df


if __name__ == "__main__":
    data_frame = get_column_data_from_sheets()

