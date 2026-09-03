# Dockerfiles & Images Homework

This folder contains the multi-stage Docker build application, student details, and verification screenshots.

---

## Verification Screenshot Evidence

### 1. Web Browser Response (Port 8080)
![Multi Stage App Browser Screenshot](./screenshots/multistage_app_screenshot.png)

### 2. `docker ps` Terminal Status Verification
![Docker PS Port 8080 Verification Screenshot](./screenshots/docker_ps_port8080.png)

---

## Task 1 & 2: Multi-Stage Dockerfile & Verification

### Student Documentation
* **Student Name:** posiedon2212
* **Enrollment Number:** DEV-HW-2026
* **Application Response Verification:**
  ```bash
  $ curl http://localhost:8080
  Hello World from Docker multi-stage build
  ```
* **`docker ps` Output Showing Container Running on Port 8080:**
  ```text
  CONTAINER ID   IMAGE                 COMMAND      CREATED         STATUS         PORTS                    NAMES
  e9a82f1b4c3d   multistage-hello-app  "./server"   12 minutes ago  Up 12 minutes  0.0.0.0:8080->8080/tcp   go-multistage-container
  ```

---

## Task 3: Docker Application Deployment
The table below documents three distinct production-ready Docker application deployments created and tested in this project:

| App Type | Runtime Base Image | Container Port | Exposed Host Port | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Node.js Express** | `node:18-alpine` | 3000 | 3000 | Verified |
| **Python HTTP** | `python:3.11-slim` | 5000 | 5000 | Verified |
| **Java JDK/JRE** | `eclipse-temurin:17-jre-alpine` | 8080 | 8080 | Verified |
