# ===== CONFIG =====
APP_NAME=video-kiosk
VENV=venv
PYTHON=python3
PIP=$(VENV)/bin/pip
PY=$(VENV)/bin/python

# ===== DEFAULT =====
.PHONY: help
help:
	@echo "Comandos disponíveis:"
	@echo "  make setup   - Cria virtualenv e instala dependências"
	@echo "  make run     - Executa a aplicação"
	@echo "  make clean   - Remove o virtualenv"
	@echo "  make deps    - Instala dependências do sistema"

# ===== SYSTEM DEPS =====
.PHONY: deps
deps:
	sudo apt update
	sudo apt install -y mpv python3-full python3-venv

# ===== VENV SETUP =====
.PHONY: setup
setup: $(VENV)/bin/activate

$(VENV)/bin/activate:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install keyboard
	@touch $(VENV)/bin/activate

# ===== RUN =====
.PHONY: run
run:
	sudo $(PY) main.py

# ===== CLEAN =====
.PHONY: clean
clean:
	rm -rf $(VENV)
