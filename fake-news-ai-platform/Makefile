.PHONY: build-backend build-frontend deploy-test deploy-prod test-backend test-frontend

build-backend:
	docker build -t yourrepo/backend:latest ./backend

build-frontend:
	docker build -t yourrepo/frontend:latest ./frontend

deploy-test:
	kubectl apply -f infrastructure/kube/

deploy-prod:
	sh infrastructure/scripts/deploy.sh

test-backend:
	pytest backend/app/tests

test-frontend:
	cd frontend && npm test -- --watchAll=false
