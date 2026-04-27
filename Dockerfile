FROM dh-mirror.gitverse.ru/python:3.10-slim

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    dos2unix \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

RUN dos2unix /app/entrypoint.sh

RUN mkdir -p /app/results

COPY results/test.json /app/results/test.json

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

CMD ["python", "inference_atlanta_net.py"]
