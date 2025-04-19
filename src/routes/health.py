# -*- coding: utf-8 -*-
import time

from flask import Blueprint
from flask import jsonify
from flask import Response

health_bp = Blueprint("health_bp", __name__)
start_time = time.time()


@health_bp.route("/healthz", methods=["GET"])
def healthz() -> tuple[Response, int]:
    """Return the health status of the API.

    This endpoint provides informations about whether the API is
    functioning properly and how long it has been running.

    Returns:
        tuple: A Flask response object containing JSON with:
            - status: Current health status ("OK" if healthy)
            - uptime_seconds: Time in seconds since the API started
        and HTTP status code 200
    """
    uptime = round(time.time() - start_time, 2)
    return jsonify({"status": "OK", "uptime_seconds": uptime}), 200


@health_bp.route("/readyz", methods=["GET"])
def readyz() -> tuple[Response, int]:
    """Returns the readiness status of the API.

    This endpoint indicates whether the API is ready to accept requests,
    including having all required dependencies and resources available.

    Returns:
        tuple: A Flask response object containing JSON with:
            - status: Readiness status ("READY" if all systems are available)
        and HTTP status code 200
    """
    return jsonify({"status": "READY"}), 200
