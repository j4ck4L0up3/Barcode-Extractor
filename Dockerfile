FROM python:3.13.4-alpine3.22

WORKDIR /src/app

ENV PYTHONUNBUFFERED=1

RUN apk update &&\
apk add chromium-chromedriver

# install packages
RUN ["pip", "install", "selenium"]
RUN ["pip", "install", "beautifulsoup4"]
#RUN ["pip", "install", "webdriver-manager"]

# add barcode name data to image
COPY qry_barcode_names.txt /src/app

COPY *.py /src/app

CMD ["python3", "-u", "barcode_extractor.py"]