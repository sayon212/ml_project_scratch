from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
import sys

app = Flask(__name__)

logging.info("Testing Logger")

@app.route("/" , methods = ['GET' , 'POST'])
def index():
    try:
        raise Exception("We are testing Exception...")
    except Exception as e:
        housing_exception = HousingException(e,sys)
        logging.info(housing_exception.error_message)
    return "CI CD Pipeline Created for ML Project"

if __name__ == "__main__":
    app.run(debug=True)