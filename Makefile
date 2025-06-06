.DEFAULT_GOAL := help

# ---------------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------------
VENV       := .venv
DEV        ?= 1
REQUIREMENTS := requirements.txt
ifeq ($(DEV),1)
	REQUIREMENTS := requirements-dev.txt
endif

# ---------------------------------------------------------------------------------
# Platform Detection
# ---------------------------------------------------------------------------------
ifeq ($(OS),Windows_NT)
	BIN        := $(VENV)/Scripts
	EXEC_EXT   := .exe
	SHELL      := cmd.exe
	SHELLFLAGS := /C
	IS_WINDOWS := 1
else
	BIN        := $(VENV)/bin
	EXEC_EXT   :=
	IS_WINDOWS := 0
endif

# ---------------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------------
PYTHON := $(BIN)/python$(EXEC_EXT)
PIP    := $(BIN)/pip$(EXEC_EXT)
PYTEST := $(BIN)/pytest$(EXEC_EXT)
RUFF   := $(BIN)/ruff$(EXEC_EXT)
BLACK  := $(BIN)/black$(EXEC_EXT)

# ---------------------------------------------------------------------------------
# Targets
# ---------------------------------------------------------------------------------
help:
	@echo ========================================================================================================================
	@echo "                                                    Help                                                              "
	@echo ========================================================================================================================
	@echo ------------------------------------------------------------------------------------------------------------------------
	@echo "USAGE : make [target]"
	@echo ------------------------------------------------------------------------------------------------------------------------
	@echo "EXAMPLE : make setup (Set up virtualenv with dev dependencies)"
	@echo ------------------------------------------------------------------------------------------------------------------------
	@echo "TARGETS: "
	@echo "  setup        Create virtual environment and install dependencies (DEV=0 for standard dependencies)"
	@echo "  format       Run formatter"
	@echo "  lint         Run linter with autofix"
	@echo "  test         Run tests"
	@echo "  quality      Run format, lint, and test together"
	@echo "  build        Build the package"
	@echo "  reset        Remove the virtual environment"
	@echo "  release      Tag and push a new release"
	@echo "  help         Show this help message"

setup:
	@echo ========================================================================================================================
	@echo "                                                Setting Up                                                            "
	@echo ========================================================================================================================
ifeq ($(IS_WINDOWS),1)
	@if not exist "$(VENV)" ( \
		echo Creating virtual environment... && \
		python -m venv $(VENV) \
	) else ( \
		echo Virtual environment already exists at $(VENV) \
	)
else
	@if [ ! -d "$(VENV)" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv $(VENV); \
	else \
		echo "Virtual environment already exists at $(VENV)"; \
	fi
endif
	"$(PYTHON)" -m pip install --upgrade pip
	@echo Installing dependencies from $(REQUIREMENTS)...
	"$(PYTHON)" -m pip install -r $(REQUIREMENTS)
	
ifeq ($(DEV),1)
	@echo Installing Git pre-commit hooks...
	"$(PYTHON)" -m pre_commit install
endif

format:
	@echo ========================================================================================================================
	@echo "                                            Formatting Code                                                           "
	@echo ========================================================================================================================
ifeq ($(IS_WINDOWS),1)
	@if exist "$(BLACK)" ( \
		"$(BLACK)" src/ \
	) else ( \
		echo WARNING: black not found. Run 'make setup' first. \
	)
else
	@if [ -x "$(BLACK)" ]; then \
		"$(BLACK)" src/ ; \
	else \
		echo "WARNING: black not found. Run 'make setup' first."; \
	fi
endif

lint:
	@echo ========================================================================================================================
	@echo "                                              Linting Code                                                            "
	@echo ========================================================================================================================
ifeq ($(IS_WINDOWS),1)
	@if exist "$(RUFF)" ( \
		"$(RUFF)" check src/ --fix --show-files \
	) else ( \
		echo WARNING: ruff not found. Run 'make setup' first. \
	)
else
	@if [ -x "$(RUFF)" ]; then \
		"$(RUFF)" check src/ --fix --show-files; \
	else \
		echo "WARNING: ruff not found. Run 'make setup' first."; \
	fi
endif

test:
	@echo ========================================================================================================================
	@echo "                                              Testing Code                                                            "
	@echo ========================================================================================================================
ifeq ($(IS_WINDOWS),1)
	@if exist "$(PYTEST)" ( \
		"$(PYTEST)" \
	) else ( \
		echo WARNING: pytest not found. Run 'make setup' first. \
	)
else
	@if [ -x "$(PYTEST)" ]; then \
		"$(PYTEST)" ; \
	else \
		echo "WARNING: pytest not found. Run 'make setup' first."; \
	fi
endif

quality: format lint test

build:
	@echo ========================================================================================================================
	@echo "                                               Building                                                               "
	@echo ========================================================================================================================
	"$(PYTHON)" -m build

reset:
	@echo ========================================================================================================================
	@echo "                                          Resetting Environment                                                       "
	@echo ========================================================================================================================
ifeq ($(IS_WINDOWS),1)
	@if exist "$(VENV)" ( \
		echo Removing virtual environment at $(VENV)... && \
		rmdir /S /Q "$(VENV)" \
	) else ( \
		echo No virtual environment found to remove. \
	)
else
	@if [ -d "$(VENV)" ]; then \
		echo "Removing virtual environment at $(VENV)..."; \
		rm -rf "$(VENV)"; \
	else \
		echo "No virtual environment found to remove."; \
	fi
endif

release:
	@echo ========================================================================================================================
	@echo "                                            Creating Release                                                          "
	@echo ========================================================================================================================
	"$(PYTHON)" scripts/release.py

.PHONY: help setup test lint format quality build reset release
