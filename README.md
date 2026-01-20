# Shepherd

A multipurpose AI agent built with Google's Gemini API. Designed to evolve beyond code assistance into a general-purpose automation platform for business workflows and process orchestration.

## Vision

The end goal: anything you could teach a junior assistant to do on a computer.

- Read emails, extract info, book appointments
- Send follow-ups and reminders
- Pull reports, summarize trends
- Monitor inventory, draft restock orders
- Chain APIs together to automate workflows

The pattern: **trigger → understand → decide → act → report**

## How It Works

The AI is the brain. Tools are the hands.

```
User request
    ↓
Shepherd (understands, decides)
    ↓
Calls tools (Python functions)
    ↓
Tools hit APIs/services (Gmail, Calendar, n8n, etc.)
    ↓
Returns result
```

Each tool is a Python function in `functions/`. The AI decides when to use it and what to pass in.

## Setup

1. Install dependencies:
   ```bash
   uv sync
   ```

2. Create a `.env` file:
   ```
   GEMINI_API_KEY=your_key_here
   ```

3. Run:
   ```bash
   uv run python main.py "your prompt here"
   ```

Use `--verbose` for token usage and debug info.

## Project Structure

```
├── main.py                  # Entry point, Gemini client, CLI
├── functions/               # Agent tools
│   └── get_files_info.py    # List directory contents
├── test_get_files_info.py   # Manual tool testing
└── calculator/              # Example project for testing
```

## Tools

| Tool | Description |
|------|-------------|
| `get_files_info` | List directory contents with file sizes and types. Includes path security to prevent escaping the working directory. |

## Roadmap

- [x] Gemini API integration
- [x] CLI with argparse (`--verbose`)
- [x] Message history structure (Content/Part types)
- [x] First tool: `get_files_info`
- [x] Path security (normpath, commonpath)
- [ ] Multi-turn conversations
- [ ] Tool/function calling integration with Gemini
- [ ] File read/write tools
- [ ] Code execution tool
- [ ] n8n webhook integration
- [ ] Business automation workflows

## Integration

Shepherd can plug into **n8n** for easier automation:

- n8n handles pre-built connectors (400+ services), auth, triggers
- Shepherd handles understanding, deciding, orchestrating
- Connect via webhooks: Shepherd calls n8n workflows as tools

## Author

Built by Dylan Lamb ([@bydylanlamb](https://twitter.com/bydylanlamb))
