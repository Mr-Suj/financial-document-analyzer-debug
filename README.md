# Financial Document Analyzer – Debug Challenge Submission

## Overview

This project is a fixed and enhanced version of a buggy CrewAI-based financial document analysis system provided as part of a debugging assignment.

The original project contained multiple architectural issues, dependency conflicts, incorrect CrewAI usage, and runtime failures. This submission focuses on debugging, stabilizing, and upgrading the system into a clean, production-style implementation.

Key Improvements:

* Fully fixed and working system
* Correct CrewAI agent architecture
* FastAPI backend with background worker model
* Database integration (SQLite)
* Environment-based API key configuration
* Graceful fallback mode when LLM quota fails

The system now runs end-to-end and supports asynchronous processing of financial document analysis.

---

## Bugs Found and Fixes

### 1. Dependency Conflicts

Issues:

* Pydantic version mismatch
* CrewAI dependency conflicts
* OpenAI SDK incompatibilities

Fix:

* Cleaned requirements.txt
* Installed compatible versions
* Rebuilt virtual environment

---

### 2. Incorrect CrewAI Usage

Issues:

* Wrong agent imports
* Tools not extending BaseTool
* Pydantic validation errors
* Improper task configuration

Fix:

* Migrated to latest CrewAI usage
* Implemented proper BaseTool classes
* Fixed Agent and Task initialization

---

### 3. FastAPI Runtime Problems

Issues:

* Missing python-multipart dependency
* Blocking execution flow
* No concurrency handling

Fix:

* Added required dependencies
* Implemented background processing using FastAPI BackgroundTasks

---

### 4. OpenAI Quota / Rate Limit Handling

During development, quota limits caused failures.

Engineering Decision:

* Use real LLM if valid API key exists
* Gracefully fallback to mock response if LLM fails

Benefits:

* Stable pipeline
* Recruiters can test using their own API key
* No crashes during evaluation

---

## Architecture Overview

### FastAPI Backend

* REST API
* Swagger documentation (/docs)
* Async background processing

---

### CrewAI Multi-Agent System

Agents:

* Financial Analyst
* Document Verifier
* Investment Advisor
* Risk Assessor

Uses structured task execution with CrewAI.

---

### Queue Worker Model (Bonus Requirement)

Implemented lightweight queue architecture using FastAPI BackgroundTasks.

Workflow:

1. User uploads document
2. Job queued with job_id
3. Background worker processes analysis
4. Result saved to database
5. User retrieves result via API

---

### Database Integration (Bonus Requirement)

SQLite database stores:

* job_id
* user query
* analysis result

Table Schema:

analysis_results (
id TEXT PRIMARY KEY,
query TEXT,
result TEXT
)

---

## Project Structure

```text
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

Recruiters can use their own API key for testing.

---

## Running the Server

```bash
python main.py
```

Open Swagger UI:

http://localhost:8000/docs

---

## API Documentation

### POST /analyze

Uploads financial document and starts background analysis.

Response:

```json
{
  "status": "queued",
  "job_id": "uuid"
}
```

---

### GET /result/{job_id}

Check analysis result.

Processing:

```json
{
  "status": "processing"
}
```

Completed:

```json
{
  "status": "completed",
  "analysis": "Generated analysis text"
}
```

---

## Fallback Mode

If:

* API key missing
* Quota exceeded
* External LLM failure

System automatically returns mock structured response.

Purpose:

* Maintain API stability
* Allow testing without paid API access
* Demonstrate robust engineering design

---

## Key Engineering Improvements

* Fixed dependency conflicts
* Correct CrewAI architecture
* Background worker implementation
* Database persistence layer
* Environment-based configuration
* Graceful error handling
* Structured API design

---

## CrewAI Reference

https://docs.crewai.com/en/quickstart

---

## Author

Sujal Gowda J M
