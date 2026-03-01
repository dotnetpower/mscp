PYTHON ?= python3
VENV_DIR ?= .venv

.PHONY: help venv install check-env lint run clean

help:
	@echo "Targets: venv, install, check-env, lint, run, clean"

venv:
	$(PYTHON) -m venv $(VENV_DIR)

install: venv
	$(VENV_DIR)/bin/pip install -r requirements.txt

check-env:
	@test -n "$$AZURE_OPENAI_ENDPOINT" || (echo "Missing AZURE_OPENAI_ENDPOINT" && exit 1)
	@test -n "$$AZURE_OPENAI_API_KEY" || (echo "Missing AZURE_OPENAI_API_KEY" && exit 1)
	@test -n "$$AZURE_OPENAI_DEPLOYMENT" || (echo "Missing AZURE_OPENAI_DEPLOYMENT" && exit 1)

lint:
	$(VENV_DIR)/bin/python -m py_compile app.py

run: check-env
	$(VENV_DIR)/bin/python app.py

clean:
	rm -rf $(VENV_DIR)
