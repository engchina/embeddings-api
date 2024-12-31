call conda activate embeddings-api
uvicorn openai_api:app --reload --host 0.0.0.0 --port 7965