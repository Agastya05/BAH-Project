#!/bin/bash

# Start Rasa server
rasa run --enable-api &

# Start FastAPI server
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 &

# Start React development server
cd src/frontend && npm start

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?