#!/bin/bash
set -e

kubectl apply -f kube/namespace.yaml
kubectl config set-context --current --namespace=fakenews-platform

echo "Deploying configmap..."
kubectl apply -f kube/configmap.yaml

echo "Deploying postgres..."
kubectl apply -f kube/postgres-deployment.yaml

echo "Deploying redis..."
kubectl apply -f kube/redis-deployment.yaml

echo "Deploying backend..."
kubectl apply -f kube/backend-deployment.yaml

echo "Deploying frontend..."
kubectl apply -f kube/frontend-deployment.yaml

echo "Deploying services..."
kubectl apply -f kube/service.yaml

echo "Deploying ingress..."
kubectl apply -f kube/ingress.yaml
