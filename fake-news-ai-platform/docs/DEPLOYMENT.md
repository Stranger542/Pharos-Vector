# Deployment Guide

## Prerequisites

- Kubernetes cluster access and context configured.
- Docker Hub account with repository access for images.
- Environment variable secrets stored securely (e.g., GitHub Secrets).

## Steps

1. Build Docker images for backend and frontend (`scripts/build.sh`).
2. Push images to Docker Hub.
3. Apply Kubernetes manifests using `kubectl apply -f infrastructure/kube/`.
4. Configure ingress DNS to your domain (environment-specific).
5. Monitor pods and services with `kubectl get pods,svc -n fakenews-platform`.
6. Use `scripts/deploy.sh` for automated deployment.
7. Backup Postgres regularly with `scripts/backup.sh`.

## Notes

- Use `infrastructure/docker-compose.prod.yml` for local production-like testing.
- CI/CD pipelines handle automation on main branch pushes.
