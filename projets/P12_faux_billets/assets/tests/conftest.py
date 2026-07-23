from pathlib import Path

import httpx
import joblib
import pytest

from api.main import app


@pytest.fixture
async def client():
	transport = httpx.ASGITransport(app=app)
	async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
		yield client


@pytest.fixture
def model():
	candidates = [
		Path("src/model_oncfm.joblib"),
		Path("data/processed/model_oncfm.joblib"),
		Path("model_oncfm.joblib"),
	]
	for path in candidates:
		if path.exists():
			return joblib.load(path)
	pytest.skip("Aucun fichier modele .joblib trouve pour la fixture model")
