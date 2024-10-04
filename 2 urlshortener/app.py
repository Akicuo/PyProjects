from flask import Flask, request, render_template, jsonify, redirect
import requests as reqs
import random

app = Flask(__name__)


shortened_links = []

def FindId(id: int):
    global shortened_links
    for i in range(len(shortened_links)):
        if shortened_links[i][0] == id:
            return shortened_links[i][1]
            # returns site if the id is found
    return "/notfound" # returns notfound route if not found

def works(url: str) -> dict:
    if 2 in reqs.get(url).status_code: # 2xxs – Success! The request was successfully completed and the server gave the browser the expected response.
        return True
    else:
        return False
    

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sl/<id>")
def index():
    return render_template(FindId(id), code=200)

@app.route("/api/shorten?url=<url>")
def  shorten_url(url):
    global shortened_links
    if works(url): # test response of the given site 
        id = random.randint(11111111,  99999999)
        shortened_links.append([id, url])
        return jsonify({"positive": True, "id":  id})
    else:
        return jsonify({"positive": False})

if __name__ == "__name__":
    app.run(debug=True, port=2901)





