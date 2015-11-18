from app import app
from flask import request, render_template
import os

#This route will be the splash page for the tool, it will have log in eventually. Right now it will just have header's and footers
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/ingestion",methods=["GET","POST"])
def ingestion():
    if request.method == "POST":
        #File upload goes here
        #Also allow for folder ingestion
        return render_template("ingestion.html") # consider changing this
    else:
        return render_template("ingestion.html")

@app.route("/viewer",methods=["GET","POST"])
def viewer():
    return render_template("viewer.html")

@app.route("/test_route",methods=["GET","POST"])
def testing():
    
    return "success"
