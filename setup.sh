#!/bin/bash

set -e

INPUT=$1

if [ -z $INPUT ]; then
    echo "### Required arg to setup containers ==> 'dev' or 'deploy' ###"
    exit 1
fi

# dev container
if [ $INPUT == 'dev' ]; then
    IMG_NAME=deshrit/dev_ocr
    DEV_PORT=5002
    WORK_DIR=/ocr_rest_api
    CONTAINER_NAME=dev_ocr

    docker build -t $IMG_NAME -f Dockerfile.dev . && \
    docker run -it -p $DEV_PORT:$DEV_PORT -v `pwd`:$WORK_DIR --name $CONTAINER_NAME $IMG_NAME
    docker exec -it $CONTAINER_NAME /bin/bash
    exit
fi


# deploy container
if [ $INPUT == 'deploy' ]; then

    IMG_NAME=deshrit/ocr_rest_api
    DEPLOY_PORT=80
    WORK_DIR=/ocr_rest_api
    CONTAINER_NAME=ocr_rest_api

    docker build -t $IMG_NAME . && \
    docker run --rm -itd -p $DEPLOY_PORT:$DEPLOY_PORT --name $CONTAINER_NAME $IMG_NAME
    exit
fi