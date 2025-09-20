#!/bin/bash
set -e

echo "Building backend Docker image..."
docker build -t yourrepo/backend:latest ../backend

echo "Building frontend Docker image..."
docker build -t yourrepo/frontend:latest ../frontend
