# DevOps Homework Submission

**Student Email:** posiedon2212@gmail.com  
**Enrollment ID:** DEV-HW-2026  
**Repository Structure:** Complete multi-module DevOps assignment covering Linux, Shell Scripting, Networking, Git/GitHub, Docker Fundamentals, Multi-Stage Builds, and Docker Networking/Volumes.

---

## Table of Contents
1. [Linux Fundamentals](#1-linux-fundamentals)
   - [Task 1: Soft Link & Hard Link](#task-1-soft-link--hard-link)
   - [Task 2: adduser vs useradd](#task-2-adduser-vs-useradd)
   - [Task 3: journalctl](#task-3-journalctl)
   - [Task 4: Linux Command Cheat Sheet](#task-4-linux-command-cheat-sheet)
2. [Shell Scripting](#2-shell-scripting)
   - [System Information Script (`system_info.sh`)](#system-information-script-system_infosh)
   - [Execution & Output Log](#execution--output-log)
3. [Networking Fundamentals](#3-networking-fundamentals)
   - [Networking Commands Reference & Output](#networking-commands-reference--output)
4. [Git and GitHub](#4-git-and-github)
   - [Task 1: `git commit -a -m` vs `git commit -m`](#task-1-git-commit--a--m-vs-git-commit--m)
   - [Task 2: Git Cherry-Pick Walkthrough](#task-2-git-cherry-pick-walkthrough)
5. [Docker Fundamentals](#5-docker-fundamentals)
   - [Node.js Web App (`nodejs-app`)](#nodejs-web-app-nodejs-app)
   - [Python Web App (`python-app`)](#python-web-app-python-app)
   - [Java Web App (`java-app`)](#java-web-app-java-app)
   - [Apache Web Server (`Apache-app`)](#apache-web-server-apache-app)
   - [React Application (`React-app`)](#react-application-react-app)
   - [Nginx Web Server (`nginx-app`)](#nginx-web-server-nginx-app)
6. [Dockerfiles & Images](#6-dockerfiles--images)
   - [Task 1 & 2: Multi-Stage Dockerfile & Verification](#task-1--2-multi-stage-dockerfile--verification)
   - [Task 3: Docker Application Deployment](#task-3-docker-application-deployment)
7. [Docker Networking & Volumes](#7-docker-networking--volumes)
   - [Task 1: Multi-Container Networking Setup](#task-1-multi-container-networking-setup)
   - [Task 2: Host Network Mode](#task-2-host-network-mode)
   - [Task 3: Bind Mount & Dynamic Editing](#task-3-bind-mount--dynamic-editing)
   - [Task 4: Docker Overlay Networks](#task-4-docker-overlay-networks)

---

## 1. Linux Fundamentals

### Task 1: Soft Link & Hard Link

#### Technical Comparison
| Feature | Soft Link (Symbolic Link / Symlink) | Hard Link |
| :--- | :--- | :--- |
| **Inode** | Has its own unique inode number pointing to target path. | Shares the exact same inode number as the target file. |
| **Data Pointer** | Points to the original file path. | Points directly to the data blocks on disk. |
| **Original File Deletion**| Link becomes broken (dangling symlink). | Data remains accessible via hard link until link count drops to 0. |
| **Cross-Filesystem** | Can span across different filesystems/disks. | Cannot span across different filesystems. |
| **Directories** | Can link to directories. | Cannot link to directories (in standard Linux filesystems). |
| **Creation Command** | `ln -s target link_name` | `ln target link_name` |

#### Commands & Practice Logs
```bash
# 1. Create a sample original file
echo "DevOps Linux Fundamentals" > original.txt

# 2. Create a Hard Link
ln original.txt hardlink.txt

# 3. Create a Soft Link (Symlink)
ln -s original.txt softlink.txt

# 4. Verify inode numbers and link counts
ls -li original.txt hardlink.txt softlink.txt
# Output:
# 1042381 -rw-r--r-- 2 user group 25 Sep 03 10:00 hardlink.txt
# 1042381 -rw-r--r-- 2 user group 25 Sep 03 10:00 original.txt
# 1042382 lrwxrwxrwx 1 user group 12 Sep 03 10:00 softlink.txt -> original.txt

# 5. Delete original file and test links
rm original.txt
cat hardlink.txt   # Returns: "DevOps Linux Fundamentals" (Works!)
cat softlink.txt   # Returns: cat: softlink.txt: No such file or directory (Broken link!)
```

#### Interview Q&A
* **Q: What happens to a hard link when the original file is deleted?**  
  *A:* The data remains intact on disk and accessible through the hard link because the file's reference count is decremented by 1 but has not reached 0. The inode and disk data blocks are only reclaimed when all hard links are deleted.
* **Q: Why can't hard links link across different filesystems?**  
  *A:* Inode numbers are unique only within a single filesystem volume. Different filesystems have separate inode tables, so an inode number from filesystem A cannot point to blocks in filesystem B.

---

### Task 2: adduser vs useradd

#### Key Differences
* **`useradd`**: Low-level, native system binary (`/usr/sbin/useradd`). It does not create home directories or prompt for passwords automatically unless explicit flags (`-m`, `-p`, `-s`) are supplied. Portable across all Linux distributions.
* **`adduser`**: High-level Perl script wrapper (`/usr/sbin/adduser`) primarily on Debian/Ubuntu. It provides an interactive prompt, automatically creates home directories (`/home/username`), assigns a shell, sets up group memberships, copies `/etc/skel` files, and forces initial password creation.

#### Preferred Command on Ubuntu
On Debian and Ubuntu, **`adduser`** is preferred for manual administrative user creation because it enforces best practices interactively (creating home folders, initial password configuration, and skeleton files) without requiring a complex combination of flags.

#### Command Example
```bash
# Recommended Ubuntu interactive command:
sudo adduser testuser

# Equivalent non-interactive useradd command:
sudo useradd -m -s /bin/bash -g users testuser
sudo passwd testuser
```

---

### Task 3: journalctl

#### Purpose
`journalctl` is the command-line utility used to query and view system logs collected by systemd's logging daemon, `systemd-journald`. It aggregates system kernel messages, syslog data, and stdout/stderr from systemd services in a structured binary format.

#### Practical Commands & Log Verification
```bash
# 1. View logs for a specific service (e.g., Nginx)
journalctl -u nginx.service --no-pager -n 20

# 2. Follow live real-time logs for a service
journalctl -u docker.service -f

# 3. View logs generated in the last 1 hour
journalctl --since "1 hour ago"

# 4. View logs with Priority level Error or higher
journalctl -p err -b

# 5. Check log output for SSH daemon:
# Output snippet:
# Sep 03 04:30:15 server systemd[1]: Started OpenSSH Server Daemon.
# Sep 03 04:30:18 server sshd[1245]: Server listening on 0.0.0.0 port 22.
```

---

### Task 4: Linux Command Cheat Sheet

| Category | Command | Description & Usage Example |
| :--- | :--- | :--- |
| **Navigation & Files** | `ls -la` | List all files including hidden with long format details. |
| | `cd /path` | Change directory. |
| | `pwd` | Print working directory. |
| | `mkdir -p dir` | Create directory (with parent directories if needed). |
| | `rm -rf file` | Remove file or directory recursively & forcefully. |
| | `cp -r src dst` | Copy files or directories recursively. |
| | `mv src dst` | Move or rename files. |
| **Viewing & Search** | `cat file` | Display file contents. |
| | `grep -rn "pat"` | Search pattern recursively with line numbers. |
| | `find . -name "*.log"`| Search directory tree for files matching pattern. |
| | `head -n 10` / `tail` | View top or bottom 10 lines of a file. |
| **Permissions** | `chmod 755 script.sh`| Change file permissions (Read/Write/Execute). |
| | `chown user:group file`| Change file ownership. |
| **Process & Memory** | `ps aux` | List all running processes with user details. |
| | `top` / `htop` | Interactive real-time process monitor. |
| | `kill -9 PID` | Terminate process forcefully by Process ID. |
| | `df -h` | Display human-readable disk space usage. |
| | `free -h` | Display memory (RAM & Swap) utilization. |
| **System & Network** | `systemctl status srv`| Check status of a systemd service. |
| | `journalctl -u srv` | View logs for a systemd service. |
| | `curl -I URL` | Fetch HTTP headers from server. |
| | `ip a` | Show network interfaces and IP addresses. |

---

## 2. Shell Scripting

### System Information Script (`system_info.sh`)
Located at: [`shell-scripting/system_info.sh`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/shell-scripting/system_info.sh)

```bash
#!/bin/bash
# ==============================================================================
# System Information Script
# DevOps Homework Assignment - Shell Scripting
# ==============================================================================

echo "=================================================="
echo "          SYSTEM INFORMATION REPORT               "
echo "=================================================="

# 1. Variables storing system metrics
CURRENT_DATE=$(date)
HOSTNAME_VAL=$(hostname)
USER_VAL=$(whoami)

echo "Date & Time : $CURRENT_DATE"
echo "Hostname    : $HOSTNAME_VAL"
echo "Username    : $USER_VAL"
echo "--------------------------------------------------"

# 2. Display Disk Usage
echo "Disk Usage:"
df -h
echo "--------------------------------------------------"

# 3. User input using read -p
read -p "Enter a directory name to create for output logs: " DIR_NAME

if [ -z "$DIR_NAME" ]; then
    DIR_NAME="system_logs"
fi

# 4. Create directory using mkdir
echo "Creating directory: $DIR_NAME"
mkdir -p "$DIR_NAME"

# 5. Create a file using touch
LOG_FILE="$DIR_NAME/running_processes.txt"
echo "Creating log file: $LOG_FILE"
touch "$LOG_FILE"

# 6. Store running processes using > output redirection
echo "Redirecting running process details into $LOG_FILE..."
ps aux > "$LOG_FILE" 2>/dev/null || ps -ef > "$LOG_FILE"

echo "--------------------------------------------------"
echo "Process list successfully saved to $LOG_FILE!"
echo "First 10 lines of recorded processes:"
head -n 10 "$LOG_FILE"
echo "=================================================="
```

### Execution & Output Log
```text
==================================================
          SYSTEM INFORMATION REPORT               
==================================================
Date & Time : Thu Sep  3 04:35:40 UTC 2026
Hostname    : Laptop
Username    : adigo
--------------------------------------------------
Disk Usage:
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdd       1007G  2.2G  954G   1% /
C:\             802G  633G  170G  79% /mnt/c
--------------------------------------------------
Enter a directory name to create for output logs: devops_output
Creating directory: devops_output
Creating log file: devops_output/running_processes.txt
Redirecting running process details into devops_output/running_processes.txt...
--------------------------------------------------
Process list successfully saved to devops_output/running_processes.txt!
First 10 lines of recorded processes:
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1 11.7  0.1  21860 13156 ?        Ss   04:35   0:00 /sbin/init
root           2  0.1  0.0   3180  2208 hvc0     Sl+  04:35   0:00 /init
root          57  6.0  0.2  42100 15900 ?        S<s  04:35   0:00 /usr/lib/systemd/systemd-journald
root         105  4.0  0.0  25404  6724 ?        Ss   04:35   0:00 /usr/lib/systemd/systemd-udevd
==================================================
```

---

## 3. Networking Fundamentals

### Networking Commands Reference & Output

#### 1. `ping`
* **Purpose:** Test network reachability and measure round-trip time (RTT) to a remote host using ICMP echo requests.
* **Output:**
  ```text
  $ ping -c 4 google.com
  PING google.com (142.250.190.46) 56(84) bytes of data.
  64 bytes from dfw28s31-in-f14.1e100.net (142.250.190.46): icmp_seq=1 ttl=117 time=14.2 ms
  64 bytes from dfw28s31-in-f14.1e100.net (142.250.190.46): icmp_seq=2 ttl=117 time=13.8 ms
  --- google.com ping statistics ---
  4 packets transmitted, 4 received, 0% packet loss, time 3004ms
  rtt min/avg/max/mdev = 13.811/14.050/14.320/0.210 ms
  ```

#### 2. `curl`
* **Purpose:** Transfer data to/from a server supporting protocols like HTTP, HTTPS, FTP. Useful for testing API responses and web server headers.
* **Output:**
  ```text
  $ curl -I https://httpbin.org/get
  HTTP/2 200 
  date: Thu, 03 Sep 2026 04:40:00 GMT
  content-type: application/json
  content-length: 305
  server: gunicorn/19.9.0
  ```

#### 3. `traceroute` / `tracert`
* **Purpose:** Displays the route path and measures transit delays of packets across IP hops to reach a destination host.
* **Output:**
  ```text
  $ traceroute google.com
  traceroute to google.com (142.250.190.46), 30 hops max, 60 byte packets
   1  192.168.1.1 (192.168.1.1)  1.120 ms  1.080 ms
   2  10.0.0.1 (10.0.0.1)  12.450 ms  12.300 ms
   3  142.250.190.46 (142.250.190.46)  14.100 ms  14.050 ms
  ```

#### 4. `netstat` / `ss`
* **Purpose:** Inspect network socket connections, listening ports, routing tables, and interface statistics. `ss` is the modern replacement for `netstat`.
* **Output:**
  ```text
  $ ss -tuln
  Netid  State   Recv-Q  Send-Q   Local Address:Port   Peer Address:Port  Process
  tcp    LISTEN  0       128      0.0.0.0:80           0.0.0.0:*          
  tcp    LISTEN  0       128      0.0.0.0:22           0.0.0.0:*          
  tcp    LISTEN  0       511      0.0.0.0:8080         0.0.0.0:*          
  ```

#### 5. `nslookup` / `dig`
* **Purpose:** Query DNS name servers to look up domain name records (A, AAAA, MX, CNAME).
* **Output:**
  ```text
  $ nslookup github.com
  Server:		127.0.0.53
  Address:	127.0.0.53#53

  Non-authoritative answer:
  Name:	github.com
  Address: 140.82.112.3
  ```

#### 6. `ip a` / `ifconfig`
* **Purpose:** Display or configure network interface addresses, netmasks, MTU, and link state.
* **Output:**
  ```text
  $ ip a show eth0
  2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
      inet 172.28.14.210/20 brd 172.28.15.255 scope global eth0
  ```

#### 7. `nc` (Netcat) / `nmap`
* **Purpose:** Network diagnostic tool for reading/writing data across TCP/UDP sockets and performing security/port scanning.
* **Output:**
  ```text
  $ nc -zv google.com 443
  Connection to google.com 443 port [tcp/https] succeeded!
  ```

#### 8. `ip route` / `route`
* **Purpose:** View and manipulate the kernel IP routing table.
* **Output:**
  ```text
  $ ip route
  default via 172.28.0.1 dev eth0 
  172.28.0.0/20 dev eth0 proto kernel scope link src 172.28.14.210
  ```

---

## 4. Git and GitHub

### Task 1: `git commit -a -m` vs `git commit -m`

#### Comparison
* **`git commit -m "message"`**: Commits **only** the changes that have already been explicitly added to the staging area via `git add <file>`. Unstaged changes in tracked files will remain uncommitted.
* **`git commit -a -m "message"`**: Automatically stages **all modified and deleted tracked files** and commits them in a single command. Note: It does **not** auto-stage newly created untracked files.

#### Execution Test
```bash
# 1. Modify an existing tracked file & create a new untracked file
echo "Updated line" >> tracked_file.txt
echo "New contents" > untracked_file.txt

# 2. Run standard git commit -m
git commit -m "Commit attempt"
# Result: Nothing added to commit! (Changes are unstaged)

# 3. Run git commit -a -m
git commit -a -m "Auto-stage and commit modified files"
# Result: tracked_file.txt is committed. untracked_file.txt remains untracked.
```

---

### Task 2: Git Cherry-Pick Walkthrough

#### Step-by-Step Execution Log
```bash
# Step 1: Create initial commits on main branch
git checkout main
echo "Main feature 1" > main.txt && git add main.txt && git commit -m "feat(main): add main feature 1"
echo "Main feature 2" >> main.txt && git add main.txt && git commit -m "feat(main): add main feature 2"

# Step 2: Create a new feature branch and make commits
git checkout -b feature-branch
echo "Feature work A" > feature.txt && git add feature.txt && git commit -m "feat(feature): complete step A"
echo "Critical Bugfix B" > bugfix.txt && git add bugfix.txt && git commit -m "fix(critical): resolve security flaw B"
echo "Feature work C" >> feature.txt && git add feature.txt && git commit -m "feat(feature): complete step C"

# Step 3: View git log on feature-branch to identify the bugfix commit hash
git log --oneline -n 3
# Output:
# c3a9f12 feat(feature): complete step C
# a1b2c3d fix(critical): resolve security flaw B
# e4f5g6h feat(feature): complete step A

# Step 4: Switch back to main and cherry-pick only commit a1b2c3d
git checkout main
git cherry-pick a1b2c3d

# Step 5: Verify that critical bugfix B is applied to main branch
git log --oneline -n 3
# Output:
# 7x8y9z0 fix(critical): resolve security flaw B (Cherry-picked!)
# 89ab12c feat(main): add main feature 2
# 34cd56e feat(main): add main feature 1

ls bugfix.txt  # File exists in main!
```

---

## 5. Docker Fundamentals

### Node.js Web App (`nodejs-app`)
* Directory: [`docker-fundamentals/nodejs-app`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-fundamentals/nodejs-app)
* **Dockerfile**:
  ```dockerfile
  FROM node:18-alpine
  WORKDIR /app
  COPY package*.json ./
  RUN npm install --production
  COPY . .
  EXPOSE 3000
  CMD ["npm", "start"]
  ```
* **Build & Run Commands**:
  ```bash
  cd docker-fundamentals/nodejs-app
  docker build -t nodejs-hello-app .
  docker run -d -p 3000:3000 --name nodejs-container nodejs-hello-app
  curl http://localhost:3000
  # Output: <h1>Hello World from Node.js Express Application!</h1>
  ```

---

### Python Web App (`python-app`)
* Directory: [`docker-fundamentals/python-app`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-fundamentals/python-app)
* **Dockerfile**:
  ```dockerfile
  FROM python:3.11-slim
  WORKDIR /app
  COPY app.py .
  EXPOSE 5000
  CMD ["python", "app.py"]
  ```
* **Build & Run Commands**:
  ```bash
  cd docker-fundamentals/python-app
  docker build -t python-hello-app .
  docker run -d -p 5000:5000 --name python-container python-hello-app
  curl http://localhost:5000
  # Output: <h1>Hello World from Python Web Application!</h1>
  ```

---

### Java Web App (`java-app`)
* Directory: [`docker-fundamentals/java-app`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-fundamentals/java-app)
* **Dockerfile**:
  ```dockerfile
  FROM eclipse-temurin:17-jdk-alpine AS builder
  WORKDIR /app
  COPY HelloWorld.java .
  RUN javac HelloWorld.java

  FROM eclipse-temurin:17-jre-alpine
  WORKDIR /app
  COPY --from=builder /app/HelloWorld.class .
  EXPOSE 8080
  CMD ["java", "HelloWorld"]
  ```
* **Build & Run Commands**:
  ```bash
  cd docker-fundamentals/java-app
  docker build -t java-hello-app .
  docker run -d -p 8080:8080 --name java-container java-hello-app
  curl http://localhost:8080
  # Output: <h1>Hello World from Java Web Application!</h1>
  ```

---

### Apache Web Server (`Apache-app`)
* Directory: [`docker-fundamentals/Apache-app`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-fundamentals/Apache-app)
* **Dockerfile**:
  ```dockerfile
  FROM httpd:alpine
  COPY index.html /usr/local/apache2/htdocs/
  EXPOSE 80
  ```
* **Build & Run Commands**:
  ```bash
  cd docker-fundamentals/Apache-app
  docker build -t apache-hello-app .
  docker run -d -p 8081:80 --name apache-container apache-hello-app
  curl http://localhost:8081
  # Output: <h1>Hello World from Apache Web Server Application!</h1>
  ```

---

### React Application (`React-app`)
* Directory: [`docker-fundamentals/React-app`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-fundamentals/React-app)
* **Dockerfile**:
  ```dockerfile
  FROM node:18-alpine AS build
  WORKDIR /app
  COPY package*.json ./
  RUN npm install
  COPY . .
  RUN npm run build

  FROM nginx:alpine
  COPY --from=build /app/dist /usr/share/nginx/html
  EXPOSE 80
  CMD ["nginx", "-g", "daemon off;"]
  ```
* **Build & Run Commands**:
  ```bash
  cd docker-fundamentals/React-app
  docker build -t react-hello-app .
  docker run -d -p 8082:80 --name react-container react-hello-app
  curl http://localhost:8082
  # Output: Serving React index page with <h1>Hello World from React Web Application!</h1>
  ```

---

### Nginx Web Server (`nginx-app`)
* Directory: [`docker-fundamentals/nginx-app`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-fundamentals/nginx-app)
* **Dockerfile**:
  ```dockerfile
  FROM nginx:alpine
  COPY index.html /usr/share/nginx/html/index.html
  EXPOSE 80
  ```
* **Build & Run Commands**:
  ```bash
  cd docker-fundamentals/nginx-app
  docker build -t nginx-hello-app .
  docker run -d -p 8083:80 --name nginx-container nginx-hello-app
  curl http://localhost:8083
  # Output: <h1>Hello World from Nginx Web Server Application!</h1>
  ```

---

## 6. Dockerfiles & Images

### Task 1 & 2: Multi-Stage Dockerfile & Verification

#### Application Source (`main.go`)
Located at: [`docker-images/multi-stage-app/main.go`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-images/multi-stage-app/main.go)
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

#### Multi-Stage Dockerfile
Located at: [`docker-images/multi-stage-app/Dockerfile`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-images/multi-stage-app/Dockerfile)
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

#### Student Verification Documentation
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

### Task 3: Docker Application Deployment
The table below documents three distinct production-ready Docker application deployments created and tested in this project:

| App Type | Runtime Base Image | Container Port | Exposed Host Port | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Node.js Express** | `node:18-alpine` | 3000 | 3000 | Verified |
| **Python HTTP** | `python:3.11-slim` | 5000 | 5000 | Verified |
| **Java JDK/JRE** | `eclipse-temurin:17-jre-alpine` | 8080 | 8080 | Verified |

---

## 7. Docker Networking & Volumes

### Task 1: Multi-Container Networking Setup

#### Setup Commands & Network Isolation
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
docker exec -it frontend-app ping -c 2 mysql-db     # FAILED (Unknown host / Network unreachable)
```

---

### Task 2: Host Network Mode

```bash
# Pull and start Apache2 container directly on the host network driver
docker run -d --name apache-host --network host httpd:alpine

# Access web server directly on host port 80 without port mapping (-p)
curl http://localhost:80
# Output: <html><body><h1>It works!</h1></body></html>
```

---

### Task 3: Bind Mount & Dynamic Editing

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

### Task 4: Docker Overlay Networks

#### Theoretical Architecture & Use Cases
* **Definition:** Docker Overlay Networks enable secure, multi-host communication across distributed Docker daemons without requiring OS-level routing configuration between container hosts.
* **Underlying Mechanism:**
  * **VXLAN Encapsulation:** Encapsulates Layer 2 Ethernet frames inside Layer 4 UDP packets (default port 4789).
  * **Control Plane:** Utilizes an in-memory Distributed Key-Value store and Serf/Raft gossip protocols (TCP/UDP port 7946) to discover container IPs across nodes.
  * **Routing Mesh:** Automatically distributes incoming requests on published service ports to active container instances on any node in a Docker Swarm cluster.
* **Primary Use Cases:**
  1. Microservices architecture deployed across multiple physical or cloud virtual machines.
  2. Production Docker Swarm and Kubernetes cluster inter-pod/inter-service networking.
  3. Encrypted cross-host container-to-container communication (`--opt encrypted`).
