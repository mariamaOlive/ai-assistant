# AI Assistant with Tool Calling (Calculator)
###  Artefact Case - Junior AI Engineer

Mariama Oliveira - AI Engineer – Full-Stack para Aplicações com IA Generativa - Vaga afirmativa para mulheres cis e trans


## Overview
This project implements a small AI assistant that can **decide when to answer normally** (LLM-only) and **when to call an external tool** (a calculator).

---
## Pré-requisitos

- Python 3.8+
- Jupyter Notebook

## Setup (Notebook)

### 1) Create and activate a virtual environment

First, make sure you're in the project directory and then:

macOS/Linux
```bash
python3 -m venv .venv
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
jupyter notebook case_notebook.ipynb
```

Open the project notebook and run the cells in order.

---

## Case Approach 

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

A multi-agent design (e.g., a separate router agent plus specialized agents) was considered, but it would add unnecessary complexity for this simple task.

As a BONUS feature it was included a call for a currency exchange rate for calculations replies. It was included as a bonus to demonstrate how the assistant can integrate additional external tools.

---
### Project Structure

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
   └─ exchange_rate.py
```
---
### Lessons learned and Limitations

1. LangChain, as the chosen framework, allows different types of configurations that can be selected according to the project’s needs. Because this is the MVP of an assistant, the configuration chosen was minimal. In a production environment, it would be worth leveraging additional features to improve maintainability and user experience, such as tracking users and conversations by ID and persisting conversation history across sessions.

2. Even though the assistant is working, there are some limitations. Mainly, for example, the ambiguity of how a mathematical expression can be written in natural language. For example: *“How much is the cube root of four multiplied by two?”* could be parsed as `(4 ** (1/3)) * 2` or as `(4 * 2) ** (1/3)`, depending on how the grouping is interpreted. Therefore, for better parsing a more in depth logic could be implemented.

3. The main focus of the implementation was tool calling (function invocation); therefore, the calculator implementation is limited and needs improvements if this solution were to go to production.

4. Before putting this kind of solution into production, it would also be important to monitor token usage and latency under different configurations (ex. chosen model, prompt) in order to choose the best approach.

5. Lastly, if more responsibilities were added to the assistant, I would probably split them across separate agents or adopt an agent pattern such as ReAct, because in my experience an agent with too many responsibilities tends to perform poorly across tasks or fail to execute some of them.
