FROM python:3.10-bullseye

WORKDIR /app/
ARG RUN_ENV
COPY requirements/ ./requirements
RUN pip install -r ./requirements/${RUN_ENV}.txt
COPY ./ ./
RUN python manage.py collectstatic --noinput

ENTRYPOINT ["./run.sh"]