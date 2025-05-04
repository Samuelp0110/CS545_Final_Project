#!/bin/bash

# Start backend
cd backend
uvicorn app.main:app --reload &
BACK_PID=$!

# Start frontend
cd ../frontend
npm run dev &

# Trap CTRL+C and kill background processes
trap "kill $BACK_PID" EXIT

# Wait for both to exit
wait
