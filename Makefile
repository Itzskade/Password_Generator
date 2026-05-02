.PHONY: clean run test lint install

run:
	python3 -m main

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +

test:
	pytest -q

lint:
	flake8 .

install:
	pip install -r requirements.txt