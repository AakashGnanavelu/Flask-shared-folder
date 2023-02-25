
from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from flask import jsonify
from werkzeug.utils import secure_filename
import os
import time

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "folder/"

@app.route("/data_json")
def data_json():
    files = []

    filenames = os.listdir(app.config["UPLOAD_FOLDER"])
    for y in range(0, len(filenames)):
        files.append(
            {
                "file_id": y,
                "file_name": filenames[y],
                "file_cdate": time.ctime(os.path.getctime(os.path.join(app.config["UPLOAD_FOLDER"], filenames[y]))),
                "file_mdate": os.path.splitext(filenames[y])[1],
                "file_size": os.path.getsize(os.path.join(app.config["UPLOAD_FOLDER"], filenames[y]))
            }
        )
    return jsonify(files)

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(app.config['UPLOAD_FOLDER'] + filename)
    files = data_json()
    return render_template('content.html', files = files.json)

@app.route("/folder/<filename>")
def download_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)

