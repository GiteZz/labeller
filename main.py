from flask import Flask, jsonify
import os
import json
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app = Flask(__name__)


@app.route('/category/<category>', methods=['GET'])
@cross_origin()
def get_category(category):
    file = os.path.join('./categories', category + '.json')
    if os.path.exists(file):
        with open(file, 'r') as f:
            return jsonify(json.load(f))
    else:
        jsonify({'error': 'category not found'})