# playwright-cloud-demo

## Description
Demo Playwright + pytest project running in GitHub Actions with video and trace recording.

## Run locally
```bash
pip install -r requirements.txt
playwright install
pytest -v
```

## GitHub Actions
Push to main branch to run tests in the cloud. Videos and traces will be available as downloadable artifacts.
