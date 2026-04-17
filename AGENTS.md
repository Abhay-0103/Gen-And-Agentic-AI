# AGENTS.md

This workspace is a set of small GenAI lessons and demos. Keep changes minimal, script-friendly, and consistent with the existing examples.

## Working Style

- Treat each numbered folder as an independent lesson unless the user asks to connect them.
- Prefer small, direct edits over abstractions or framework-wide refactors.
- Keep examples self-contained and runnable as standalone scripts.
- Preserve the teaching style of the existing code unless a change is explicitly requested.

## Environment

- Use the existing virtual environment in the workspace when running or testing code.
- Most scripts load environment variables with `python-dotenv`.
- Gemini access is commonly configured through `GEMINI_API_KEY` and the OpenAI-compatible base URL `https://generativelanguage.googleapis.com/v1beta/openai/`.
- Many lessons rely on local services such as Qdrant, Redis, MongoDB, or Ollama; check the lesson folder before assuming a dependency is available.

## Conventions

- Follow the current print-driven, example-first style in the lesson scripts.
- Keep prompt examples concise and aligned with [04_Prompt-Style/prompt_style.md](04_Prompt-Style/prompt_style.md).
- For Docker-backed lessons, use the folder-local compose file instead of duplicating service definitions.
- Be careful with numbered folder names such as `08_RAG` and `11_langGraph_learning`; they are part of the lesson structure.
- Several lessons are intentionally minimal and do not include reusable package boundaries or CLI wrappers.

## Before Editing

- Check the lesson-specific files in the target folder first.
- Prefer updating the lesson’s own `requirements.txt` when a script only needs a narrow dependency set.
- Avoid renaming lesson folders or files unless the user explicitly asks.

## Useful References

- [04_Prompt-Style/prompt_style.md](04_Prompt-Style/prompt_style.md)
- [08_RAG/docker-compose.yml](08_RAG/docker-compose.yml)
- [09_RAG_queue/docker-compose.yml](09_RAG_queue/docker-compose.yml)
- [11_langGraph_learning/docker-compose.yml](11_langGraph_learning/docker-compose.yml)
- [12_mem0/docker-compose.yml](12_mem0/docker-compose.yml)
