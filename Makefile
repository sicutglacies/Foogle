.PHONY: run build stop format lint

run:
	docker-compose up -d

build:
	docker-compose build

stop:
	docker-compose down

format:
	ruff check --fix

lint:
	ruff check .
