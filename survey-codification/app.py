from flask import ( Flask, jsonify, render_template, request )
from werkzeug.utils import secure_filename
import parse
app = Flask(__name__)
from flask import send_file
import sys
import re
import os
from flask import abort

@app.route('/')
def upload():
   return render_template('upload.html')

@app.route('/show-metrics')
def show_metrics():
   return render_template('metrics.html')

@app.route('/show-questioninfo')
def show_questioninfo():
   return render_template('questionInfo.html')

@app.route('/return_template')
def return_file():
   data_url = os.path.dirname(__file__) + '/Demosurvey.docx'
   return send_file( data_url, attachment_filename='Demosurvey.docx')
	
@app.route('/preuploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      if not request.files.get('file', None):   
         abort(400, 'No file chosen')

      else:
         pattern = re.compile('[^a-zA-Z0-9_.]')
         string = re.sub(pattern, '', f.filename)
         f.save(secure_filename(string))
         val = (parse.parse_q(string))
         resp = jsonify(val)
      
   return resp
	
@app.route('/postuploader', methods = ['GET', 'POST'])
def upload_post():
   if request.method == 'POST':
      f = request.files['file']
      pattern = re.compile('[^a-zA-Z0-9_.]')
      string = re.sub(pattern, '', f.filename)
      f.save(secure_filename(string))
      val = (parse.parse_q(string))
      resp = jsonify(val)
   return resp

   
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
