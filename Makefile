.PHONY: run build format lint

run:
	docker-compose up -d

build:
	docker-compose build

format:
	ruff check --fix

lint:
	ruff check .
