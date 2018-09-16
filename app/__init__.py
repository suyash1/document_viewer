from flask import Flask, request, redirect, url_for, flash, Response
from werkzeug.utils import secure_filename
from config import app_config
import os
from .gdrive_util import GoogleDriveUtil

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])

    googleDrieUtil = GoogleDriveUtil()

    def allowed_file(filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config.get('ALLOWED_EXTENSIONS')

    def upload_to_drive(file_name):
        return

    @app.route('/')
    def hello():
        print(app.config)
        return 'hello world'

    @app.route('/upload/', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit a empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                googleDrieUtil.upload_file(filename)
                return Response(response='Successfully uploaded file to google drive', status=302)
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <p><input type=file name=file>
            <input type=submit value=Upload>
        </form>
        '''

    return app

