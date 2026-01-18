# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Shepherd** - A multipurpose AI agent built with Python and Google's Gemini API. Evolving from code assistance into business automation and process orchestration.

## Commands

```bash
# Install dependencies
uv sync

# Run the application
uv run python main.py
```

## Dependencies

- `google-genai` - Google's GenAI SDK for LLM interactions
- `python-dotenv` - Environment variable management (expects `.env` file for API keys)
