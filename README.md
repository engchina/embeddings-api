# Embeddings API

## Install

```
conda create -n embeddings-api python=3.11 -y
conda activate embeddings-api
```

```
python -m pip install -U pip setuptools wheel
python -m pip install packaging ninja psutil

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

## Use

```
http://localhost:7965/v1/embed
```

## Supported Models

- text-embedding-3-large
- text-embedding-3-small
- text-embedding-ada-002
- multilingual-e5-large-instruct
