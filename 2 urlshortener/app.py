from flask import Flask, request, render_template, jsonify, redirect, url_for
import requests as reqs
import random

app = Flask(__name__)

shortened_links = []

def find_id(id: int):
    global shortened_links
    for link in shortened_links:
        if link[0] == id:
            return link[1]
    return None

def works(url: str) -> bool:
    try:
        response = reqs.get(url, timeout=5)
        return response.status_code // 100 == 2  # Check if it's a 2xx response since those are usualy successful ones
    except reqs.RequestException:
        return False

@app.route("/")
def index():
    return render_template("index.html") # minimalistic page with  input field and submit button


@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    url = request.json.get("url")
    if works(url):
        id = random.randint(11111111, 99999999)
        shortened_links.append([id, url])
        return jsonify({"success": True, "id": id})
    else:
        return jsonify({"success": False, "message": "Invalid URL"}), 400

@app.route("/sl/<int:id>")
def redirect_shortened(id):
    url = find_id(id)
    if url:
        return redirect(url)
    else:
        return redirect(url_for('notfound'))

@app.route("/notfound")
def notfound():
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True, port=2901)
