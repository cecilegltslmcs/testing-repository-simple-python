# -*- coding: utf-8 -*-
import pytest
from flask import Flask

from .src.routes.health import health_bp


@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    return app


@pytest.fixture
def client(app):
    return app.test_client()


def test_healthz_status_code(client):
    response = client.get("/healthz")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "OK"
    assert "uptime_seconds" in data
    assert isinstance(data["uptime_seconds"], float)


def test_readyz_status_code(client):
    response = client.get("/readyz")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "READY"
