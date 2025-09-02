FROM python:3.12-slim-bookworm

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

COPY ./core /app

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
