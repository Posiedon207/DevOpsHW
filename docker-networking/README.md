# Docker Networking & Volumes Homework

This folder contains my tasks and screenshots for Docker Networking and Bind Mount Volumes.

---

## Task 1: Multi-Container Networking

### Steps Executed
1. Created 3 separate Docker networks: `frontend-net`, `backend-net`, and `db-net`.
2. Created 3 containers:
   * `frontend-app` on `frontend-net`
   * `backend-app` on `backend-net`
   * `mysql-db` on `db-net`
3. Connected the backend container to both `frontend-net` and `db-net`:
   ```bash
   docker network connect frontend-net backend-app
   docker network connect db-net backend-app
   ```
4. Tested connectivity:
   * `backend-app` can ping `frontend-app` and `mysql-db` (Success).
   * `frontend-app` cannot directly reach `mysql-db` (Network isolation verified).

---

## Task 2: Host Network

Ran an Apache web server using host network mode so it binds directly to port 80 of the host machine:
```bash
docker run -d --name apache-host --network host httpd:alpine
curl http://localhost:80
```

---

## Task 3: Bind Mount & Dynamic Editing

1. Created a local folder `./bind_mount_data` and an `index.html` file with content `"Hello students"`.
2. Started an Nginx container mounting this folder to `/usr/share/nginx/html`:
   ```bash
   docker run -d --name nginx-bindmount -p 8084:80 -v $(pwd)/bind_mount_data:/usr/share/nginx/html nginx:alpine
   ```
3. Modified `index.html` on the host machine to `"Hello students - Updated content live!"`.
4. Verified that the website content updated immediately without restarting the container.

---

## Task 4: Docker Overlay Networks

### What I Learned
* **Definition:** Docker Overlay Networks are used in multi-host setups (like Docker Swarm) to allow containers running on different physical or virtual host machines to communicate securely.
* **Use Cases:** Microservices spread across multiple cloud instances or Swarm cluster nodes.

---

## Screenshots

### 1. Multi-Container Networking & Connectivity
![Container Networking Screenshot](./screenshots/docker_container_networking.png)

### 2. Bind Mount Live Editing
![Bind Mount Screenshot](./screenshots/docker_bind_mount.png)
