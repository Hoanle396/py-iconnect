from flask import Flask
from flask_compress import Compress
from flask_cors import CORS

app = Flask(__name__)
Compress(app)
CORS(app)
