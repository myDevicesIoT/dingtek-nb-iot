FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

CMD [ "python3", "NB_Server_Gateway.py", "--log=DEBUG"]
