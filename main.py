import os
import argparse
from sheets_utils import ensure_sheet_exists
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# 環境変数 or Secrets から取得
SHEET_ID = os.environ.get("SHEET_ID")

def get_sheets_service():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_authorized_user_file("token.json", SCOPES) \
        if os.path.exists("token.json") else None
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
        with open("token.json", "w") as f:
            f.write(creds.to_json())
    return build("sheets", "v4", credentials=creds)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_id", required=True)
    parser.add_argument("--sheet_name", required=True)
    args = parser.parse_args()

    svc = get_sheets_service()
    ensure_sheet_exists(svc, SHEET_ID, args.sheet_name)

    # ここに YouTube API 呼び出し → コメント／タイトル解析 → append_to_sheet を実装

if __name__ == "__main__":
    main()
