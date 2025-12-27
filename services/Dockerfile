# Dockerfile for production mode

#
# ---------------------------------------------------------
#
FROM python:3.12-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_DIR=/opt/poetry \
    SERVICE_CORE_DIR=/home/services

#
# ---------------------------------------------------------
#
FROM base AS poetry

WORKDIR $POETRY_DIR

COPY ./poetry.lock ./pyproject.toml $POETRY_DIR/

RUN pip install --timeout=100 poetry -U \
    && pip install --timeout=100 poetry-plugin-export -U \
    && poetry export --without-hashes --without dev -f requirements.txt -o requirements.txt

#
# ---------------------------------------------------------
#
FROM base AS deps

WORKDIR $SERVICE_CORE_DIR

COPY deploy/pre-install.sh ./

RUN chmod a+x $SERVICE_CORE_DIR/pre-install.sh && $SERVICE_CORE_DIR/pre-install.sh

COPY --from=poetry $POETRY_DIR/requirements.txt $SERVICE_CORE_DIR/

RUN pip install --no-cache-dir --timeout=100 -r requirements.txt

#
# ---------------------------------------------------------
#
FROM base AS runner

USER root

WORKDIR $SERVICE_CORE_DIR

COPY deploy/pre-install.sh ./

RUN chmod a+x $SERVICE_CORE_DIR/pre-install.sh && $SERVICE_CORE_DIR/pre-install.sh

COPY --from=deps /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=deps /usr/local/bin/ /usr/local/bin/

COPY deploy/gunicorn.sh \
     deploy/migrations.sh \
     deploy/tests.sh \
     deploy/gunicorn.conf.py \
     ./

COPY . $SERVICE_CORE_DIR/

EXPOSE 5000

RUN chmod a+x $SERVICE_CORE_DIR/migrations.sh \
              $SERVICE_CORE_DIR/gunicorn.sh \
              $SERVICE_CORE_DIR/tests.sh