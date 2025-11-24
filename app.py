from flask import Flask, jsonify, send_file
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# ------------------------
# 主資料（你之後只改這裡即可）
# ------------------------
DATA = [
    {"id": 1, "title": "標題 A", "body": "內容 A"},
    {"id": 2, "title": "標題 B", "body": "內容 B"},
    {"id": 3, "title": "標題 C", "body": "內容 C"}
]

DATA_FILE = "data.json"

# ------------------------
# 自動同步資料到 data.json
# ------------------------
def sync_json():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(DATA, f, ensure_ascii=False, indent=2)

# ------------------------
# API: 回傳 JSON（給 DartPad、Flutter 用）
# ------------------------
@app.route("/data", methods=["GET"])
def get_data():
    sync_json()  # 自動同步
    return jsonify(DATA)

# ------------------------
# API: 提供下載 data.json
# ------------------------
@app.route("/file/data.json", methods=["GET"])
def download_json():
    sync_json()  # 自動同步
    return send_file(DATA_FILE, as_attachment=True)

# ------------------------
# 啟動 Flask
# ------------------------
if __name__ == "__main__":
    sync_json()  # 啟動時同步一次
    app.run(host="0.0.0.0", port=5000)
