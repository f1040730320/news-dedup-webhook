from flask import Flask, request, jsonify
import os
from fetch_sheet import fetch_existing_contents
from deduplicate import is_similar

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("✅ 收到資料：", data)  # debug 用
        existing_contents = fetch_existing_contents()

        # 其他處理...
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print("❌ 伺服器錯誤：", e)
        return jsonify({"error": str(e)}), 500
