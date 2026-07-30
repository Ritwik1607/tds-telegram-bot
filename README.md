# Data Analyst Telegram Agent

An LLM-powered data analysis agent that can download datasets,
generate analysis plans, execute pandas operations, and answer
questions through Telegram.

## Features

- Dataset URL ingestion
- LLM-based planning using Groq Llama
- Structured pandas execution
- Automatic result explanation
- JSONL agent logging

## Architecture

User
 |
Telegram Bot
 |
Planner
 |
DataFrame Engine
 |
LLM Response

## Setup

Clone repository:

git clone <repo-url>

Install dependencies:

pip install -r requirements.txt

Create .env:

GROQ_API_KEY=
TELEGRAM_BOT_TOKEN=

Run:

python bot.py

## Telegram Bot

Username:
@Dalyze_bot