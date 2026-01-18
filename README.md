# Shepherd

A multipurpose AI agent built with Google's Gemini API. Shepherd is designed to evolve beyond code assistance into a versatile automation platform—handling everything from development tasks to business workflows and process orchestration.

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_key_here
   ```

3. Run:
   ```bash
   uv run python main.py "your prompt here"
   ```

Use `--verbose` for detailed output including token usage.

## Roadmap

- [x] Gemini API integration
- [ ] Multi-turn conversations
- [ ] Tool/function calling
- [ ] File operations
- [ ] Business automation workflows
- [ ] Process orchestration
