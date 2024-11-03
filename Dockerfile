FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt upgrade
RUN apt install portaudio19-dev
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "ai.py"]

