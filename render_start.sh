#!/bin/bash
echo "Starting server with: gunicorn server:app"
export PYTHONUNBUFFERED=true
gunicorn server:app --bind=0.0.0.0:$PORT 