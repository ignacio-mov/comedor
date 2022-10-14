from flask import Flask

from comedor.config import LOG_LEVEL

app = Flask(__name__)

from comedor import main

app.logger.setLevel(LOG_LEVEL)