from flask import Flask, jsonify
from flask_cors import CORS   # <-- 新增這行

app = Flask(__name__)
CORS(app)  # <-- 新增這行，允許所有網域存取

@app.route("/data", methods=["GET"])
def get_data():
    data = [
        {"id": 1, "title": "標題 A", "body": "內容 A"},
        {"id": 2, "title": "標題 B", "body": "內容 B"},
        {"id": 3, "title": "標題 C", "body": "內容 C"}
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
