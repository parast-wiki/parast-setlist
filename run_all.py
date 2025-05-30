import json
import os
import subprocess
from googleapiclient.discovery import build

# 環境変数から YouTube API キーを取得
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# channels.json 読み込み
with open("channels.json", encoding="utf-8") as f:
    channels = json.load(f)

def get_target_videos(channel_id, last_published_at, is_initial):
    # ここに search.list → publishedAfter 判定ロジックを実装
    return []

def main():
    # Config シートから last_published_at を取得（未実装サンプル）
    last_published_at = None
    is_initial = last_published_at is None

    for channel_id, sheet_name in channels.items():
        video_ids = get_target_videos(channel_id, last_published_at, is_initial)
        for vid in video_ids:
            subprocess.run([
                "python", "main.py",
                "--video_id", vid,
                "--sheet_name", sheet_name
            ], check=True)

    # ここで last_published_at を更新するロジックを追加

if __name__ == "__main__":
    main()
