#!/bin/bash
# Docker Networking Setup Helper Script

echo "1. Creating 3 Docker networks..."
docker network create frontend-net
docker network create backend-net
docker network create db-net

echo "2. Running containers..."
docker run -d --name frontend-app --network frontend-net nginx:alpine
docker run -d --name mysql-db --network db-net -e MYSQL_ROOT_PASSWORD=secret mysql:8.0
docker run -d --name backend-app --network backend-net alpine sleep 3600

echo "3. Connecting backend to frontend-net and db-net..."
docker network connect frontend-net backend-app
docker network connect db-net backend-app

echo "4. Testing connectivity..."
docker exec -it backend-app ping -c 2 frontend-app
docker exec -it backend-app ping -c 2 mysql-db

echo "Networking setup test complete!"
