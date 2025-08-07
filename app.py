import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# 從環境變數讀取 API Token（不要把密鑰寫死在程式）
API_TOKEN = os.getenv("API_TOKEN", "")

@app.route("/ping")
def ping():
    return "pong"

def require_token():
    """最簡單的 Token 檢查：Authorization: Bearer <TOKEN>"""
    auth = request.headers.get("Authorization", "")
    expected = f"Bearer {API_TOKEN}" if API_TOKEN else None
    if not expected or auth != expected:
        abort(401)

@app.route("/users")
def get_users():
    require_token()
    users = [
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "user"},
        {"id": 3, "name": "Charlie", "role": "moderator"}
    ]
    return jsonify(users)

if __name__ == "__main__":
    # 本地開發：export API_TOKEN=yourtoken 後再執行
    app.run(host="0.0.0.0", port=5000)
