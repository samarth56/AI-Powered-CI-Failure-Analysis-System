# AI-Powered-CI-Failure-Analysis-System

An end-to-end AI-driven CI intelligence system that automatically analyzes Jenkins test failures, explains the root cause in plain English, and suggests actionable fixes — directly inside the Jenkins console.

This project demonstrates how GenAI can be embedded into real DevOps and backend systems, not just used via standalone prompts.

📌 Problem Statement

CI pipelines often fail with long, noisy stack traces that:

Are hard to interpret

Waste developer debugging time

Provide no actionable guidance

Developers don’t want logs — they want answers.

✅ Solution Overview

This system integrates Jenkins, TestNG, FastAPI, and GenAI to automatically:

Capture test failure logs from Jenkins

Analyze them using an LLM

Generate:

Exact root cause

Explanation of why the failure happened

Suggested fixes

What to check if it repeats

Display results directly in the Jenkins console

Persist logs and AI analysis for future reference

🏗️ Architecture Overview

Flow:

Jenkins runs Maven + TestNG tests

On failure:

Surefire logs are collected

Logs are sent to a FastAPI backend

AI analyzes the failure

Results are:

Printed in Jenkins console

Stored in database for historical analysis

Jenkins → TestNG → Surefire Logs
                ↓
           FastAPI Backend
                ↓
           AI Failure Analysis
                ↓
     Jenkins Console + Database

⚙️ Tech Stack

CI/CD: Jenkins

Testing: Java, TestNG, Maven

Backend: FastAPI (Python)

Database: PostgreSQL (log storage & analysis)

AI: LLM-based log analysis (local / API-based)

DevOps: Git, GitHub, Jenkins Pipelines

🧠 AI Prompt Design

The AI is prompted as a Senior QA Automation Engineer and instructed to return structured output including:

Root cause

Why the failure happened

Suggested code/test fixes

What to check next if it repeats

This ensures consistent, actionable responses, not generic explanations.

📄 Sample AI Output (Shown in Jenkins Console)
{
  "root_cause": "java.lang.AssertionError: Expected true but found false",
  "why": "The assertion failed because the test condition was hardcoded to false.",
  "suggested_fix": "Update the assertion logic or fix the expected value.",
  "check_next": "Verify test data and assertion conditions."
}

🗄️ Data Persistence

Raw logs and AI analysis are stored in the database

Enables:

Historical failure tracking

Pattern analysis

Future ML-based failure classification

🎯 Why This Project Matters

Shows real-world GenAI integration, not just API calls

Demonstrates backend + DevOps + data flow

Mirrors how AI is used in production CI platforms

Reduces developer debugging time significantly

📈 Future Enhancements

Failure categorization (test, infra, data, environment)

Confidence scoring for AI suggestions

Learning from historical failures

Slack / Email notifications

Dashboard for failure trends

🧩 Key Learnings

How CI systems generate and manage logs

How to design AI prompts for deterministic outputs

How backend services integrate with DevOps pipelines

How data persistence enables smarter AI systems

How GenAI fits into real engineering workflows

🏁 Conclusion

This project bridges CI/CD, backend engineering, data handling, and GenAI, showcasing how AI can enhance developer productivity when embedded into real systems.
