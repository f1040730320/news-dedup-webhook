import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# 設定範圍與授權
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds_path = "service_account.json"
sheet_id = "1l4jEuJMZfD5E_ndCu9ILYaucE6zh872VARQNxZPEQ9o"
worksheet_name = "News_Datatable"

def fetch_existing_contents():
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id)
    worksheet = sheet.worksheet(worksheet_name)
    
    # 讀取整欄 C（Content），跳過標題列
    contents = worksheet.col_values(3)[1:]
    return contents

# 🧪 測試用
if __name__ == "__main__":
    contents = fetch_existing_contents()
    print(f"✅ Fetched {len(contents)} existing articles from Google Sheets")
