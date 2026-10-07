# Session 20: Monitoring, Observability and GitOps

**Student:** posiedon2212@gmail.com
**Enrollment ID:** DEV-HW-2026

---

## Task 1: Monitoring Demo

### Key Metrics Monitored
- **CPU utilization:** Percentage of CPU used by application Pods
- **Memory utilization:** RAM usage - critical for detecting memory leaks
- **Application health:** HTTP response codes, error rates, response time
- **Pod restarts:** Indicates CrashLoopBackOff or instability

### Prometheus + Grafana Setup on Kubernetes
```bash
# Install Prometheus Stack using Helm
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace

kubectl get pods -n monitoring
# NAME                                                   READY   STATUS
# alertmanager-monitoring-kube-prometheus-alertmanager   2/2     Running
# monitoring-grafana-7c9bc4c67f-xxx                      3/3     Running
# monitoring-kube-prometheus-operator-xxx                1/1     Running
# monitoring-prometheus-xxx                              2/2     Running
# node-exporter-xxx                                      1/1     Running
```

### Access Grafana Dashboard
```bash
# Port-forward Grafana
kubectl port-forward -n monitoring svc/monitoring-grafana 3000:80

# Default credentials: admin / prom-operator
# Access: http://localhost:3000

# Key dashboards:
# - Kubernetes / Cluster - overall cluster health
# - Kubernetes / Nodes - node CPU, memory, disk
# - Kubernetes / Pods - per-pod CPU and memory
```

### Prometheus Queries (PromQL)
```promql
# CPU usage per pod
rate(container_cpu_usage_seconds_total{namespace="default"}[5m])

# Memory usage per pod
container_memory_usage_bytes{namespace="default"} / 1024 / 1024

# HTTP error rate
rate(http_requests_total{status=~"5.."}[5m])

# Pod restart count
kube_pod_container_status_restarts_total{namespace="default"}
```

---

## Task 2: Observability - Three Pillars

### 1. Metrics
Numerical measurements over time (e.g., CPU %, request count, latency).
- Tool: **Prometheus** (scraping + storage), **Grafana** (visualization)
- Format: time-series data points with labels
- Why needed: Spot trends, set alerts, capacity planning

### 2. Logs
Time-stamped text records of events.
- Tool: **ELK Stack** (Elasticsearch, Logstash, Kibana), **Loki** (Grafana)
- Why needed: Debug errors, audit trail, understand what happened

### 3. Traces
End-to-end request flow across distributed services (microservices).
- Tool: **Jaeger**, **Zipkin**, **AWS X-Ray**
- Why needed: Find bottlenecks in complex request chains
- Each trace has spans (one per service call)

### Why Observability is Required
- Modern apps are distributed (microservices, Kubernetes)
- Impossible to debug without visibility into system internals
- "Black box" monitoring (just up/down) is not enough
- Need to answer: What, Where, When, Why, How

### Common Tools

| Category | Open Source | Cloud |
|----------|-------------|-------|
| Metrics | Prometheus + Grafana | AWS CloudWatch, Datadog |
| Logs | ELK Stack, Loki | AWS CloudWatch Logs, Splunk |
| Traces | Jaeger, Zipkin | AWS X-Ray, Datadog APM |

---

## Task 3: GitOps

### What is GitOps?
GitOps is an operational framework where Git is the single source of truth for infrastructure and application configuration. All changes are made via Git commits and automatically applied.

### Core Principles
1. **Declarative:** System state described in Git (YAML manifests)
2. **Versioned:** All changes tracked in Git history
3. **Automated:** System automatically syncs to Git state
4. **Reconciled:** Continuous loop comparing desired vs actual state

### GitOps Workflow
```
Developer pushes code to Git
  -> CI Pipeline (build, test, security scan)
    -> Update image tag in Kubernetes manifests (Git commit)
      -> GitOps controller detects change
        -> Pulls new manifests
          -> Applies to Kubernetes cluster
            -> Verifies deployment health
```

### Kubernetes + GitOps (ArgoCD)
```bash
# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Create ArgoCD Application
kubectl apply -f - <<EOF
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/Posiedon207/DevOpsHW
    targetRevision: main
    path: kubernetes
  destination:
    server: https://kubernetes.default.svc
    namespace: default
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
EOF

# ArgoCD will now auto-sync any Kubernetes manifest changes in the repo
```

### Benefits of GitOps
- Full audit trail of all changes (git log)
- Easy rollback (git revert)
- Disaster recovery from scratch (just apply manifests)
- Security: no direct cluster access needed (GitOps agent does it)
- Team collaboration via Pull Requests
