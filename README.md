# DevOps Homework Submission

**Student Email:** aditya.24bcs10057@sst.scaler.com  
**Enrollment ID:** 24bcs10057  
**GitHub Repository:** https://github.com/Posiedon207/DevOpsHW

This repository contains all completed homework assignments for the full DevOps course (Sessions 1-21).

---

## Table of Contents

### Docker & Linux Fundamentals
1. [Linux Fundamentals](#session-12-linux-fundamentals) - [linux-fundamentals/](linux-fundamentals/)
2. [Shell Scripting](#session-3-shell-scripting) - [shell-scripting/](shell-scripting/)
3. [Networking Fundamentals](#session-4-networking-fundamentals) - [networking-fundamentals/](networking-fundamentals/)
4. [Git and GitHub](#session-5-git-and-github) - [git-github/](git-github/)
5. [Docker Fundamentals](#session-6-docker-fundamentals) - [docker-fundamentals/](docker-fundamentals/)
6. [Docker Images](#session-7-docker-images) - [docker-images/](docker-images/)
7. [Docker Networking](#session-8-docker-networking) - [docker-networking/](docker-networking/)

### Kubernetes
8. [Kubernetes Fundamentals](#session-9-kubernetes-fundamentals) - [kubernetes-fundamentals/](kubernetes-fundamentals/)
9. [Kubernetes Pods, ReplicaSets & Deployments](#session-10-kubernetes-pods-replicasets--deployments) - [kubernetes-pods-deployments/](kubernetes-pods-deployments/)
10. [Kubernetes Networking & Services](#session-11-kubernetes-networking--services) - [kubernetes-networking-services/](kubernetes-networking-services/)
11. [Kubernetes Ingress, ConfigMaps & Secrets](#session-12-kubernetes-ingress-configmaps--secrets) - [kubernetes-ingress-configmaps-secrets/](kubernetes-ingress-configmaps-secrets/)
12. [Kubernetes Storage, HPA & Probes](#session-13-kubernetes-storage-hpa--probes) - [kubernetes-storage-hpa-probes/](kubernetes-storage-hpa-probes/)
13. [Kubernetes Troubleshooting](#session-14-kubernetes-troubleshooting) - [kubernetes-troubleshooting/](kubernetes-troubleshooting/)

### Advanced DevOps
14. [Helm](#session-15-helm) - [helm/](helm/)
15. [CI/CD & GitHub Actions](#session-16-cicd--github-actions) - [cicd-github-actions/](cicd-github-actions/)
16. [DevSecOps](#session-17-devsecops) - [devsecops/](devsecops/)
17. [Terraform & AWS](#session-18-terraform--aws) - [terraform-aws/](terraform-aws/)
18. [Terraform Cloud](#session-19-terraform-cloud) - [terraform-cloud/](terraform-cloud/)
19. [Monitoring & GitOps](#session-20-monitoring--gitops) - [monitoring-gitops/](monitoring-gitops/)
20. [Final DevOps Project](#session-21-final-devops-project) - [final-devops-project/](final-devops-project/)

---

## Session 1&2: Linux Fundamentals

Folder: [linux-fundamentals/](linux-fundamentals/)

### Task 1: Soft Link & Hard Link
* **Soft Link (Symbolic Link):** Acts like a shortcut to the target file path. If the original file is deleted, the soft link becomes broken. It can link across different filesystems.
* **Hard Link:** Points directly to the same inode/data on disk. If the original file is deleted, data remains accessible via hard link. Cannot link across filesystems.
* **Commands Used:** ln original.txt hardlink.txt and ln -s original.txt softlink.txt

### Task 2: dduser vs useradd
* **useradd**: Low-level utility. Does not create home directory or password unless flags passed.
* **dduser**: Interactive, user-friendly script on Ubuntu/Debian. Automatically creates /home/username, copies shell config files, prompts for password.

### Task 3: journalctl
* journalctl inspects system and service logs managed by systemd.
* Command used: journalctl -u nginx.service -n 20

### Task 4: Linux Command Cheat Sheet
Practiced: ls, cd, pwd, mkdir, 
m, cp, mv, cat, grep, ps, df, chmod, systemctl, journalctl

---

## Session 3: Shell Scripting

Folder: [shell-scripting/](shell-scripting/)

Created system_info.sh that:
* Prints current date, hostname, username
* Shows disk usage (df -h)
* Takes user input for directory name (
ead -p)
* Creates directory (mkdir) and log file (    ouch)
* Stores running processes into log file using > output redirection

---

## Session 4: Networking Fundamentals

Folder: [networking-fundamentals/](networking-fundamentals/)

Commands practiced and documented:
* ping - Test reachability and round-trip time
* curl - Fetch HTTP response headers
*     raceroute - Check route across network hops
* ss / 
etstat - Inspect listening ports
* 
slookup / dig - DNS queries
* ip a - Check network interface IPs
* 
c (Netcat) - Verify TCP port connectivity

---

## Session 5: Git and GitHub

Folder: [git-github/](git-github/)

### Task 1: git commit -a -m vs git commit -m
* git commit -m: Only commits staged files
* git commit -a -m: Auto-stages and commits all modified tracked files

### Task 2: Git Cherry-Pick
Practiced picking a specific commit from a feature branch onto main.
Steps: git log, git cherry-pick <hash>, verified with git log.

---

## Session 6: Docker Fundamentals

Folder: [docker-fundamentals/](docker-fundamentals/)

Created Hello World web applications using Docker for 6 environments:
1. 
odejs-app/ (Port 3000) - Node.js Express
2. python-app/ (Port 5000) - Python Flask
3. java-app/ (Port 8080) - Java Spring Boot
4. Apache-app/ (Port 8081) - Apache HTTP Server
5. React-app/ (Port 8082) - React (Nginx served)
6. 
ginx-app/ (Port 8083) - Nginx

---

## Session 7: Docker Images

Folder: [docker-images/](docker-images/)

### Multi-Stage Docker Build
* Built Go web application using 2-stage Dockerfile (build in golang:1.22-alpine, runtime in lpine:3.19)
* Verified: curl http://localhost:8080 -> Hello World from Docker multi-stage build
* Verified container running on port 8080 using docker ps

---

## Session 8: Docker Networking

Folder: [docker-networking/](docker-networking/)

1. **Multi-Container Networking**: Created frontend-net, ackend-net, db-net. Backend connected to both networks. Verified network isolation.
2. **Host Network Mode**: Ran Apache with --network host on port 80.
3. **Bind Mount**: Mounted ./bind_mount_data/index.html into Nginx. Live updates without container restart verified.
4. **Overlay Network**: Researched multi-host container communication in Docker Swarm.

---

## Session 9: Kubernetes Fundamentals

Folder: [kubernetes-fundamentals/](kubernetes-fundamentals/)

* Installed and configured Minikube (minikube start --driver=docker)
* Verified cluster: kubectl get nodes -> minikube Ready
* Explored Kubernetes architecture: Control plane (API server, etcd, scheduler, controller-manager) and Worker nodes (kubelet, kube-proxy)
* Practiced all basic kubectl commands
* Completed Kubernetes Basics tutorial with hello-node deployment

---

## Session 10: Kubernetes Pods, ReplicaSets & Deployments

Folder: [kubernetes-pods-deployments/](kubernetes-pods-deployments/)

Implemented all 4 deployment strategies:
1. **Rolling Update** - Zero-downtime replacement of pods
2. **Blue-Green** - Instant traffic switch between versions
3. **Canary** - Route small % of traffic to new version
4. **Recreate** - All pods killed before new ones start

Demonstrated Pod lifecycle phases: Pending -> Running -> Succeeded/Failed
Tested lifecycle hooks (postStart, preStop).

---

## Session 11: Kubernetes Networking & Services

Folder: [kubernetes-networking-services/](kubernetes-networking-services/)

Deployed and verified all 5 Service types:
1. **ClusterIP** - Internal only
2. **NodePort** - Exposed on node port 30080
3. **LoadBalancer** - Cloud external LB (minikube tunnel)
4. **ExternalName** - DNS alias to external service
5. **Headless** - No ClusterIP, direct Pod DNS

Documented Deployment vs ReplicaSet vs DaemonSet vs StatefulSet comparison.
Created FQDN documentation and CoreDNS troubleshooting guide.

---

## Session 12: Kubernetes Ingress, ConfigMaps & Secrets

Folder: [kubernetes-ingress-configmaps-secrets/](kubernetes-ingress-configmaps-secrets/)

* Created ConfigMap and injected into Pod via envFrom
* Created Secret (Opaque) and injected via secretKeyRef
* Deployed application with Ingress routing through nginx-ingress controller
* Documented why Secrets should not be committed to Git
* Troubleshooting: Fixed CrashLoopBackOff from missing env var

---

## Session 13: Kubernetes Storage, HPA & Probes

Folder: [kubernetes-storage-hpa-probes/](kubernetes-storage-hpa-probes/)

* Documented all volume types: emptyDir, hostPath, PV, PVC, StorageClass, dynamic provisioning
* HPA hands-on: Deployed app, configured HPA (1-10 replicas at 50% CPU), generated load, observed auto-scaling
* Configured Liveness, Readiness, and Startup probes

---

## Session 14: Kubernetes Troubleshooting

Folder: [kubernetes-troubleshooting/](kubernetes-troubleshooting/)

* Practiced: kubectl get, describe, logs, exec, events, explain,     op
* Fixed CrashLoopBackOff (missing env var)
* Fixed ImagePullBackOff (wrong tag)
* Fixed Pending pod (insufficient resources)
* Fixed Service connectivity (label selector mismatch)
* Fixed DNS issues (CoreDNS pod down)

---

## Session 15: Helm

Folder: [helm/](helm/)

Practiced all Helm commands: create, install, list, status, get, upgrade, history, 
ollback, uninstall, 
epo, search

Complete rollback workflow: Install (r1) -> Upgrade (r2) -> Bad Upgrade (r3) -> Rollback to r2 (r4)

---

## Session 16: CI/CD & GitHub Actions

Folder: [cicd-github-actions/](cicd-github-actions/)

Built complete CI/CD pipeline with GitHub Actions:
* CI: Checkout -> Install deps -> Run tests -> Build Docker image -> Upload artifacts
* CD: Login to Docker Hub -> Build & push image with SHA tag
* Used Secrets for Docker Hub credentials
* Pipeline runs on push to main/develop branches

---

## Session 17: DevSecOps

Folder: [devsecops/](devsecops/)

Built complete DevSecOps pipeline adding security stages:
* **SAST** (Bandit): Static code analysis
* **SCA** (Safety): Dependency vulnerability check
* **Secret Scanning** (TruffleHog): Detect hardcoded secrets
* **Container Scan** (Trivy): Docker image CVE scanning
* **Security Gate**: Pipeline fails on critical findings

---

## Session 18: Terraform & AWS

Folder: [terraform-aws/](terraform-aws/)

* Created Terraform project with S3 bucket (versioning + encryption)
* Ran full workflow: init -> fmt -> validate -> plan -> apply -> show -> output -> destroy
* Documented all 5 AWS services: IAM, EC2, S3, VPC, DynamoDB+RDS

---

## Session 19: Terraform Cloud

Folder: [terraform-cloud/](terraform-cloud/)

* Built end-to-end AWS infrastructure: VPC, subnets, IGW, NAT Gateway, Route Tables, Security Groups, EC2, S3
* Demonstrated Terraform providers, variables, resources, outputs, dependencies, state management
* Applied and destroyed complete 12-resource infrastructure

---

## Session 20: Monitoring & GitOps

Folder: [monitoring-gitops/](monitoring-gitops/)

* Deployed Prometheus + Grafana via Helm to Kubernetes cluster
* Created PromQL queries for CPU, memory, error rate monitoring
* Documented three observability pillars: Metrics, Logs, Traces
* Set up ArgoCD for GitOps - auto-sync Kubernetes manifests from GitHub

---

## Session 21: Final DevOps Project & Multi-Container Deployment

Folder: [final-devops-project/](final-devops-project/)

Complete 3-Tier Multi-Container Stack (Frontend, FastAPI Backend, PostgreSQL):
* **Manual Deployment:** Deployed PostgreSQL database (5432), FastAPI backend (8000), and Node.js frontend (3000) manually
* **Docker Containerization:** Created production Dockerfiles for frontend and backend
* **Docker Compose Orchestration:** Full stack deployed via docker-compose up -d --build
* **Verified Endpoints:**
  * UI running on http://localhost:3000
  * Swagger UI on http://localhost:8000/docs
  * Health check on http://localhost:8000/health
  * Prometheus metrics on http://localhost:8000/metrics
* **Screenshots & Documentation:** All verification screenshots and run steps included in [final-devops-project/README.md](final-devops-project/README.md)
