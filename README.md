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
* Clean dependency stabilization for easy setup

The system now runs end-to-end and supports asynchronous processing of financial document analysis.

---

## Bugs Found and Fixes

### 1. Dependency Conflicts

Issues:

* Pydantic version mismatch
* CrewAI dependency conflicts
* OpenAI SDK incompatibilities
* Build failures due to heavy vector database dependencies

Fix:

* Cleaned and stabilized requirements.txt
* Removed unnecessary heavy dependencies causing installation failures
* Installed compatible versions
* Rebuilt virtual environment from scratch

Result:

Project installs cleanly using:

pip install -r requirements.txt

---

### 2. Incorrect CrewAI Usage

Issues:

* Wrong agent imports
* Tools not extending BaseTool
* Pydantic validation errors
* Improper task configuration

Fix:

* Migrated to latest CrewAI usage patterns
* Implemented proper BaseTool classes
* Fixed Agent and Task initialization
* Cleaned tool integration workflow

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

During development, API quota limits caused failures.

Engineering Decision:

* Use real LLM if valid API key exists
* Gracefully fallback to mock response if LLM fails

Benefits:

* Stable pipeline behavior
* Recruiters can test using their own API key
* No crashes during evaluation
* Demonstrates resilient system design

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

financial-document-analyzer-debug/

main.py              # FastAPI server + background worker + DB  
agents.py            # CrewAI agent definitions  
task.py              # Financial analysis task configuration  
tools.py             # Custom BaseTool implementations  
requirements.txt  
.env.example         # Environment variable template  
.gitignore  
README.md  

---

## Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/Mr-Suj/financial-document-analyzer-debug.git
cd financial-document-analyzer-debug

---

### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Configure Environment Variables

Copy template:

copy .env.example .env

Edit `.env`:

OPENAI_API_KEY=your_api_key_here

Provide your own OpenAI API key in the .env file to enable real LLM execution.

---

## Running the Server

python main.py

Open Swagger UI:

http://localhost:8000/docs

---

## API Documentation

### POST /analyze

Uploads financial document and starts background analysis.

Response:

{
  "status": "queued",
  "job_id": "uuid"
}

---

### GET /result/{job_id}

Check analysis result.

Processing:

{
  "status": "processing"
}

Completed:

{
  "status": "completed",
  "analysis": "Generated analysis text"
}

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
* Dependency stabilization for smoother installation

---

## Python Compatibility

Tested successfully with Python 3.11.

Dependencies were stabilized to improve compatibility across modern Python environments.

---

## CrewAI Reference

https://docs.crewai.com/en/quickstart

---

## 📖 Author

Sujal Gowda J M

Email: sujalgowda42@gmail.com