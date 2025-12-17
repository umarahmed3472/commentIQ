from dotenv import load_dotenv
load_dotenv()

import os
import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)

# Allow requests from a local file (file://) OR localhost pages
CORS(app, resources={r"/*": {"origins": "*"}})

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found. Check your .env file location/name.")

client = OpenAI(api_key=api_key)

@app.get("/health")
def health():
    return jsonify({"ok": True})

@app.post("/summarize")
def summarize():
    try:
        data = request.get_json(force=True) or {}
        comments = data.get("comments", [])

        comments = [c.strip() for c in comments if isinstance(c, str) and c.strip()]
        if not comments:
            return jsonify({"summary": "No comments to summarize."})

        joined = "\n".join(f"- {c}" for c in comments)[:20000]

        prompt = (
            "You are a Business Analyst with 15 years of experience in Financial technology. Summarize these comments. Please do not include the # symbols in the output. Return:\n"
            "1) Overall sentiment (1 short line)\n"
            "2) 3–6 bullet key takeaways\n"
            "3) Top themes (max 5)\n"
            "4) Action items/suggestions (max 5)\n\n"
            f"Comments:\n{joined}"
        )

        # Model note: if gpt-4.1-mini errors for your account, switch to "gpt-4o-mini"
        resp = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
        )

        return jsonify({"summary": resp.output_text.strip()})

    except Exception as e:
        # Print full traceback in your terminal AND return it to the browser for debugging
        tb = traceback.format_exc()
        print(tb)
        return jsonify({"error": str(e), "traceback": tb}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
