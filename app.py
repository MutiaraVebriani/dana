import numpy as np
from flask import Flask, jsonify, request, render_template, redirect, url_for
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open("best_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html', link="", result="")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        link_input = request.form['link']
        link_data = [link_input]

        prediction = model.predict(link_data)
        print("Nilai prediksi:", prediction[0])  # Tambahkan pernyataan cetak
        result = prediction[0]
        print("Hasil prediksi:", prediction[0])  # Tambahkan pernyataan cetak

        return render_template('index.html', link=link_input, result=result)

@app.route('/reset')
def reset():
    return render_template('index.html')

@app.route('/dana')
def dana():
     return render_template('dana.html')

@app.route('/tips')
def tips():
     return render_template('tips.html')

@app.route('/pp')
def pp():
     return render_template('pp.html')


if __name__ == '__main__':
    app.run(debug=True)
