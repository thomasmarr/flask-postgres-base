FROM python:3.8.0-alpine3.10

RUN adduser -D flaskapp

WORKDIR /home/flaskapp

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY flaskapp flaskapp
COPY run.py config.py start.sh ./
RUN chmod +x start.sh

ENV FLASK_APP run.py

RUN chown -R flaskapp:flaskapp ./
USER flaskapp

ENTRYPOINT ["./start.sh"]
EXPOSE 5000