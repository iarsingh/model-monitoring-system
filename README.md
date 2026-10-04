# Model Monitoring System

Level: 11 — ML Engineering

Skills: Python, live vs train mean

Score abs(live_mean - train_mean). At or above 2 is drift-watch.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
