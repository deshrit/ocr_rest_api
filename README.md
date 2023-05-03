# OCR-REST-API
Endpoints return OCR of image files.
Using google's tesseract OCR engine - [here](https://github.com/tesseract-ocr/tesseract).
Images files maybe in 3 different languages,
seperate endpoint for each language

    1. english - eng 
    2. french - fra
    3. spanish - spa 

# TRY
[LIVE](https://ocr-rest-api.azurewebsites.net/api/v1/docs/)

(use 'https' scheme for swagger)

# To run locally
**1. MUST HAVE DOCKER INSTALLED**

`git clone git@github.com:deshrit/ocr_rest_api.git`

`cd ocr_rest_api`

`./setup.sh dev`

**2. TO VISIT ENDPOINT LOCALLY**

`http://127.0.0.1:5002/api/v1/docs`