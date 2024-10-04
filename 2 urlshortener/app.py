from flask import Flask, request, render_template, jsonify, redirect, url_for
import requests as reqs
import random

app = Flask(__name__)

shortened_links = []

def find_id(id: int):
    global url
    global shortened_links
    for link in shortened_links:
        if link[0] == id:
            link[2] += 1
            return link[1]
        
    return None

def works(url: str) -> bool:
    try:
        response = reqs.get(url, timeout=5)
        return response.status_code // 100 == 2  # Check if it's a 2xx response since those are usualy successful ones
    except reqs.RequestException:
        return False

@app.route("/analytics")
def stats():
    return render_template("analytics.html") # minimalistic page with  input field and submit button

@app.route("/")
def index():
    return render_template("index.html") # minimalistic page with  input field and submit button

# backend api
@app.route("/api/total-shortens", methods=["GET"])
def totalsl():
    global shortened_links
    return jsonify({"total":  len(shortened_links)})

# backend api
@app.route("/api/most-recent-one", methods=["GET"])
def msrol():
    global shortened_links
    rev = shortened_links[-1]
    return jsonify({"id": rev[0], "url": rev[1]}) # by creation date newest

# backend api
@app.route("/api/top-clicked-on", methods=["GET"])
def topclickedsl():
    global shortened_links
    highest = {"id":  0, "count": 0}
    for listlink in shortened_links:
        if listlink[2]  > highest["count"]:
            highest["id"] = listlink[0]
            highest["count"] = listlink[2]


    return jsonify({"id":  highest["id"], "count":  highest["count"]})

    
@app.route("/api/shorten", methods=["POST"])
def shorten_url():
    url = request.json.get("url")
    if works(url):
        id = random.randint(11111111, 99999999)
        shortened_links.append([id, url, 0])
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
