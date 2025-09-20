# System Architecture

- **Frontend:** React SPA with components for news analysis, source credibility, media literacy tutorials.
- **Backend:** FastAPI REST API, modular with AI model inference, explainability, fact-checking modules.
- **ML Pipeline:** PyTorch BERT model with training, evaluation, and vectorizer modules.
- **Data Sources:** LIAR and ISOT datasets for training, NewsGuard and Google Fact Check APIs for validation.
- **Infrastructure:** Containerized via Docker and orchestrated with Kubernetes (EKS/GKE/Azure AKS).
- **CI/CD:** GitHub Actions automate testing, build, push, and deploy.
- **Security:** OAuth2 authentication, environment variable management, API rate limiting included.
