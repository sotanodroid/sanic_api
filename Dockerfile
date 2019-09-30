FROM python:3.6-alpine

ARG BUILD_PACKAGES="postgresql-dev"
ARG BUILD_DEPS="gcc musl-dev"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    PIPENV_HIDE_EMOJIS=true \
    PIPENV_COLORBLIND=true \
    PIPENV_NOSPIN=true \
    PIPENV_DOTENV_LOCATION=.env 

RUN set -ex && \
    apk add --update --no-cache $BUILD_PACKAGES 

COPY Pipfile Pipfile.lock ./

RUN set -ex && \
    apk add --update --no-cache --virtual .build-deps $BUILD_DEPS && \
    pip install pipenv && \
    pipenv install --deploy --system --ignore-pipfile && \
    pip uninstall -y pipenv virtualenv virtualenv-clone && \
    apk del --no-cache .build-deps

WORKDIR /application

COPY . .

CMD python -m app
