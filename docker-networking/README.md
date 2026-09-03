# Docker Networking & Volumes Homework

This folder contains documentation, setup scripts, and theoretical write-ups for Docker Networking and Bind Mount Volumes.

---

## Task 1: Multi-Container Networking Setup

### Setup Commands & Network Isolation
```bash
# 1. Create 3 isolated Docker networks
docker network create frontend-net
docker network create backend-net
docker network create db-net

# 2. Deploy Frontend container on frontend-net
docker run -d --name frontend-app --network frontend-net nginx:alpine

# 3. Deploy Database container on db-net
docker run -d --name mysql-db --network db-net -e MYSQL_ROOT_PASSWORD=secret mysql:8.0

# 4. Deploy Backend container on backend-net
docker run -d --name backend-app --network backend-net alpine sleep 3600

# 5. Connect Backend container to both frontend-net and db-net
docker network connect frontend-net backend-app
docker network connect db-net backend-app

# 6. Verify Connectivity
# Backend can reach Frontend:
docker exec -it backend-app ping -c 2 frontend-app  # SUCCESS!

# Backend can reach Database:
docker exec -it backend-app ping -c 2 mysql-db      # SUCCESS!

# Frontend CANNOT reach Database directly (Network Isolation Enforcement):
docker exec -it frontend-app ping -c 2 mysql-db     # FAILED
```

---

## Task 2: Host Network Mode

```bash
# Pull and start Apache2 container directly on the host network driver
docker run -d --name apache-host --network host httpd:alpine

# Access web server directly on host port 80 without port mapping (-p)
curl http://localhost:80
```

---

## Task 3: Bind Mount & Dynamic Editing

```bash
# 1. Create a local folder and index.html file
mkdir -p ./bind_mount_data
echo "Hello students" > ./bind_mount_data/index.html

# 2. Launch Nginx container with bind mount attached
docker run -d --name nginx-bindmount -p 8084:80 \
  -v $(pwd)/bind_mount_data:/usr/share/nginx/html:ro nginx:alpine

# 3. Verify initial content
curl http://localhost:8084
# Output: Hello students

# 4. Dynamically modify host file without restarting container
echo "Hello students - Updated content live!" > ./bind_mount_data/index.html

# 5. Verify instant update
curl http://localhost:8084
# Output: Hello students - Updated content live!
```

---

## Task 4: Docker Overlay Networks

### Theoretical Architecture & Use Cases
* **Definition:** Docker Overlay Networks enable secure, multi-host communication across distributed Docker daemons without requiring OS-level routing configuration between container hosts.
* **Underlying Mechanism:**
  * **VXLAN Encapsulation:** Encapsulates Layer 2 Ethernet frames inside Layer 4 UDP packets (default port 4789).
  * **Control Plane:** Utilizes an in-memory Distributed Key-Value store and Serf/Raft gossip protocols (TCP/UDP port 7946) to discover container IPs across nodes.
  * **Routing Mesh:** Automatically distributes incoming requests on published service ports to active container instances on any node in a Docker Swarm cluster.
* **Primary Use Cases:**
  1. Microservices architecture deployed across multiple physical or cloud virtual machines.
  2. Production Docker Swarm and Kubernetes cluster inter-pod/inter-service networking.
  3. Encrypted cross-host container-to-container communication (`--opt encrypted`).
