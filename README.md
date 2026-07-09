# DormiCare API

This is the backend for DormiCare, a sleep-tracking app. Built with **FastAPI**

Alongside the standard app routes, it adds 2 additional ML features and an AI layer:
1. **Sleep-journal sentiment** - a scikit-learn classifier that scores a user's description of the night.
2. **Sleep-tip recommendations** - a semantic search that surfaces most relevant tips for a free-text query
3. **AI insights & chat** - sleep-activity scoring(OpenAI) and open chat (xAI, Grok), both through one OpenAI-compatible client.

## Endpoints

|
 Method
|
 Path
|
 Description
|
---
|
---
|
---
|
|
GET
|
`/health`
|
 Health Check
|
|
 GET
|
`/docs`
|
Interactive API docs (Swagger UI)
|
|
 POST
|
`/ml/sentiment`
|
 Score a sleep-journal entry (positive/negative + confidence) 
|
|
 POST 
|
`/ml/recommend`
|
 Rank sleep tips against a query 
|
|
 POST
|
`/ai/chat`
|
 Chat with Grok 
|
|
 GET 
|
`/api/sample`
|
 Multilingual greeting (connectivity check) 
|
|
 GET 
|
`/api/users/count`
|
 Total registered users 
|
|
 POST 
|
`/api/users/register`
|
 Increment the user count 
|
|
 POST
|
`/api/insights/activity`
|
 AI sleep-impact insight for an activity 
|

## Layout

```
dormicare-api/
├── app/
│   ├── main.py            # App factory + startup model training
│   ├── config.py          # Settings from environment
│   ├── schemas.py         # Pydantic request/response models
│   ├── ml/
│   │   ├── datasets.py     # Bundled training data
│   │   ├── sentiment.py    # TF-IDF + logistic-regression classifier
│   │   └── recommender.py  # TF-IDF + cosine-similarity search
│   ├── routers/            # One module per route group
│   └── services/
│       └── llm.py          # OpenAI-compatible chat client
├── scripts/start           # Launch helper
├── run.py                  # `uv run run.py` for local dev
└── pyproject.toml
```

## Running

Dependencies are managed with ['uv'](https://docs.astral.sh/uv/).

```bash
cd dormicare-api
cp .env.example .env
./scripts/start
```

Then open http://localhost:8000/docs.

## Configuration

The app reads only generic environment variables (`.env.example`)
`LLM_API_KEY`, the model overrides, and -- if you sit behind an API gateway --  `LLM_GATEWAY_HOST` / `LLM_GATEWAY_PROJECT_ID` / `LLM_PROJECT_HEADER`. With the gateway variables empty, the client calls OpenAI and xAI directly.

## Examples
```bash
curl -X POST localhost:8000/ml/sentiment \
  -H 'Content-Type: application/json' \
  -d '{"text":"slept really well and woke up refreshed"}'

curl -X POST localhost:8000/ml/recommend \
  -H 'Content-Type: application/json' \
  -d '{"text":"i keep waking up at night","top_k:3"}'

curl -X POST localhost:8000/api/insights/activity \
  -H 'Content-Type: application/json' \
  -d '{"activityName":"scrolling on my phone","duration": 30}'
```
