FROM debian:buster-20230208

docker build -t debian-juan .
docker image tag debian-juan juanluiscc/debian-juan:latest
