from app import app
from flask import request, render_template, redirect, url_for
import os
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['pdf'])

#This route will be the splash page for the tool, it will have log in eventually. Right now it will just have header's and footers
@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/ingestion', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "success"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route("/viewer",methods=["GET","POST"])
def viewer():
    return render_template("viewer.html")

@app.route("/test_route",methods=["GET","POST"])
def testing():
    
    return "success"
