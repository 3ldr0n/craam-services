from flask import Blueprint, Response, request, jsonify

from requests import get
from requests.exceptions import RequestException
from sunpy.timeseries import TimeSeries
from sunpy.time import TimeRange
from sunpy.net import Fido, attrs

from utils import get_correct_goes_index

goes_page = Blueprint("goes", __name__)


@goes_page.route("/", methods=["GET"])
def index():
    data = {"message": "GOES Data"}
    return jsonify(data)


@goes_page.route("/health", methods=["GET"])
def health():
    try:
        get("https://umbra.nascom.nasa.gov/goes/fits")
        data = {"status": "UP"}
    except RequestException:
        data = {"status": "DOWN"}
    return jsonify(data)


@goes_page.route("/get_data", methods=["GET"])
def goes_data():
    begin = request.args["begin"]
    end = request.args["end"]
    try:
        tr = TimeRange(begin, end)
    except ValueError:
        return jsonify({"message": "Date error"}), 400

    results = Fido.search(attrs.Time(tr), attrs.Instrument("XRS"))
    files = Fido.fetch(results)
    goes = TimeSeries(files)
    # Transforms XRSTimeSeries object to a Dataframe to ease manipulation.
    goes = goes.to_dataframe()

    begin, end = get_correct_goes_index(goes.index, begin, end)
    goes = goes[begin:end]
    # Transforms all the index to strings.
    goes.index = goes.index.map(lambda x: str(x))
    return Response(goes.to_json(), mimetype='application/json')
