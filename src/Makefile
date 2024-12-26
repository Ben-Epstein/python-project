export PYTHONPATH = .venv

.PHONY: uv
uv:
	pip install --upgrade 'uv>=0.5.6,<0.6'
	uv venv

.PHONY: setup
setup:
	@if [ ! -d ".venv" ] || ! command -v uv > /dev/null; then \
		echo "UV not installed or .venv does not exist, running uv"; \
		make uv; \
	fi
	@if [ ! -f "uv.lock" ]; then \
		echo "Can't find lockfile. Locking"; \
		uv lock; \
	fi
	uv sync --all-extras --all-groups
	uv pip install --no-deps -e .

.PHONY: format
format: setup
	uv --quiet run ruff format .
	uv --quiet run ruff check --fix .

.PHONY: lint
lint: setup
	uv --quiet run ruff check .
	uv --quiet run ruff format --check
	uv --quiet run mypy .

.PHONY: api
api: setup
	uv run fastapi dev api/main.py 
