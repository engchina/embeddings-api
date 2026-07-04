# Embeddings API

## Install

```
conda create -n embeddings-api python=3.11 -y
conda activate embeddings-api
```

```
python -m pip install -U pip setuptools wheel
python -m pip install packaging ninja psutil

pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124

python -c "import torch; print(torch.__version__, torch.version.cuda)"

grep -v '^flash-attn' requirements.txt > /tmp/requirements-no-flash-attn.txt
python -m pip install -r /tmp/requirements-no-flash-attn.txt

MAX_JOBS=4 python -m pip install flash-attn==2.7.0.post2 --no-build-isolation
```

## Run

```
uvicorn openai_api:app --reload --host 0.0.0.0 --port 7965

# or on windows
./main.bat

# or on linux
./main.sh
```

## Use Example

```
curl -s -X POST "http://localhost:7965/v1/embeddings" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-3-large",
    "input": [
      "これは日本語の埋め込みAPIテストです。",
      "東京都の天気について教えてください。",
      "Oracle Databaseのベクトル検索機能を検証しています。",
      "多言語モデルで日本語文書の意味検索を行います。"
    ]
  }' | jq '{
    model,
    count: (.data | length),
    dims: [.data[].embedding | length],
    usage
  }'
```

## Supported Models

- text-embedding-3-large
