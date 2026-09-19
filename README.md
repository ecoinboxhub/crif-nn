# CRIF-NN — Climate-Resilient Infrastructure Framework for Northern Nigeria

AI-powered road condition monitoring and policy recommendation system for
climate-resilient road infrastructure in Northern Nigeria.

## Applications

| App     | Stack                        | Live URL                                   |
| ------- | ---------------------------- | ------------------------------------------ |
| Backend | FastAPI (Python) on Render   | https://crif-nn-backend.onrender.com       |
| Frontend| React (CDN) static on Vercel | https://frontend-pi-seven-30.vercel.app    |
| Mobile  | Static HTML on GitHub Pages  | https://ecoinboxhub.github.io/crif-nn/     |
| APK     | Android WebView app (signed) | https://ecoinboxhub.github.io/crif-nn/CRIF-NN.apk |
| Download| Landing page                 | https://ecoinboxhub.github.io/crif-nn/download.html |

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

## Android APK

The signed release APK wraps the live mobile web app in an offline-capable WebView
system. It is rebuilt manually and committed to `apk/` so GitHub Pages serves a
permanent, stable download URL.

-  **Download:** `https://ecoinboxhub.github.io/crif-nn/CRIF-NN.apk`
-  **Landing page:** `https://ecoinboxhub.github.io/crif-nn/download.html`
-  **Package:** `com.crifnn.mobile` · version `1.0.0` · min Android 7.0 (API 24)
-  **SHA-256:** `AD98D8E1FD2BAFAFE603951C57EC4FFA3373B40FE34161EFCFF1FC39842605AB`

Sources live in `mobile-apk/` supported by the Gradle wrapper. Rebuild:

```bash
cd mobile-apk
./gradlew.bat :app:assembleRelease   # requires local.properties + keystore.properties (gitignored)
```

## Repository layout

```
backend/   FastAPI REST API (deployed on Render)
frontend/  React dashboard — static site (deployed on Vercel)
mobile/    Mobile-first web app (published on GitHub Pages)
mobile-apk/ Android WebView app source (Gradle) — produces apk/
apk/       Signed release APK artifacts (served by GitHub Pages)
download.html  APK landing page (published on GitHub Pages)
render.yaml Render Blueprint (authoritative config)
```