FROM python:3.11.6-slim


RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    build-essential \
    libmagic-dev \
    libgl1 \ 
    libreoffice \
    pandoc \
    poppler-utils \
    tesseract-ocr \
    libtesseract-dev \
    tesseract-ocr-rus

WORKDIR /code

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app ./app
