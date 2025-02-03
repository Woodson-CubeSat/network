FROM python:3.12-slim

WORKDIR /usr/src/central-webserver

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Add startup script
COPY startup.sh /usr/src/startup.sh
RUN chmod +x /usr/src/startup.sh

EXPOSE 3000

CMD ["sh", "-c", "/usr/src/startup.sh | tee -a /usr/src/central-webserver/common/logs/webserver.log"]

