def ensure_sheet_exists(svc, spreadsheet_id, sheet_name):
    """シートが存在しなければ作成し、ヘッダ行を初期化する"""
    meta = svc.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheets = [s['properties']['title'] for s in meta['sheets']]
    if sheet_name not in sheets:
        # シート追加
        requests = [{
            "addSheet": {
                "properties": {"title": sheet_name}
            }
        }]
        svc.spreadsheets().batchUpdate(
            spreadsheetId=spreadsheet_id,
            body={"requests": requests}
        ).execute()
        # ヘッダ行書き込み
        header = [["管理用ID","配信日","曲名","アーティスト","配信URL","配信内容","スタイル","備考","配信タイトル"]]
        svc.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=f"{sheet_name}!A1:I1",
            valueInputOption="USER_ENTERED",
            body={"values": header}
        ).execute()
