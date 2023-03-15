.PHONY: all install venv run

.PHONY: cluster
cluster: ## Create a Kubernetes cluster
	$(info Creating Kubernetes cluster with a registry...)
	k3d cluster create --registry-create cluster-registry:0.0.0.0:32000 --port '8080:80@loadbalancer'

.PHONY: build
build: ## Build a Docker image
	$(info Building Docker image...)
	docker build --rm --pull --tag accounts:1.0 . 

.PHONY: push
push: ## Push image to K3d registry
	$(info Pushing Docker image to K3D registry...)
	docker tag accounts:1.0 localhost:32000/accounts:1.0
	docker push localhost:32000/accounts:1.0

venv: ## Create a Python virtual environment
	$(info Creating Python 3 virtual environment...)
	python3 -m venv ~/venv

install: ## Install Python dependencies
	$(info Installing dependencies...)
	python3 -m pip install --upgrade pip wheel
	pip install -r requirements.txt
		
lint: ## Run the linter
	$(info Running linting...)
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 . --count --max-complexity=10 --max-line-length=127 --statistics

.PHONY: tests
tests: ## Run the unit tests
	$(info Running tests...)
	nosetests -vv --with-spec --spec-color --with-coverage --cover-package=service
