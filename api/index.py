from flask import Flask, request, jsonify
import httpx
import json

app = Flask(__name__)

# Aapka bypass data
FINGERPRINT = "e8012f853d9cdca0a82d1e8f727f9b04"
USER_AGENT = "Mozilla/5.0 (Linux; Android 12; LAVA Blaze) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile"

@app.route('/')
def home():
    return jsonify({"status": "active", "message": "FindTube Proxy API is running"}), 200

@app.route('/api/search', methods=['GET'])
def search_proxy():
    # Query parameter 'q' se input lega
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing query parameter 'q'"}), 400

    url = "https://findtube.ai/api/search/youtube/knowledge"
    
    headers = {
        "host": "findtube.ai",
        "content-type": "application/json",
        "x-fingerprint": FINGERPRINT,
        "user-agent": USER_AGENT,
        "origin": "https://findtube.ai",
        "referer": "https://findtube.ai/",
        "accept": "*/*"
    }

    payload = {
        "q": query,
        "size": 50,
        "doc_filter": {}
    }

    try:
        
        with httpx.Client(http2=True, timeout=30.0) as client:
            resp = client.post(url, headers=headers, json=payload)
            

            return jsonify(resp.json()), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app.debug = True
