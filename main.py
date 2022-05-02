import os
import numpy as np
import pandas as pd
from flask import Flask
import requests
from flask import json
from werkzeug.exceptions import HTTPException
import logging # <-- added
import numpy as np
import pandas as pd

from sklearn.preprocessing import FunctionTransformer
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import re
import pickle
import pandas as pd


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
        urls = [ 'https://drive--google.com/luke.johnson', 'https://efax.hosting.com.mailru382.co/efaxdelivery/2017Dk4h325RE3', 'https://drive.google.com.download-photo.sytez.net/AONh1e0hVP', 'https://www.dropbox.com/buy', 'westmountdayschool.org', 'https://myaccount.google.com-securitysettingpage.ml-security.org/signonoptions/', 'https://google.com/amp/tinyurl.com/y7u8ewlr', 'www.tripit.com/uhp/userAgreement' ]
        x = []
        for url in urls:
            y= re.split("//", url, 1)[-1]+"/"
            x.append(y )
        print(x)
        with open('phish-model-1649995335.cloudpickle', 'rb') as f:
            clf_loaded = pickle.load(f)
        test_data_sample = pd.DataFrame (x, columns = ['url_name'])

        # Get predictions for the uploaded data
        clf_loaded.predict(test_data_sample)
            
        response_object['prediction'] = clf_loaded.predict(test_data_sample)
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
