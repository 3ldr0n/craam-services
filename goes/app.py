from flask import Flask

from goes_service import goes_page

app = Flask(__name__)

app.register_blueprint(goes_page, url_prefix="/goes")
