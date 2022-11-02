docker-compose down
docker rm -f $(docker ps -a -q)
docker rmi -f $(docker images -q)
docker-compose build
docker-compose up -d
