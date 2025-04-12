#!/bin/bash
set -e

# Start the FastAPI application with logging
uvicorn app.main:app --host 0.0.0.0 --port 5000 --log-level debug