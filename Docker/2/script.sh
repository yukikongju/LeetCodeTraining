#!/bin/sh

# build image
docker build -t testimage .

# run image with environment variable
docker run -e myhost=host1 testimage

# run image without environment variable. use default if set as ENV in Dockerfile
docker run testimage

# removing docker image
docker rmi testimage:latest
docker images
