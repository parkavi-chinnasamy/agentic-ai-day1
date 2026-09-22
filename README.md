# Agentic AI Day 1 Lab

## Chatbot vs Rule-Based Workflow vs AI Agent

A practical **Agentic AI Day 1 laboratory project** that demonstrates the difference between a traditional LLM chatbot, a rule-based workflow, and an AI agent capable of using external tools.

The project uses **Python, VS Code, Groq API, and an OpenAI-compatible API interface** to demonstrate how AI systems evolve from simple question answering to tool-using agents.

---

## 📌 Project Overview

This project addresses a simple college course-fee scenario where the fee information is **private** and is not directly available to a general-purpose LLM.

The system compares three different approaches:

1. **LLM Chatbot** – directly communicates with the language model.
2. **Rule-Based Workflow** – uses predefined Python rules.
3. **AI Agent** – uses an LLM with external tools to retrieve information and perform calculations.

The comparison demonstrates why **tool usage is an important component of Agentic AI**.

---

## 🎯 Objectives

* Understand the basic concept of Agentic AI.
* Differentiate between an LLM chatbot, rule-based workflow, and AI agent.
* Implement a simple LLM-powered chatbot.
* Implement a deterministic rule-based workflow using Python.
* Build an AI agent capable of using external tools.
* Understand tool calling and multi-step reasoning.
* Compare the strengths and limitations of each approach.

---

## 🧩 Problem Statement

A college maintains private course-fee information that is unavailable to a general-purpose LLM.

The available course information is:

| Course Code | Course                  |     Fee |
| ----------- | ----------------------- | ------: |
| CS101       | Computer Science        | ₹12,000 |
| AI202       | Artificial Intelligence | ₹18,000 |
| DS303       | Data Science            | ₹15,000 |

The systems are tested with different types of questions, including:

* Course-fee queries
* Course comparisons
* Scholarship-related questions
* Arithmetic calculations
* Student communication queries

The objective is to observe how each system handles information that may require access to an external data source.

---

## 🏗️ System Architecture

```text
                         User Query
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        Simple Chatbot   Rule Workflow   AI Agent
              │              │              │
              ▼              ▼              ▼
             LLM        Python Rules       LLM
                                             │
                                      ┌──────┴──────┐
                                      │             │
                                      ▼             ▼
                              Course Fee Tool   Calculator
                                      │             │
                                      └──────┬──────┘
                                             ▼
                                      Final Response
```

---

# 🤖 Three Systems

## 1. Simple LLM Chatbot

**File:** `chatbot.py`

The chatbot sends the user's question directly to the LLM and returns the generated response.

### Characteristics

* Uses an LLM for response generation.
* Does not directly access the college's private fee database.
* Cannot retrieve private course information unless it is provided in the prompt.
* Suitable for general conversational questions.

### Example

```text
User:
What is the fee for AI202?

Chatbot:
I don't have access to your college's private fee database.
```

This demonstrates the limitation of a standalone LLM when required information exists outside its knowledge or context.

---

## 2. Rule-Based Workflow

**File:** `workflow.py`

The workflow uses predefined Python rules to process specific types of questions.

### Characteristics

* Does not require an LLM.
* Uses deterministic `if/else` or predefined logic.
* Can directly access the course-fee data.
* Produces predictable results.
* Has limited flexibility for unexpected questions.

### Example

```text
User:
What is the fee for AI202?

Workflow:
The fee for AI202 is ₹18,000.
```

However, a rule-based system may struggle with variations such as:

```text
"How much would I need to pay for the AI course?"
```

unless that specific pattern has been programmed.

---

## 3. AI Agent

**Files:** `agent.py`, `tools.py`

The AI agent combines an LLM with external tools.

Instead of answering every question directly, the agent can determine when additional information or computation is required.

### Agent Capabilities

The AI agent can:

* Understand the user's request.
* Determine whether a tool is required.
* Retrieve private course-fee information.
* Perform calculations using a calculator tool.
* Use multiple tools in sequence.
* Combine tool results with the LLM's language capabilities.
* Generate a final response based on the retrieved information.

### Example

```text
User:
What is the fee for AI202?

Agent:
1. Identifies that course-fee information is required.
2. Calls get_course_fee("AI202").
3. Receives ₹18,000.
4. Generates the final response.

Final Response:
The fee for AI202 is ₹18,000.
```

---

# 🔧 Tools

The project contains two primary tools.

## 1. `get_course_fee`

Retrieves the fee associated with a course code.

### Example

```python
get_course_fee("AI202")
```

Output:

```text
18000
```

### Available Courses

```text
CS101 → ₹12,000
AI202 → ₹18,000
DS303 → ₹15,000
```

---

## 2. Calculator Tool

The calculator tool performs arithmetic operations required by the agent.

For example:

```text
18000 + 15000
```

Output:

```text
33000
```

This allows the agent to perform calculations using a tool instead of relying only on language-model generation.

---

# 🔄 Agent Workflow

The basic agent workflow is:

```text
User Query
    ↓
LLM analyzes the request
    ↓
Determine whether a tool is required
    ↓
Tool Call
    ↓
Tool executes the requested operation
    ↓
Tool Result returned to LLM
    ↓
LLM generates final response
    ↓
User receives answer
```

For a question requiring multiple operations:

```text
User Query
    ↓
Identify required information
    ↓
get_course_fee()
    ↓
Calculator Tool
    ↓
Combine Results
    ↓
Generate Final Answer
```

---

# 📊 Comparison

| Feature                   | Simple Chatbot | Rule-Based Workflow   | AI Agent        |
| ------------------------- | -------------- | --------------------- | --------------- |
| Uses LLM                  | ✅              | ❌                     | ✅               |
| Uses predefined rules     | ❌              | ✅                     | Partially       |
| Accesses external tools   | ❌              | Directly through code | ✅               |
| Handles general language  | ✅              | Limited               | ✅               |
| Handles private data      | ❌              | ✅                     | ✅               |
| Performs calculations     | LLM-based      | Python-based          | Calculator tool |
| Flexible to new questions | High           | Low                   | High            |
| Tool selection            | ❌              | Predefined            | ✅               |
| Multi-step operations     | Limited        | Predefined            | ✅               |
| Agentic behavior          | ❌              | ❌                     | ✅               |

---

# 🛠️ Technologies Used

* **Python** – Core programming language
* **Groq** – LLM API provider
* **OpenAI-Compatible API** – Interface for interacting with the model
* **VS Code** – Development environment
* **Git & GitHub** – Version control and project hosting

---

# 📁 Project Structure

```text
Agentic-AI-Day1/
│
├── chatbot.py
├── workflow.py
├── agent.py
├── tools.py
├── requirements.txt
├── README.md
│
└── outputs/
    ├── chatbot_output.png
    ├── workflow_output.png
    └── agent_output.png
```

### File Description

| File               | Purpose                                  |
| ------------------ | ---------------------------------------- |
| `chatbot.py`       | Implements the simple LLM chatbot        |
| `workflow.py`      | Implements the rule-based workflow       |
| `agent.py`         | Implements the AI agent                  |
| `tools.py`         | Contains the tools used by the agent     |
| `requirements.txt` | Contains required Python packages        |
| `outputs/`         | Stores screenshots and execution results |
| `README.md`        | Project documentation                    |

---

# ⚙️ Installation and Setup

## Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
cd Agentic-AI-Day1
```

## Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Configure API Key

Create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

> Do not upload your API key or `.env` file to GitHub.

Add `.env` to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

# ▶️ Running the Project

Run each implementation separately.

### Simple Chatbot

```bash
python chatbot.py
```

### Rule-Based Workflow

```bash
python workflow.py
```

### AI Agent

```bash
python agent.py
```

Compare the outputs produced by the three systems.

---

# 🧪 Sample Test Cases

The following queries can be used to test the systems:

### Test Case 1 — Course Fee

```text
What is the fee for AI202?
```

Expected fee:

```text
₹18,000
```

### Test Case 2 — Course Comparison

```text
Which is more expensive, AI202 or DS303?
```

Expected result:

```text
AI202 is more expensive by ₹3,000.
```

### Test Case 3 — Total Fee

```text
What is the total fee for AI202 and DS303?
```

Expected result:

```text
₹33,000
```

### Test Case 4 — General Communication

```text
How should I ask my faculty about a scholarship?
```

This tests the language-generation capability of the systems.

---

# 📸 Output Screenshots

Execution screenshots are stored in the `outputs/` folder.

```text
outputs/
│
├── chatbot_output.png
├── workflow_output.png
└── agent_output.png
```

These screenshots provide evidence of the execution and comparison of the three approaches.

---

# 💡 Key Learning

This practical demonstrates an important progression in AI systems:

```text
LLM
 ↓
LLM + Rules
 ↓
LLM + Tools
 ↓
AI Agent
```

A chatbot primarily generates responses, while an AI agent can **decide when to use tools, obtain external information, perform actions, and use the results to produce a final response**.

The key concept demonstrated in this lab is:

> **An AI agent extends an LLM's capabilities by allowing it to interact with external tools and data sources.**

---

# 📌 Conclusion

The Day 1 Agentic AI Lab provides a practical comparison between a simple LLM chatbot, a deterministic rule-based workflow, and a tool-using AI agent.

Through the course-fee example, the project demonstrates how tool integration enables an AI system to work with information that is not directly available to the language model and perform operations beyond simple text generation.

This forms a foundation for understanding more advanced **Agentic AI concepts such as tool calling, multi-step workflows, autonomous task execution, and intelligent decision-making**.

---

## 👩‍💻 Author

**Parkavi C.**
B.E. Computer Science and Engineering
Bannari Amman Institute of Technology

---

## ⭐ Project Status

**Day 1 – Completed**

This project is part of an ongoing learning journey in **Agentic AI and AI-powered application development**.
