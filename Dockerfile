FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

# run updatea dn awscli command

RUN apt update -y && apt install awscli -y

RUN pip install -r requirements.txt

CMD [ "python3", "app.py" ]