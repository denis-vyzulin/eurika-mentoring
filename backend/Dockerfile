FROM python:3.8-alpine

ENV PYTHONUNBUFFERED 1
ARG PROJECT=evrika-mentoring

WORKDIR /$PROJECT

COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r /temp/requirements.txt

COPY . .

EXPOSE 8001
CMD ["python", "backend/manage.py", "runserver", "0.0.0.0:8001"]