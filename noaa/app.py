from flask import Flask

from noaa_service import noaa_page

app = Flask(__name__)

app.register_blueprint(noaa_page, url_prefix="/noaa_report")
