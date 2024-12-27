FROM python:latest

RUN pip install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8000"]