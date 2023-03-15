install: ## Install Python dependencies
	$(info Installing dependencies...)
	python3 -m pip install --upgrade pip wheel &&\
		pip install -r requirements.txt
		
test:
	python -m pytest -vv test_hello.py

format:
	black *.py


lint:
	pylint --disable=R,C hello.py

all: install lint test
