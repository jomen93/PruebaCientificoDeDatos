import json 
import os
from flask import (Flask, jsonify, request, render_template, flash, redirect)
from flask_cors import CORS
import pickle
import sklearn
import numpy as np

app = Flask(__name__, template_folder="templates")

model = pickle.load(open("metamodelo.pkl", "rb"))
 
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
def predict():	
	if request.method == "POST":
		data = request.get_json(force=True)
		int_features = data["input"]
	if request.method == "GET":
		int_features = [x for x in request.form.values()][0]
		b = "'input'[]{}:"
		for char in b:
			int_features = int_features.replace(char,"")

		int_features = np.array(int_features.split(","), dtype=np.float64)

	final_features = np.array(int_features)
	prediction = model.predict(final_features)[0]

	if prediction == 0:
		output = "(Negative)"
	if prediction == 1:
		output = "(Neutral)"
	if prediction == 2:
		output = "(Negative)"


	return render_template("index.html", prediction_text="Estado de animo es {}".format(output))
	

if __name__ == "main":
	app.run(debug=True)