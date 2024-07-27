FROM python:3.12.3-alpine3.20

COPY requirements.lock pyproject.toml /

RUN python -m venv .venv && source .venv/bin/activate &&\
    pip install --no-cache-dir -r requirements.lock && \
    source .venv/bin/activate

EXPOSE 8000

ENV PATH="/.venv/bin:$PATH"
ENV LOCALHOST="host.docker.internal"

COPY api /api

ENTRYPOINT ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]