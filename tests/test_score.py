from fastapi.testclient import TestClient
from monmodel.main import app

client = TestClient(app)


def test_high_and_low():
    assert client.post("/score", json={'delta': 3.0}).json()["label"]
    high = client.post("/score", json={'delta': 3.0}).json()
    low = client.post("/score", json={'delta': 0.2}).json()
    assert high["label"] != low["label"]
    assert high["score"] > low["score"]


def test_missing_is_refused():
    body = dict({'delta': 3.0})
    body.pop("delta")
    assert client.post("/score", json=body).status_code == 422
