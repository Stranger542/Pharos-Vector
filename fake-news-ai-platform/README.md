# Fake News Detection & Media Literacy Platform

## Overview

This project combines state-of-the-art AI-driven fake news detection with interactive media literacy tools to help users critically evaluate news.

## Features

- Multi-stage fake news detection using Transformer models.
- Source credibility analysis via NewsGuard.
- Claim cross-verification with Google Fact Check API.
- Interactive educational modules on media literacy.
- Responsive React frontend with rich visualizations.
- Scalable FastAPI backend with reliable ML integration.

## Setup

1. Clone this repo.
2. Create `.env` files in backend and frontend from `.env.example`.
3. Run `docker-compose up --build` for local dev environment.
4. For production, deploy via Kubernetes with provided manifests.
5. Use GitHub Actions for CI/CD workflows.

## Documentation

See `docs/` folder for API, Architecture, and Deployment guides.

## License

MIT License
