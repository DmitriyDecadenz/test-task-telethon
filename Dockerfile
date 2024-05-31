FROM python:3.12-slim

RUN mkdir app
WORKDIR app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
COPY . .

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.main:app", "--bind", "0.0.0.0:8000"]