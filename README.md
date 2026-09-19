# CRIF-NN — Climate-Resilient Infrastructure Framework for Northern Nigeria

AI-powered road condition monitoring and policy recommendation system for
climate-resilient road infrastructure in Northern Nigeria.

## Applications

| App     | Stack                        | Live URL                                        |
| ------- | ---------------------------- | ----------------------------------------------- |
| Backend | FastAPI (Python) on Render   | https://crif-nn-backend.onrender.com            |
| Frontend| React (CDN) static on Vercel | (adding after Vercel deploy)                    |
| Mobile  | Static HTML on GitHub Pages  | (adding after Pages publish)                    |

## Backend API

- `GET  /health`               – status + model version (objectives 5/5 aligned)
- `POST /predict`              – single road condition assessment
- `POST /predict/bulk`         – batch assessment of multiple road segments
- `POST /analyze/image`        – pavement distress analysis from an image
- `GET  /climate/risk/{lat}/{lon}` – climate risk assessment per location
- `GET  /policy/national`      – national policy & standards references

Example single prediction:

```bash
curl -X POST https://crif-nn-backend.onrender.com/predict \
  -H "Content-Type: application/json" \
  -d '{"latitude":9.0579,"longitude":7.4951,"temperature":32,"rainfall_mm":25,"traffic_volume":5000}'
```

## Local run

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8001
```

Then open `frontend/index.html` or `mobile/index.html`.

## Repository layout

```
backend/   FastAPI REST API (deployed on Render)
frontend/  React dashboard — static site (deployed on Vercel)
mobile/    Mobile-first web app (published on GitHub Pages)
render.yaml Render Blueprint (authoritative config)
```