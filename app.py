# Flask API creation

import pickle

from flask import Flask, request ,jsonify
# import logisticmodel

# unpickling the model

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def start():
    return "hello world"


@app.route('/predict', methods=['POST'])
def predict():
    url = request.form.get('url')
    res = model.predict([url])[0]
    return jsonify({'result':str(res)})


if __name__ == '__main__':
    app.run(debug=True)
