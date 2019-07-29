from requests import get
from requests.exceptions import RequestException
from rstnpy import RSTN
from rstnpy.exceptions import (
    FileNotFoundOnServerError, InvalidDateError
)

from flask import Blueprint, Response, jsonify

rstn_page = Blueprint("rstn", __name__)


@rstn_page.route("/", methods=["GET"])
def index():
    data = {"message": "RSTN Data"}
    return jsonify(data)


@rstn_page.route("/health", methods=["GET"])
def health():
    try:
        get("https://www.ngdc.noaa.gov/stp/space-weather/solar-data")
        data = {"status": "UP"}
    except RequestException:
        data = {"status": "DOWN"}
    return jsonify(data)


@rstn_page.route(
    "/get_data/<year>/<month>/<day>/<station>",
    methods=["GET"]
)
def rstn_data(year, month, day, station):
    path = "data"
    rstn = RSTN(year, month, day, path, station)

    try:
        filename = rstn.downloader.download_file()
    except FileNotFoundOnServerError:
        data = {"message": "File does not exist"}
        return jsonify(data), 400
    except InvalidDateError:
        data = {"message": "Impossible date"}
        return jsonify(data), 400

    filename = rstn.decompress_file(filename)
    try:
        rstn_data = rstn.create_dataframe()
        rstn_data.index = rstn_data.index.map(lambda x: str(x))
        # Remove rows with the same index.
        rstn_data = rstn_data[~rstn_data.index.duplicated(keep="first")]
        return Response(rstn_data.to_json(), mimetype="application/json")
    except FileNotFoundError:
        data = {"message": "Internal error"}
        return jsonify(data), 500
