FROM python:3.8-slim

COPY ./requirements.txt .
RUN pip install -r ./requirements.txt --no-cache-dir

RUN mkdir /app
COPY ./app /app
WORKDIR /app

#ENV DB_NAME postgres
#ENV DB_PORT 5432
#ENV POSTGRES_USER postgres
#ENV POSTGRES_PASSWORD example
#ENV DB_HOST db


ENTRYPOINT ["python", "main.py"]