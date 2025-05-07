FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY src/ ./src/
COPY .env .   # HUOM: Tuotannossa käytä environment variableja!

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/weather.py"]