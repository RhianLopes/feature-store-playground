FROM python:3.11-slim

RUN pip install --no-cache-dir uv

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

ENV PATH="/app/.venv/bin:${PATH}"

WORKDIR /app/feature_repo
