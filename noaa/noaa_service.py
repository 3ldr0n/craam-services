from noaareport import NoaaReport, NoEventReports

from flask import Blueprint, Response, request, jsonify

from utils import check_date

noaa_page = Blueprint("noaa_report", __name__)


@noaa_page.route("/", methods=["GET"])
def index():
    data = {"message": "NOAA solar reports"}
    return jsonify(data)


@noaa_page.route("/get_data", methods=["GET"])
def get_data():
    day = request.args["day"]
    month = request.args["month"]
    year = request.args["year"]

    if not check_date(year, month, day):
        data = {"message": "Impossible date"}
        return jsonify(data), 400

    path = "reports/" + year + "_events/"
    noaa = NoaaReport(year, month, day, path)
    try:
        noaa.get_dataframe()
        return Response(noaa.df.to_json(), mimetype="application/json")
    except NoEventReports:
        return jsonify({"message": "No event reports."}), 500
    except FileNotFoundError:
        return jsonify({"message": "File not found."}), 500
