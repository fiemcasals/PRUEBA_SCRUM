FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/ /app/

EXPOSE 8003

CMD ["sh", "-c", "python manage.py migrate && python manage.py seed_users && python manage.py runserver 0.0.0.0:8003"]
