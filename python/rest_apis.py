import os
from werkzeug.utils import secure_filename
from flask import Flask, request, url_for, send_from_directory, redirect
from mtcnn.mtcnn import MTCNN
import cv2
import numpy as np

UPLOAD_FOLDER = '/home/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
	return '.' in filename and filename.rspilt('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def mtcnn_face(img: np.array) -> dict:
        detector = MTCNN()
        faces = detector.detect_faces(img)
        return faces

@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_for_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/upload', methods=['POST'])
def upload_files():
	if request.method == 'POST':
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']

		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

			# face_detection(filename)
			# Show image with detected face
			return redirect(url_for('uploaded_file', filename=filename))

