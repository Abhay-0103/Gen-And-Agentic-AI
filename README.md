# Gen-AI and Agentic-AI

This repository is a collection of small GenAI lessons and demos. Each numbered folder is a self-contained example that focuses on one topic, tool, or workflow.

## What Is In This Repo

- Prompting basics and prompt styles
- Gemini-based chat examples using the OpenAI-compatible API format
- FastAPI and Ollama examples
- Hugging Face and embedding demos
- RAG workflows with Qdrant
- Queued RAG with Redis and RQ
- LangGraph, memory, image, and voice examples

## Folder Structure

```text
.
├── .gitignore
├── AGENTS.md
├── README.md
├── requirements.txt
├── 01_Tokenization/
│   ├── main.py
│   └── requirements.txt
├── 02_hello_world/
│   ├── .env
│   ├── .gitignore
│   ├── main.py
│   └── requirements.txt
├── 03_prompts/
│   ├── .env
│   ├── .gitignore
│   ├── 01_Zero.py
│   ├── 02_few.py
│   ├── 03_cot.py
│   ├── 04_persona.py
│   └── requirements.txt
├── 04_Prompt-Style/
│   └── prompt_style.md
├── 05_ollama_fastapi/
│   ├── 01_server.py
│   └── 02_server.py
├── 06_hf_basic/
│   └── main.py
├── 07_weather_agent/
│   ├── .env
│   ├── agent.py
│   ├── main.py
│   └── requirements.txt
├── 08_RAG/
│   ├── .env
│   ├── 01_index.py
│   ├── 02_index.py
│   ├── 03_index.py
│   ├── 04_chat.py
│   ├── docker-compose.yml
│   └── nodejs.pdf
├── 09_RAG_queue/
│   ├── .env
│   ├── client/
│   │   ├── __init__.py
│   │   └── rq_client.py
│   ├── docker-compose.yml
│   ├── main.py
│   ├── queues/
│   │   ├── __init__.py
│   │   └── worker.py
│   └── server.py
├── 10_images/
│   ├── .env
│   └── main.py
├── 11_langGraph_learning/
│   ├── .env
│   ├── 01_chat.py
│   ├── 02_chat.py
│   ├── 03_chat_checkpoint.py
│   └── docker-compose.yml
├── 12_mem0/
│   ├── .env
│   ├── docker-compose.yml
│   └── mem.py
└── 13_voice_agent/
    └── main.py
```

Generated directories such as `.git/`, `venv/`, and `__pycache__/` are intentionally omitted from the tree above.

## Setup

1. Create and activate the existing virtual environment.
2. Install the shared dependencies:

```bash
pip install -r requirements.txt
```

3. If a lesson has its own `requirements.txt`, install that file inside the lesson folder as well.

## Environment Variables

Most examples use `python-dotenv` and expect environment variables such as:

- `GEMINI_API_KEY`
- `OPENAI_API_KEY` for lessons that use OpenAI-compatible clients

The Gemini examples usually use this base URL:

```text
https://generativelanguage.googleapis.com/v1beta/openai/
```

## Running A Lesson

Run lesson scripts directly from the repository root, for example:

```bash
python 03_prompts/01_Zero.py
python 07_weather_agent/main.py
python 08_RAG/04_chat.py
```

Some lessons depend on local services. Make sure those services are running before you start the script.

## Service-Backed Lessons

- `08_RAG` uses Qdrant and expects the collection to exist before chat runs.
- `09_RAG_queue` uses Redis and queue worker processes.
- `11_langGraph_learning` may rely on MongoDB for checkpointing.
- `12_mem0` uses a Docker-backed memory service.
- `05_ollama_fastapi` expects Ollama to be available locally.

Use the folder-local `docker-compose.yml` files for service-backed lessons instead of copying service definitions into the root.

## Prompt Style Reference

See [04_Prompt-Style/prompt_style.md](04_Prompt-Style/prompt_style.md) for the prompt examples used in this workspace.

## Conventions

- Keep changes small and lesson-focused.
- Preserve the print-driven, example-first style used throughout the repo.
- Avoid renaming numbered folders unless the change explicitly requires it.
- Prefer updating a lesson's own dependency file when only one lesson needs a package.

## Notes For Contributors

- The numbered folders are intentionally independent.
- Many scripts are minimal on purpose and do not include reusable CLI wrappers.
- When a lesson depends on a local service, document the dependency in that lesson folder rather than duplicating it at the root.