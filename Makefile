-include .env
export

lint:
	@mypy frontend
	@flake8 frontend

dev.install:
	@poetry install

run:
	@python -m frontend