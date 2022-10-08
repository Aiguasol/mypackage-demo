FROM python:3.10.2-slim-bullseye as base

ARG PIPX_VERSION=1.1.0 POETRY_VERSION=1.2.0 POETRY_HTTP_BASIC_AIGUASOL_USERNAME POETRY_HTTP_BASIC_AIGUASOL_PASSWORD


ENV PYTHONFAULTHANDLER=1 \
	PYTHONUNBUFFERED=1 \
	PYTHONHASHSEED=random \
	PYTHONDONTWRITEBYTECODE=1 \
	# pip:
	PIP_NO_CACHE_DIR=off \
	PIP_DISABLE_PIP_VERSION_CHECK=on \
	PIP_DEFAULT_TIMEOUT=100 \
	# poetry:
	POETRY_NO_INTERACTION=1 \
	POETRY_VERSION=$POETRY_VERSION \
	# pipx:
	PATH=/opt/pipx/bin:/src/.venv/bin:$PATH \
	PIPX_BIN_DIR=/opt/pipx/bin \
	PIPX_HOME=/opt/pipx/home \
	PIPX_VERSION=$PIPX_VERSION \
	# python:
	PYTHONPATH=/src \
	POETRY_HTTP_BASIC_AIGUASOL_USERNAME=$POETRY_HTTP_BASIC_AIGUASOL_USERNAME \
	POETRY_HTTP_BASIC_AIGUASOL_PASSWORD=$POETRY_HTTP_BASIC_AIGUASOL_PASSWORD


WORKDIR /src

RUN apt-get update -qy && \
	apt-get install -qy --no-install-recommends gcc libc-dev make wget git curl && \
	python -m pip install --no-cache-dir --upgrade pip "pipx==$PIPX_VERSION" && \
	pipx install "poetry==$POETRY_VERSION" 

# install dependencies
COPY poetry.lock poetry.toml pyproject.toml /src/
RUN poetry install --only main --no-interaction --no-root

# copy and run program
COPY mypackage /src/mypackage

# install package
RUN poetry install --only main --no-interaction

# leave container up
CMD ["tail", "-f", "/dev/null"]
