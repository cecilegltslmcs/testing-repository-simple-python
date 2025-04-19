import time

from flask import Blueprint
from flask import jsonify

health_bp = Blueprint("health_bp", __name__)
start_time = time.time()


@health_bp.route("/healthz", methods=["GET"])
def healthz():
    uptime = round(time.time() - start_time, 2)
    return jsonify({"status": "OK", "uptime_seconds": uptime}), 200


@health_bp.route("/readyz", methods=["GET"])
def readyz():
    return jsonify({"status": "READY"}), 200
