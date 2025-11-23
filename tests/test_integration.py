import pytest
import requests
from multiprocessing import Process
import time
from app.main import app

@pytest.mark.integration
def test_http_root():
    # Run the Flask app in a separate process for a quick smoke test
    proc = Process(target=app.run, kwargs={'port':5001})
    proc.start()
    time.sleep(1.0)
    try:
        r = requests.get('http://127.0.0.1:5001/')
        assert r.status_code == 200
        assert 'message' in r.json()
    finally:
        proc.terminate()
        proc.join()
