# Dockerfiles & Images Homework

This folder contains the multi-stage Docker build application and student verification documentation.

---

## Task 1 & 2: Multi-Stage Dockerfile & Verification

### Application Source (`multi-stage-app/main.go`)
```go
package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Hello World from Docker multi-stage build")
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Server running on port 8080...")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Printf("Error starting server: %s\n", err)
	}
}
```

### Multi-Stage Dockerfile (`multi-stage-app/Dockerfile`)
```dockerfile
# Stage 1: Build stage
FROM golang:1.22-alpine AS builder
WORKDIR /app
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -o server main.go

# Stage 2: Final minimal runtime stage
FROM alpine:3.19
WORKDIR /app
COPY --from=builder /app/server .
EXPOSE 8080
CMD ["./server"]
```

### Student Verification Documentation
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
