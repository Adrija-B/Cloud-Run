import os
import numpy as np
import pandas as pd
from flask import Flask
import requests
from flask import json
from werkzeug.exceptions import HTTPException
import logging # <-- added

app = Flask(__name__)

@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.exception(e) # <-- added
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response



@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route('/predict', methods=[ 'POST'])
def predict():
    """
    "expects request.get_json to return a string that expects a valid url"
    """
    response_object = {'status': 'success'}
    if request.method == 'POST':
        url = request.get_json()
        length = len(url)
        prediction = model.predict_proba([[length]])
        print(prediction, file = sys.stderr)
        response_object['prediction'] = prediction.tolist()[0][1]
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
