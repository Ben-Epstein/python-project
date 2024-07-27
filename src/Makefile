export PYTHONPATH = .venv

.PHONY: uv
uv:
	pip install uv==0.2.3
	uv venv

.PHONY: setup
setup:
	@if [ ! -d ".venv" ] || ! command -v uv > /dev/null; then \
		echo "UV not installed or .venv does not exist, running uv"; \
		make uv; \
	fi
	@if [ ! -f "requirements.dev.lock" ]; then \
		echo "Can't find lockfile. Locking"; \
		make lock; \
	fi
	uv pip install -r requirements.dev.lock
	uv pip install --no-deps -e .

.PHONY: lint
lint: setup
	uv tool --quiet run ruff check .
	uv tool --quiet run ruff format --check
	uv tool --quiet run mypy .

.PHONY: test
test: setup
	uv tool --quiet run pytest --cov-config=.coveragerc --cov=src --cov=test --cov-fail-under=85 --cov-branch

.PHONY: format
format: setup
	uv tool --quiet run ruff format .
	uv tool --quiet run ruff check --fix .

.PHONY: lock
lock:
	uv pip compile --output-file requirements.lock pyproject.toml --generate-hashes --quiet
	uv pip compile --output-file requirements.dev.lock pyproject.toml --generate-hashes --all-extras --quiet

.PHONY: sync
sync: lock setup
	uv pip sync requirements.dev.lock
	uv pip install --no-deps .

.PHONY: api
api: setup
	fastapi dev api/main.py 