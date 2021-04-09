import json 
import os
from flask import (Flask, jsonify, request, render_template, flash, redirect)
from flask_cors import CORS
import pickle
import sklearn
from forms import RegistrationForm
import numpy as np



app = Flask(__name__, template_folder="templates")
app.config["SECRET_KEY"] = "156e8e546edb302d205577f5672953cb"

model = pickle.load(open("metamodelo.pkl", "rb"))

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
	# try:
	int_features = [x for x in request.form.values()]
	# int_features = request.get_json(force=True)
	# except:
		# return "Hola"
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)

	output = prediction

	return render_template("index.html", prediction_text="Estado de animo es {}".format(output))

# @app.route('/register', methods=["GET", "POST"])
# def register():
# 	form = RegistrationForm()
# 	if form.validate_on_submit():
# 		flash('Datos recibidos de'.format(form.username.data), "success")
# 		return redirect(url_for)
# 	return render_template("index.html", title="Predicción", form=form)


# def test():
# 	data = request.get_json(force=True)
# 	name = data["name"]
# 	response = {
# 		"greeting": "Hola "+"name"+"!"
# 	}
# 	return jsonfy(response)
# def predict():
# 	petition = request.get_json(force=True)
# 	prediction = model.predict(np.array(petition["input"]))
# 	prediction_dict = {
# 		'model': 'Metamodelo',
# 		'output': prediction,
# 	}
# 	return jsonify(price_dict)


# CORS(app)
# @app.route("/", methods=["GET"])
# def return_prediction():
# 	prediction = FeelPredictor.predict(request.get_json())
# 	prediction_dict={
# 		"output":prediction,
# 	}
# 	return jsonify(prediction_dict)


if __name__ == "main":
	app.run(debug=True)