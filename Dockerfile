FROM python:3-slim-bookworm AS app
WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir gunicorn
EXPOSE 80

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80", "--workers=4"]
