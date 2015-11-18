from flask import Flask

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/home/eric/Documents/whitehouse/VAUSDS/personal_projects/pdf_to_web/pdfs"


from app import views, models
