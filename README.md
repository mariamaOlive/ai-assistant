# AI Assistant with Tool Calling (Calculator)

## Overview
This project implements a small AI assistant that can **decide when to answer normally** (LLM-only) and **when to call an external tool** (a calculator).

---

## Setup (Notebook)

### 1) Create and activate a virtual environment

macOS/Linux
```bash
python -m venv .venv
source .venv/bin/activate  
```
Windows
```bash
python -m venv .venv
.venv\Scripts\activate  
```

### 2) Install dependencies
```bash
pip install -r requirements.txt
```

### 3) Configure environment variables
Copy the example env file and fill in your credentials:
```bash
cp .env.example .env
```

Set at least:
```
OPENAI_API_KEY=...
```

⚠️ Do not commit your .env file.

### 4) Run the notebook
```bash
jupyter notebook
```

Open the project notebook and run the cells in order.

---

## Approach

Brief description of the approach utilized on the case. More comments are available on the notebook.

### Choosing the framework
I used LangChain because it simplifies:
- building an agent-style,
- integrating tool calling,
- working with different model providers through a consistent interface.

### Model configuration
I used an OpenAI chat model (GPT-4).

Configuration choices:
- temperature = 0: reduces randomness and keeps answers deterministic (no creativity needed for this case).
- max_tokens = 500: caps the maximum length of the generated output, which is enough for the expected responses.

### Agent Architecture
This implementation uses a single agent responsible for:
- receiving the user question,
- deciding whether it requires an exact arithmetic calculation,
- calling the calculator tool (math) or answering directly (non-math).

A multi-agent design (e.g., a separate router agent plus specialized agents) is possible, but it would add unnecessary complexity for this simple task.

---

## Project Structure

Tools and prompts are stored in separate files rather than embedded directly in the notebook.

This improves maintainability and reuse as the project grows.

Project structure:
```
.
├─ README.md
├─ requirements.txt
├─ .env.example
├─ case_notebook.ipynb
├─ prompts/
│  └─ prompts.py
└─ tools/
   └─ calculator.py
```
