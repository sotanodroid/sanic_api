FROM python:3.6

ENV  PYTHONUNBUFFERED 1


RUN pip install --upgrade pip && \
    pip install -U setuptools pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY ./ /application
WORKDIR /application

CMD ["python", "-m", "app"]
