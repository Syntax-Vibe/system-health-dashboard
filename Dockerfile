FROM python:3.10

WORKDIR /app
COPY backend/app.py .

RUN pip install flask psutil

EXPOSE 5000

CMD ["python", "app.py"]
