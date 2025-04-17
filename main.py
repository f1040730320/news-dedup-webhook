from flask import Flask, request, jsonify
import os
from fetch_sheet import fetch_existing_contents
from deduplicate import is_similar

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        print("📥 headers:", dict(request.headers))  # ✅ 放進來
        print("📩 raw body:", request.data)          # ✅ 放進來

        data = request.get_json()
        print("✅ 收到資料：", data)

        # 處理邏輯...
        return jsonify({"status": "ok"}), 200

    except Exception as e:
        print("❌ 錯誤：", str(e))
        return jsonify({"error": str(e)}), 500
