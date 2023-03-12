FROM python:3.10-bullseye

WORKDIR /app/
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./
RUN python manage.py collectstatic --noinput

ENTRYPOINT ["./run.sh"]