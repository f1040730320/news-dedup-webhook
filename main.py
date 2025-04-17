from flask import Flask, request, jsonify
import os
from fetch_sheet import fetch_existing_contents
from deduplicate import is_similar

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    existing_contents = fetch_existing_contents()

    filtered = []
    for article in data:
        content = article.get("content", "")
        if not is_similar(content, existing_contents):
            filtered.append(article)

    print(f"🧠 Received {len(data)} articles, {len(filtered)} are unique.")
    return jsonify(filtered)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
