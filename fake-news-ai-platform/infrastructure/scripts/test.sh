#!/bin/bash
set -e

echo "Running backend tests..."
cd ../backend
pytest app/tests

echo "Running frontend tests..."
cd ../frontend
npm test -- --watchAll=false
