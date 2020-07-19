#!make
.PHONY: test venv
# include ./.env
# export

# make headline colorful
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"


poetry-env:
	pyenv local 3.7.4
	poetry install
	ln -sf $(sh poetry env info -p) venv

run:
	@echo $(TAG)Running app$(END)
	poetry run python app.py

lint:
	@echo $(TAG)Running Lint$(END)
	poetry run flake8 kafka_consumer app.py --count --ignore=E501,E126

test:
	@echo $(TAG)Running Unit Test$(END)
	poetry run pytest tests
