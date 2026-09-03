# Docker Fundamentals Homework

This folder contains six complete Hello World web applications, each housed in its own folder with source code and Dockerfile.

---

## Folder Structure

```text
docker-fundamentals/
├── nodejs-app/       <- Node.js Express Hello World Application
├── python-app/       <- Python HTTP Hello World Application
├── java-app/         <- Java HTTP Hello World Application
├── Apache-app/       <- Apache Web Server Hello World Application
├── React-app/        <- React + Vite + Nginx Hello World Application
└── nginx-app/        <- Nginx Web Server Hello World Application
```

---

## Build & Run Instructions

### 1. Node.js App (`nodejs-app`)
```bash
cd nodejs-app
docker build -t nodejs-hello-app .
docker run -d -p 3000:3000 --name nodejs-container nodejs-hello-app
curl http://localhost:3000
```

### 2. Python App (`python-app`)
```bash
cd python-app
docker build -t python-hello-app .
docker run -d -p 5000:5000 --name python-container python-hello-app
curl http://localhost:5000
```

### 3. Java App (`java-app`)
```bash
cd java-app
docker build -t java-hello-app .
docker run -d -p 8080:8080 --name java-container java-hello-app
curl http://localhost:8080
```

### 4. Apache App (`Apache-app`)
```bash
cd Apache-app
docker build -t apache-hello-app .
docker run -d -p 8081:80 --name apache-container apache-hello-app
curl http://localhost:8081
```

### 5. React App (`React-app`)
```bash
cd React-app
docker build -t react-hello-app .
docker run -d -p 8082:80 --name react-container react-hello-app
curl http://localhost:8082
```

### 6. Nginx App (`nginx-app`)
```bash
cd nginx-app
docker build -t nginx-hello-app .
docker run -d -p 8083:80 --name nginx-container nginx-hello-app
curl http://localhost:8083
```
