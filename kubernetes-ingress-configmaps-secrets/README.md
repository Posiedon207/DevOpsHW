# Session 12: Kubernetes Ingress, ConfigMaps and Secrets

**Student:** posiedon2212@gmail.com
**Enrollment ID:** DEV-HW-2026

---

## Task 1: ConfigMap Hands-On

```bash
kubectl create configmap app-config   --from-literal=DATABASE_HOST=postgres.default.svc.cluster.local   --from-literal=APP_ENV=production   --from-literal=LOG_LEVEL=info

kubectl get configmap app-config
# NAME         DATA   AGE
# app-config   3      5s

kubectl describe configmap app-config
# Data
# APP_ENV: production
# DATABASE_HOST: postgres.default.svc.cluster.local
# LOG_LEVEL: info
```

Injected into Pod via envFrom. Verified inside container:
```bash
kubectl exec -it app-pod -- env | grep APP_ENV
# APP_ENV=production
```

---

## Task 2: Secret Hands-On

```bash
kubectl create secret generic db-secret   --from-literal=DB_USERNAME=postgres   --from-literal=DB_PASSWORD=secretpass

kubectl get secret db-secret
# NAME        TYPE     DATA   AGE
# db-secret   Opaque   2      5s
```

Injected into Pod via secretKeyRef. Verified inside container:
```bash
kubectl exec -it db-pod -- env | grep POSTGRES_USER
# POSTGRES_USER=postgres
```

Why NOT commit Secrets to Git:
- base64 is encoding, NOT encryption
- Anyone with repo access can decode and steal credentials
- Use external secret managers: HashiCorp Vault, AWS Secrets Manager, External Secrets Operator

---

## Task 3: Ingress Hands-On

```bash
minikube addons enable ingress
kubectl apply -f ingress.yaml

kubectl get ingress
# NAME             CLASS   HOSTS       ADDRESS        PORTS
# web-app-ingress  nginx   myapp.local 192.168.49.2   80

# Add to /etc/hosts: 192.168.49.2 myapp.local
curl http://myapp.local
# Nginx Welcome Page served through Ingress!
```

---

## Task 4: Ingress vs Ingress Controller

| Aspect | Ingress | Ingress Controller |
|--------|---------|-------------------|
| What | Kubernetes API object (YAML resource) | Running software implementing routing |
| Role | Define routing rules | Actually route the traffic |
| Examples | ingress.yaml | nginx-ingress, Traefik, AWS ALB |

Both are required:
- Ingress defines WHAT routing should happen
- Ingress Controller implements HOW it happens

---

## Task 5: Troubleshooting Demo

Problem: CrashLoopBackOff due to missing env var.

```bash
kubectl logs broken-app
# Error: DATABASE_URL environment variable not set

# Fix: Patch deployment to add ConfigMap ref
kubectl set env deployment/broken-app --from=configmap/app-config

kubectl get pods
# NAME        READY   STATUS    RESTARTS
# broken-app  1/1     Running   0
```
