#!/bin/sh

DOCKER_TAG=pythonstockleeks/pythonstockleeks:latest

echo " docker build -f Dockerfile -t ${DOCKER_TAG} ."
docker build -f Dockerfile -t ${DOCKER_TAG} .
echo "#################################################################"
echo " docker push ${DOCKER_TAG} "

