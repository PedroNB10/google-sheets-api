# google_sheets_facade.py
import gspread

class GoogleSheetsFacade:
    def __init__(self, spread_sheet_id, worksheet_name, json_key_path):
        self.spread_sheet_id = spread_sheet_id
        self.worksheet_name = worksheet_name
        self.json_key_path = json_key_path

    def authenticate(self):
        return gspread.service_account(filename=self.json_key_path)

    def open_worksheet(self):
        gc = self.authenticate()
        sh = gc.open_by_key(self.spread_sheet_id)
        return sh.worksheet(self.worksheet_name)

    def update_sheets(self, worksheet, situations, grades):
        worksheet.update('G4:G27', [[situation] for situation in situations])
        worksheet.update('H4:H27', [[grade] for grade in grades])
