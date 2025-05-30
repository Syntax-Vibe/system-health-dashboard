FROM python:3.10

WORKDIR /app

# 👇 این خط کل پوشه backend رو کپی می‌کنه شامل app.py و frontend/index.html
COPY backend /app

RUN pip install flask psutil

EXPOSE 5000

CMD ["python", "app.py"]
