# Docker Fundamentals Homework

This folder contains six complete Hello World web applications, each housed in its own folder with source code, Dockerfile, and verification screenshot.

---

## Verified Screenshot Evidence

### 1. Node.js Express Application (Port 3000)
![Node.js App Screenshot](./screenshots/nodejs_app_screenshot.png)

### 2. Python Web Application (Port 5000)
![Python App Screenshot](./screenshots/python_app_screenshot.png)

### 3. Java Web Application (Port 8080)
![Java App Screenshot](./screenshots/java_app_screenshot.png)

### 4. Apache Web Server Application (Port 8081)
![Apache App Screenshot](./screenshots/apache_app_screenshot.png)

### 5. React Web Application (Port 8082)
![React App Screenshot](./screenshots/react_app_screenshot.png)

### 6. Nginx Web Server Application (Port 8083)
![Nginx App Screenshot](./screenshots/nginx_app_screenshot.png)

---

## Build & Run Instructions

```bash
# Node.js
cd nodejs-app && docker build -t nodejs-app . && docker run -d -p 3000:3000 nodejs-app

# Python
cd python-app && docker build -t python-app . && docker run -d -p 5000:5000 python-app

# Java
cd java-app && docker build -t java-app . && docker run -d -p 8080:8080 java-app

# Apache
cd Apache-app && docker build -t apache-app . && docker run -d -p 8081:80 apache-app

# React
cd React-app && docker build -t react-app . && docker run -d -p 8082:80 react-app

# Nginx
cd nginx-app && docker build -t nginx-app . && docker run -d -p 8083:80 nginx-app
```
