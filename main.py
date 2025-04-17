from flask import Flask, request, jsonify
import os  # 🛠️ 加上這一行

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        print("✅ 收到資料：", data)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        print("❌ 錯誤：", str(e))
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
