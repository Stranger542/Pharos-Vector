# This script creates the complete folder and file structure for the fake-news-ai-platform project.
# To run:
# 1. Save this file as "create_project.ps1".
# 2. Open a PowerShell terminal.
# 3. Navigate to the directory where you saved the file.
# 4. Run the command: .\create_project.ps1

# Set the root project name
$projectName = "fake-news-ai-platform"

# Create the root project directory and navigate into it
New-Item -ItemType Directory -Name $projectName
Set-Location $projectName

# --- Create Root Level ---
"backend", "frontend", "ml", "infrastructure", ".github", "docs" | ForEach-Object { New-Item -ItemType Directory -Name $_ }
".gitignore", ".dockerignore", "README.md", "LICENSE", "docker-compose.yml", "Makefile", "requirements.txt" | ForEach-Object { New-Item -ItemType File -Name $_ }

# --- Backend Structure ---
Set-Location "backend"
New-Item -ItemType Directory -Name "app"
"requirements.txt", "Dockerfile", ".env.example" | ForEach-Object { New-Item -ItemType File -Name $_ }
Set-Location "app"
"api", "core", "models", "schemas", "services", "tests" | ForEach-Object { New-Item -ItemType Directory -Name $_ }
"__init__.py", "main.py" | ForEach-Object { New-Item -ItemType File -Name $_ }
# API v1
New-Item -ItemType Directory -Path "api" -Name "v1"
New-Item -ItemType File -Path "api" -Name "__init__.py"
"__init__.py", "fake_news.py", "media_literacy.py", "source.py", "claims.py", "user.py" | ForEach-Object { New-Item -ItemType File -Path "api\v1" -Name $_ }
# Core
"__init__.py", "config.py", "security.py" | ForEach-Object { New-Item -ItemType File -Path "core" -Name $_ }
# Models
"__init__.py", "article.py", "source.py", "user.py", "claim.py" | ForEach-Object { New-Item -ItemType File -Path "models" -Name $_ }
# Schemas
"__init__.py", "article.py", "source.py", "user.py", "claim.py" | ForEach-Object { New-Item -ItemType File -Path "schemas" -Name $_ }
# Services
"__init__.py", "detection.py", "explainability.py", "media_literacy.py", "newsguard_api.py", "factcheck_api.py", "llm_synthesis.py", "celery_worker.py" | ForEach-Object { New-Item -ItemType File -Path "services" -Name $_ }
# Tests
"__init__.py", "test_api.py", "test_services.py" | ForEach-Object { New-Item -ItemType File -Path "tests" -Name $_ }
Set-Location "..\.."

# --- Frontend Structure ---
Set-Location "frontend"
"public", "src" | ForEach-Object { New-Item -ItemType Directory -Name $_ }
"package.json", "package-lock.json", "Dockerfile", ".env.example" | ForEach-Object { New-Item -ItemType File -Name $_ }
# Public
"index.html", "favicon.ico", "manifest.json" | ForEach-Object { New-Item -ItemType File -Path "public" -Name $_ }
# Src
Set-Location "src"
"components", "pages", "api", "utils", "styles" | ForEach-Object { New-Item -ItemType Directory -Name $_ }
"App.js", "index.js", "App.css" | ForEach-Object { New-Item -ItemType File -Name $_ }
# Components
"CredibilityReport", "HighlightText", "SourceAnalysis", "FactualCheck", "DataViz", "MediaLiteracy", "Auth", "common" | ForEach-Object { New-Item -ItemType Directory -Path "components" -Name $_ }
"CredibilityReport.js", "CredibilityReport.css" | ForEach-Object { New-Item -ItemType File -Path "components\CredibilityReport" -Name $_ }
"HighlightText.js", "HighlightText.css" | ForEach-Object { New-Item -ItemType File -Path "components\HighlightText" -Name $_ }
"SourceAnalysis.js", "SourceAnalysis.css" | ForEach-Object { New-Item -ItemType File -Path "components\SourceAnalysis" -Name $_ }
"FactualCheck.js", "FactualCheck.css" | ForEach-Object { New-Item -ItemType File -Path "components\FactualCheck" -Name $_ }
"DataViz.js", "DataViz.css" | ForEach-Object { New-Item -ItemType File -Path "components\DataViz" -Name $_ }
"DeconstructNews.js", "FallacyFinder.js", "CredibilityCoach.js", "MediaLiteracy.css" | ForEach-Object { New-Item -ItemType File -Path "components\MediaLiteracy" -Name $_ }
"Login.js", "Register.js", "Auth.css" | ForEach-Object { New-Item -ItemType File -Path "components\Auth" -Name $_ }
"Header.js", "Footer.js", "Layout.js" | ForEach-Object { New-Item -ItemType File -Path "components\common" -Name $_ }
# Pages
"Home.js", "Analysis.js", "Learning.js", "About.js", "Dashboard.js" | ForEach-Object { New-Item -ItemType File -Path "pages" -Name $_ }
# API
"client.js", "fakeNews.js", "mediaLiteracy.js", "user.js" | ForEach-Object { New-Item -ItemType File -Path "api" -Name $_ }
# Utils
"constants.js", "helpers.js", "validators.js" | ForEach-Object { New-Item -ItemType File -Path "utils" -Name $_ }
# Styles
"globals.css", "variables.css", "components.css" | ForEach-Object { New-Item -ItemType File -Path "styles" -Name $_ }
Set-Location "..\.."

# --- ML Structure ---
Set-Location "ml"
"data", "training", "evaluation", "models", "vectorizer" | ForEach-Object { New-Item -ItemType Directory -Name $_ }
New-Item -ItemType File -Name "README.md"
# Data
"download_prepare_datasets.py", "train.csv", "val.csv" | ForEach-Object { New-Item -ItemType File -Path "data" -Name $_ }
# Training
New-Item -ItemType File -Path "training" -Name "train_bert.py"
# Evaluation
"eval_bert.py", "confusion_matrix.png" | ForEach-Object { New-Item -ItemType File -Path "evaluation" -Name $_ }
# Models
"bert_fake_news_classifier.py", "bert_fakenews.pt" | ForEach-Object { New-Item -ItemType File -Path "models" -Name $_ }
# Vectorizer
"tfidf_vectorizer.py", "tfidf_vectorizer.pkl" | ForEach-Object { New-Item -ItemType File -Path "vectorizer" -Name $_ }
Set-Location ".."

# --- Infrastructure Structure ---
Set-Location "infrastructure"
"kube", "scripts", "terraform" | ForEach-Object { New-Item -ItemType Directory -Name $_ }
"docker-compose.yml", "docker-compose.prod.yml" | ForEach-Object { New-Item -ItemType File -Name $_ }
# Kube
"namespace.yaml", "backend-deployment.yaml", "frontend-deployment.yaml", "redis-deployment.yaml", "postgres-deployment.yaml", "service.yaml", "ingress.yaml", "configmap.yaml" | ForEach-Object { New-Item -ItemType File -Path "kube" -Name $_ }
# Scripts
"build.sh", "deploy.sh", "test.sh", "backup.sh" | ForEach-Object { New-Item -ItemType File -Path "scripts" -Name $_ }
# Terraform
"main.tf", "variables.tf", "outputs.tf", "terraform.tfvars.example" | ForEach-Object { New-Item -ItemType File -Path "terraform" -Name $_ }
Set-Location ".."

# --- .github Structure ---
Set-Location ".github"
New-Item -ItemType Directory -Name "workflows"
"ci.yml", "cd.yml", "security.yml" | ForEach-Object { New-Item -ItemType File -Path "workflows" -Name $_ }
Set-Location ".."

# --- Docs Structure ---
Set-Location "docs"
"API.md", "ARCHITECTURE.md", "DEPLOYMENT.md", "CONTRIBUTING.md", "RESEARCH.md" | ForEach-Object { New-Item -ItemType File -Name $_ }
Set-Location ".."

Write-Host "Project structure for '$projectName' created successfully!"

