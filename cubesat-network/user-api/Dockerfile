FROM python:3.12-slim

WORKDIR /usr/src/user-api

RUN apt-get update && apt-get install -y \
    libsqlite3-dev \
    build-essential \
    gcc \
    make \
    python3-dev \
    libssl-dev \
    libsqlcipher-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Ensure migration runs only if the database is not initialized
CMD ["sh", "-c", "[ -f common/data/private.db ] || python common/migration.py && gunicorn --config gunicorn_config.py app:app | tee -a /usr/src/user-api/common/logs/user-api.log"]
