from rstnpy import RSTN
from rstnpy.exceptions import (
    FileNotFoundOnServerError, InvalidDateError,
    FileNotFoundError
)

from flask import Blueprint, Response, request, jsonify

rstn_page = Blueprint("rstn", __name__)


@rstn_page.route("/", methods=["GET"])
def index():
    data = {"message": "RSTN Data"}
    return jsonify(data)


@rstn_page.route(
    "/get_data/",
    methods=["GET"]
)
def rstn_data():
    year = request.args["year"]
    month = request.args["month"]
    day = request.args["day"]
    station = request.args["station"]

    path = "data"
    rstn = RSTN(year, month, day, path, station)

    try:
        filename = rstn.downloader.download_file()
    except FileNotFoundOnServerError:
        msg = {"message": "File does not exist"}
        return jsonify(msg), 400
    except InvalidDateError:
        msg = {"message": "Impossible date"}
        return jsonify(msg), 400

    filename = rstn.decompress_file(filename)
    try:
        rstn_data = rstn.create_dataframe()
        rstn_data.index = rstn_data.index.map(lambda x: str(x))
        # Remove rows with the same index.
        rstn_data = rstn_data[~rstn_data.index.duplicated(keep="first")]
        return Response(rstn_data.to_json(), mimetype="application/json")
    except FileNotFoundError:
        error = {"message": "Internal error"}
        return jsonify(error), 500
