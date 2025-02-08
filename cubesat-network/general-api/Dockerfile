FROM python:3.12-slim

WORKDIR /usr/src/general-api

COPY requirements.txt ./

RUN apt-get update && apt-get install -y \
    libxi6 \
    libgconf-2-4 \
    cron \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt


COPY . .

EXPOSE 5500

CMD ["sh", "-c", "[ -f common/data/data.db ] || python common/migration.py && gunicorn --config gunicorn_config.py app:app | tee -a /usr/src/general-api/common/logs/general-api.log"]
