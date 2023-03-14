install: ## Install Python dependencies
	$(info Installing dependencies...)
	python3 -m pip install --upgrade pip wheel &&\
		pip install -r requirements.txt