FROM python:3.10-alpine
WORKDIR /app
COPY app.py .
RUN pip install flask --no-cache-dir flask
CMD ["python","app.py"]