from flask import Flask

from rstn_service import rstn_page

app = Flask(__name__)

app.register_blueprint(rstn_page, url_prefix="/RSTN")
