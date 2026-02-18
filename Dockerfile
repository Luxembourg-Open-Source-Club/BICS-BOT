FROM python:3.12-bookworm

COPY . /bot
WORKDIR /bot

RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]

