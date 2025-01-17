FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN pip cache purge

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]