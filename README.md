# DevOps Homework Submission

**Student Email:** aditya.24bcs10057@sst.scaler.com  
**Enrollment ID:** 24bcs10057 

This repository contains my completed homework assignments for the DevOps course covering Linux Fundamentals, Shell Scripting, Networking Fundamentals, Git & GitHub, Docker Fundamentals, Dockerfiles & Images, and Docker Networking.

---

## Table of Contents
1. [Linux Fundamentals](#1-linux-fundamentals)
2. [Shell Scripting](#2-shell-scripting)
3. [Networking Fundamentals](#3-networking-fundamentals)
4. [Git and GitHub](#4-git-and-github)
5. [Docker Fundamentals](#5-docker-fundamentals)
6. [Dockerfiles & Images](#6-dockerfiles--images)
7. [Docker Networking & Volumes](#7-docker-networking--volumes)

---

## 1. Linux Fundamentals

Folder: [`linux-fundamentals/`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/linux-fundamentals)

### Task 1: Soft Link & Hard Link
* **Soft Link (Symbolic Link):** Acts like a shortcut to the target file path. If the original file is deleted, the soft link becomes broken. It can link across different filesystems and directories.
* **Hard Link:** Points directly to the same inode/data on disk. If the original file is deleted, the data is still accessible via the hard link until all hard links are removed. Cannot link across filesystems or directories.
* **Commands Used:** `ln original.txt hardlink.txt` and `ln -s original.txt softlink.txt`

### Task 2: `adduser` vs `useradd`
* **`useradd`**: A low-level Linux utility that creates a user without automatically setting up a home directory or password unless specific flags are passed.
* **`adduser`**: An interactive, user-friendly script recommended on Ubuntu/Debian. It automatically creates `/home/username`, copies shell configuration files, and prompts for a password.

### Task 3: `journalctl`
* `journalctl` is used to inspect system and service logs managed by `systemd`.
* Command used to view service logs: `journalctl -u nginx.service -n 20`

### Task 4: Linux Command Cheat Sheet
Reviewed and practiced standard Linux commands (`ls`, `cd`, `pwd`, `mkdir`, `rm`, `cp`, `mv`, `cat`, `grep`, `ps`, `df`, `chmod`, `systemctl`, `journalctl`).

---

## 2. Shell Scripting

Folder: [`shell-scripting/`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/shell-scripting)

### System Information Script (`system_info.sh`)
I created a shell script that performs the following:
* Prints current date, hostname, and username using variables.
* Displays disk usage using `df -h`.
* Prompts user for a directory name using `read -p`.
* Creates the directory (`mkdir`) and a log file (`touch`).
* Stores running process information into the log file using `>` output redirection.

```bash
chmod +x shell-scripting/system_info.sh
./shell-scripting/system_info.sh
```

---

## 3. Networking Fundamentals

Folder: [`networking-fundamentals/`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/networking-fundamentals)

Practiced the following networking commands and documented their purpose and outputs:
* **`ping`**: Tested reachability and measured round-trip time to host (`ping -c 4 google.com`).
* **`curl`**: Fetched HTTP response headers from web server (`curl -I https://httpbin.org/get`).
* **`traceroute`**: Checked route path across network hops.
* **`ss` / `netstat`**: Inspected listening ports and open sockets (`ss -tuln`).
* **`nslookup` / `dig`**: Performed DNS queries for domain name resolution.
* **`ip a`**: Checked network interface IP addresses.
* **`nc` (Netcat)**: Verified TCP port connectivity.
* **`ip route`**: Viewed default network gateway and routing table.

---

## 4. Git and GitHub

Folder: [`git-github/`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/git-github)

### Task 1: `git commit -a -m` vs `git commit -m`
* **`git commit -m`**: Only commits changes that were explicitly added to staging via `git add`.
* **`git commit -a -m`**: Automatically stages and commits all modified or deleted tracked files in a single step.

### Task 2: Git Cherry-Pick
* Practiced picking a specific commit from a feature branch and applying it onto `main`.
* Steps: Created commits on `main`, created `feature-branch`, identified target commit hash with `git log`, switched to `main`, and executed `git cherry-pick <hash>`.

---

## 5. Docker Fundamentals

Folder: [`docker-fundamentals/`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-fundamentals)

Created Hello World web applications for 6 different environments in separate folders:
1. `nodejs-app/` (Port 3000)
2. `python-app/` (Port 5000)
3. `java-app/` (Port 8080)
4. `Apache-app/` (Port 8081)
5. `React-app/` (Port 8082)
6. `nginx-app/` (Port 8083)

Built and ran each container, verifying that "Hello World" is displayed on the webpage.

---

## 6. Dockerfiles & Images

Folder: [`docker-images/`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-images)

### Multi-Stage Docker Build
* Built a Go web application using a 2-stage Dockerfile (build stage in `golang:1.22-alpine` and lightweight runtime stage in `alpine:3.19`).
* Verified response: `curl http://localhost:8080` -> Output: `Hello World from Docker multi-stage build`
* Verified container running on port 8080 using `docker ps`.
* Documented deployment of 3 application types: Node.js, Python, and Java.

---

## 7. Docker Networking & Volumes

Folder: [`docker-networking/`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/docker-networking)

### Tasks Completed:
1. **Multi-Container Networking**: Created `frontend-net`, `backend-net`, `db-net`. Attached backend container to both `frontend-net` and `db-net`. Verified backend can reach both frontend and DB, while frontend cannot directly access DB.
2. **Host Network Mode**: Ran Apache container with `--network host` and verified direct access on host port 80.
3. **Bind Mount**: Mounted local folder `./bind_mount_data` containing `index.html` into Nginx. Updated `index.html` on host and confirmed changes were reflected live without container restart.
4. **Overlay Network**: Researched overlay networks used for multi-host container communication in Docker Swarm.
