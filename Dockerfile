FROM debian:buster-20230208

docker build -t debian-juan .
docker image tag debian-juan USER/debian-juan:latest
