from flask import Flask, request, jsonify
import os  # 🧠 不可省略

app = Flask(__name__)

# ✅ 首頁路由，給人檢查用
@app.route("/", methods=["GET"])
def home():
    return "✅ Webhook is running."

# ✅ 處理 Webhook POST 請求
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("✅ 收到資料：", data)
        # 👉 這裡可以進行資料處理邏輯
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print("❌ 錯誤：", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
