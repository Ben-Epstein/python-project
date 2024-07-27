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
	@if [ ! -f "requirements.dev.lock" ] || [ ! -f "requirements-lowest.lock" ]; then \
		echo "Can't find lockfile. Locking"; \
		make lock; \
	fi
	uv pip install -r $(if $(lowest),requirements-lowest.lock,requirements.dev.lock)
	uv pip install --no-deps -e .

.PHONY: setup-lowest
setup-lowest:
	make setup lowest=1

.PHONY: lint
lint: setup
	uv --quiet run ruff check .
	uv --quiet run ruff format --check
	uv --quiet run mypy .

.PHONY: test
test:
	uv --quiet run pytest tests --cov=api --cov=tests --cov-fail-under=85 --cov-branch tests

.PHONY: format
format: setup
	uv --quiet run ruff format .
	uv --quiet run ruff check --fix .

.PHONY: lock
lock:
	uv pip compile --output-file requirements.lock pyproject.toml --generate-hashes --quiet
	uv pip compile --output-file requirements.dev.lock pyproject.toml --generate-hashes --all-extras --quiet
	uv pip compile --resolution=lowest --output-file requirements-lowest.lock pyproject.toml --generate-hashes --all-extras --quiet


.PHONY: sync
sync: lock setup
	uv pip sync $(if $(lowest),requirements-lowest.lock,requirements.dev.lock)
	uv pip install --no-deps .

.PHONY: sync-lowest
sync-lowest: lock setup-lowest
	make sync lowest=1

.PHONY: api
api: setup
	fastapi dev api/main.py 