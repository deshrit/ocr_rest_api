FROM ubuntu

RUN apt update && \ 
    apt install python3 \
                python3-pip \
                tesseract-ocr \
                tesseract-ocr-fra \
                tesseract-ocr-spa -y

WORKDIR /ocr_rest_api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "gunicorn", "-b", "0.0.0.0:80", "app:create_app()" ]