import gspread
from google.oauth2.service_account import Credentials

def fetch_existing_contents(sheet_name='News_Datatable'):
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds = Credentials.from_service_account_file('service_account.json', scopes=scopes)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1
    records = sheet.get_all_records()
    return [row['Content'] for row in records if 'Content' in row]
