FROM python:3.9

WORKDIR /app

        COPY requirements.txt config.env .
        RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "-m", "bot"]
