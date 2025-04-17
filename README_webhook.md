# 🧠 Deduplication Webhook for News Filtering

This lightweight Flask app is designed to receive news articles from n8n, compare them to existing content in your Google Sheet, and return only **non-duplicate** entries based on content similarity.

---

## 📁 Folder Structure

```
.
├── main.py                  # Flask app - webhook endpoint
├── deduplicate.py           # Cosine similarity filter
├── fetch_sheet.py           # Load existing content from Google Sheet
├── requirements.txt         # Dependencies
└── service_account.json     # Your Google API credentials (DO NOT SHARE)
```

---

## ⚙️ Environment Variables

You don't need any `.env` if you upload your `service_account.json` and use the default Sheet ID and worksheet name hardcoded in `fetch_sheet.py`.

---

## 🚀 How to Deploy to Railway

1. Create a new project on [Railway](https://railway.app)
2. Upload all the files above, including `service_account.json`
3. Railway will expose your Flask app at:

```
https://your-project-name.up.railway.app/webhook
```

---

## 📥 Sample POST from n8n

```json
[
  {
    "title": "Sample Headline",
    "content": "This is the body of the article...",
    "date": "2025-04-17",
    "link": "https://example.com",
    "source": "NYT"
  }
]
```

✅ The webhook will return only **non-duplicate** articles in the same format.
