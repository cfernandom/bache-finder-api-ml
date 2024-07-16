FROM python:3.10-slim

WORKDIR /bache-finder-ml-api

RUN apt-get update && \
    apt-get install -y \
        pkg-config \
        libhdf5-dev \
        gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN addgroup --system pythongroup && \
    adduser --system --ingroup pythongroup pythonuser && \
    chown -R pythonuser:pythongroup /bache-finder-ml-api
USER pythonuser

CMD ["python", "main.py"]
