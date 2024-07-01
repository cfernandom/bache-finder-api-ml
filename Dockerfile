FROM python:3.10-slim

WORKDIR /bache-finder-ml-model

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        pkg-config \
        libhdf5-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN addgroup --system pythongroup && \
    adduser --system --ingroup pythongroup pythonuser && \
    chown -R pythonuser:pythongroup /bache-finder-ml-model
USER pythonuser

CMD ["python", "main.py"]