# Session 9: Kubernetes Fundamentals

**Student:** posiedon2212@gmail.com
**Enrollment ID:** DEV-HW-2026

---

## Task Overview

Installed and configured Minikube, verified cluster status, explored Kubernetes architecture, and practiced basic Kubernetes objects and commands.

---

## Task 1: Install and Configure Minikube

### Installation Steps

`ash
# Install Minikube (Linux/WSL)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Install kubectl
curl -LO https://dl.k8s.io/release/stable/bin/linux/amd64/kubectl
chmod +x kubectl && sudo mv kubectl /usr/local/bin/

# Start Minikube
minikube start --driver=docker
`

### Output
`
minikube v1.33.0 on Ubuntu 22.04
Using the docker driver
Creating docker container (CPUs=2, Memory=3900MB)
Preparing Kubernetes v1.30.0 on Docker 26.0.1
Verifying Kubernetes components...
Done! kubectl is now configured to use minikube cluster
`

---

## Task 2: Verify Kubernetes Cluster Status

`ash
minikube status
# minikube: Running
# type: Control Plane
# host: Running
# kubelet: Running
# apiserver: Running
# kubeconfig: Configured

kubectl get nodes
# NAME       STATUS   ROLES           AGE   VERSION
# minikube   Ready    control-plane   2m    v1.30.0
`

---

## Task 3: Kubernetes Architecture Notes

### Control Plane Components

| Component | Role |
|-----------|------|
| kube-apiserver | Exposes the Kubernetes API; front-end for control plane |
| etcd | Key-value store for all cluster data |
| kube-scheduler | Assigns new Pods to nodes |
| kube-controller-manager | Runs controller processes to maintain state |

### Worker Node Components

| Component | Role |
|-----------|------|
| kubelet | Agent on each node; ensures containers are running |
| kube-proxy | Maintains network rules for Pod communication |
| Container Runtime | Runs containers (Docker/containerd) |

### Architecture Diagram
`
kubectl --> API Server --> etcd
                |
           Scheduler --> assigns Pod to Node
                |
     Controller Manager --> maintains desired state
                |
        kubelet (on Node) --> starts containers
`

---

## Task 4: Basic Kubernetes Objects and Commands

### Key Objects

| Object | Purpose |
|--------|---------|
| Pod | Smallest deployable unit; wraps one or more containers |
| ReplicaSet | Ensures N copies of a Pod are running |
| Deployment | Manages ReplicaSets; enables rolling updates |
| Service | Exposes Pods via stable network endpoint |
| ConfigMap | Stores non-sensitive config data |
| Secret | Stores sensitive data (passwords, tokens) |
| Namespace | Logical isolation of resources |

### Commands Practiced

`ash
kubectl get all
kubectl get pods -o wide
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl exec -it <pod-name> -- /bin/bash
kubectl apply -f deployment.yaml
kubectl delete pod <pod-name>
kubectl get namespaces
kubectl scale deployment <name> --replicas=3
kubectl get events
`

---

## Task 5: Kubernetes Basics Tutorial Hands-On

`ash
# Create deployment
kubectl create deployment hello-node --image=k8s.gcr.io/echoserver:1.4

# Verify
kubectl get deployments
# NAME         READY   UP-TO-DATE   AVAILABLE   AGE
# hello-node   1/1     1            1           1m

kubectl get pods
# NAME                          READY   STATUS    RESTARTS   AGE
# hello-node-7567d9fdc9-42bdb   1/1     Running   0          1m

# Expose as NodePort service
kubectl expose deployment hello-node --type=NodePort --port=8080

# Access via minikube
minikube service hello-node --url
curl http://192.168.49.2:32046
`

### System Pod Status
`
kubectl get pods -n kube-system
NAME                               READY   STATUS    RESTARTS
coredns-5dd5756b68-7hv4g           1/1     Running   0
etcd-minikube                      1/1     Running   0
kube-apiserver-minikube            1/1     Running   0
kube-controller-manager-minikube   1/1     Running   0
kube-proxy-9bqfl                   1/1     Running   0
kube-scheduler-minikube            1/1     Running   0
`
