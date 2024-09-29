FROM python:3.12.0

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -v -r requirements.txt

CMD ["python", "main.py"]
