# Financial Document Analyzer – Debug Challenge Submission

## Overview

This project is a fixed and enhanced version of a buggy CrewAI-based financial document analysis system provided as part of a debugging assignment.

The original project contained architectural issues, dependency conflicts, incorrect CrewAI usage, and runtime failures. This submission focuses on stabilizing, debugging, and upgrading the system into a clean, production-style implementation.

### Key Improvements

- Fully fixed and working system
- Correct CrewAI agent architecture
- FastAPI backend with background worker model
- Database integration (SQLite)
- Environment-based API key configuration
- Graceful fallback mode when LLM quota fails
- Stabilized dependencies for smoother installation

The system now runs end-to-end and supports asynchronous financial document analysis.

---

## Bugs Found and Fixes

### 1. Dependency Conflicts

**Issues:**
- Pydantic version mismatch
- CrewAI dependency conflicts
- OpenAI SDK incompatibilities
- Build failures from vector database dependencies

**Fix:**
- Cleaned and stabilized `requirements.txt`
- Removed unnecessary heavy dependencies
- Installed compatible versions
- Rebuilt virtual environment

Result:

```bash
pip install -r requirements.txt
```

Installs cleanly without manual build tools.

---

### 2. Incorrect CrewAI Usage

**Issues:**
- Incorrect agent imports
- Tools not extending BaseTool
- Pydantic validation errors
- Improper task configuration

**Fix:**
- Migrated to latest CrewAI usage patterns
- Implemented proper BaseTool classes
- Corrected Agent and Task initialization
- Cleaned tool integration logic

---

### 3. FastAPI Runtime Problems

**Issues:**
- Missing `python-multipart`
- Blocking execution flow
- No concurrency handling

**Fix:**
- Added required dependencies
- Implemented background processing using FastAPI `BackgroundTasks`

---

### 4. OpenAI Quota / Rate Limit Handling

During development, API quota limits caused failures.

**Engineering Decision:**

- Use real LLM when valid API key is available  
- Gracefully fallback to structured mock response if LLM fails  

**Benefits:**
- Stable pipeline behavior
- No crashes during evaluation
- Demonstrates resilient system design

---

## 5. Prompt Engineering & Hallucination Control

### Issues in Original Code

The original agent prompts and task descriptions contained intentionally chaotic and unsafe instructions, including:

- Encouraging hallucinated financial URLs
- Promoting contradictory outputs
- Instructions to ignore the user's query
- Random financial jargon generation
- Fabricated market predictions
- Non-deterministic and inconsistent analysis structure

These issues resulted in:

- Unreliable outputs
- High hallucination rate
- Inconsistent financial reasoning
- Non-production-safe behavior

---

### Fix Implemented

The prompting strategy was redesigned to improve reliability and align with production-grade practices:

- Rewritten task descriptions to strictly follow the user query
- Removed hallucination-inducing instructions
- Eliminated fabricated URL generation
- Introduced structured financial analysis format
- Enforced coherent and logically consistent output
- Reduced randomness in agent reasoning

---

### Result

- More deterministic and reliable responses
- Reduced hallucination probability
- Query-aligned financial insights
- Cleaner, production-style prompt design

---

## Architecture Overview

### FastAPI Backend

- REST API
- Swagger documentation (`/docs`)
- Async background processing

---

### CrewAI Multi-Agent System

Agents:

- Financial Analyst  
- Document Verifier  
- Investment Advisor  
- Risk Assessor  

Structured task execution using CrewAI.

---

### Queue Worker Model (Bonus Requirement)

Lightweight queue architecture using FastAPI `BackgroundTasks`.

**Workflow:**

1. User uploads document  
2. Job queued with `job_id`  
3. Background worker processes analysis  
4. Result saved to database  
5. User retrieves result via API  

---

### Database Integration (Bonus Requirement)

SQLite database stores:

- `job_id`
- `query`
- `analysis result`

**Table Schema:**

```sql
analysis_results (
  id TEXT PRIMARY KEY,
  query TEXT,
  result TEXT
)
```

---

## Project Structure

```
financial-document-analyzer-debug/
│
├── main.py              # FastAPI server + background worker + DB
├── agents.py            # CrewAI agent definitions
├── task.py              # Financial analysis task configuration
├── tools.py             # Custom BaseTool implementations
├── requirements.txt
├── .env.example         # Environment variable template
├── .gitignore
└── README.md
```

---

## Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/Mr-Suj/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Copy template:

```bash
copy .env.example .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

Provide your own OpenAI API key to enable real LLM execution.

---

## Running the Server

```bash
python main.py
```

Open Swagger UI:

```
http://localhost:8000/docs
```

---

## API Documentation

### POST `/analyze`

Uploads financial document and starts background analysis.

**Response:**

```json
{
  "status": "queued",
  "job_id": "uuid"
}
```

---

### GET `/result/{job_id}`

Check analysis result.

**Processing:**

```json
{
  "status": "processing"
}
```

**Completed:**

```json
{
  "status": "completed",
  "analysis": "Generated analysis text"
}
```

---

## Fallback Mode

If:

- API key missing  
- Quota exceeded  
- External LLM failure  

System automatically returns structured mock response.

**Purpose:**

- Maintain API stability  
- Allow testing without paid API access  
- Demonstrate robust engineering design  

---

## Key Engineering Improvements

- Fixed dependency conflicts  
- Correct CrewAI architecture  
- Background worker implementation  
- Database persistence layer  
- Prompt Engineering & Hallucination Control
- Environment-based configuration  
- Graceful error handling  
- Structured API design  
- Installation reliability improvements  

---

## Python Compatibility

Tested successfully with Python 3.11.

Dependencies stabilized for improved compatibility across modern Python environments.

---

## CrewAI Reference

https://docs.crewai.com/en/quickstart

---

## Author

**Sujal Gowda J M**  
Email: sujalgowda42@gmail.com