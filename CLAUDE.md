# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Shepherd** - A multipurpose AI agent built with Python and Google's Gemini API. The goal is a general-purpose automation platform that can handle business workflows, not just coding tasks.

## Commands

```bash
# Install dependencies
uv sync

# Run the application
uv run python main.py "your prompt" --verbose

# Test tools
uv run python test_get_files_info.py
```

## Dependencies

- `google-genai` - Google's GenAI SDK for LLM interactions
- `python-dotenv` - Environment variable management (expects `.env` file for API keys)

## Architecture

```
main.py                     # CLI, Gemini client, message handling
functions/                  # Agent tools (Python functions)
  └── get_files_info.py     # Directory listing with path security
```

**Pattern for tools:**
1. Each tool is a Python function in `functions/`
2. Takes inputs, returns a string result
3. Handles errors gracefully (returns "Error: ..." strings)
4. Security: validate paths stay within working directory

## Key Concepts

**Message structure:**
```python
messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
]
```

**Path security pattern:**
```python
abs_working_dir = os.path.abspath(working_directory)
target = os.path.normpath(os.path.join(abs_working_dir, directory))
if os.path.commonpath([abs_working_dir, target]) != abs_working_dir:
    return "Error: outside permitted directory"
```

## What's Built

- [x] Gemini client with API key from `.env`
- [x] CLI args with argparse (`--verbose` flag)
- [x] Message list using `types.Content` and `types.Part`
- [x] Token usage reporting (verbose mode)
- [x] `get_files_info` tool with path security

## Next Up

- Multi-turn conversations (maintain message history)
- Register tools with Gemini for function calling
- More tools: read file, write file, run code
- n8n webhook integration for external automations
