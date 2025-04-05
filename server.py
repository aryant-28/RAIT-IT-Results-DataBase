#!/usr/bin/env python3
"""
Server entry point for the Flask application.
This file creates and exposes the Flask app instance.
"""
import os
from app import create_app

# Create the Flask application instance
application = create_app()
app = application  # For compatibility with different WSGI servers

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host="0.0.0.0", port=port) 