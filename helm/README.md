# Session 15: Helm

**Student:** posiedon2212@gmail.com
**Enrollment ID:** DEV-HW-2026

---

## What is Helm?
Helm is the package manager for Kubernetes. It manages Kubernetes applications using charts (pre-configured resource packages).

---

## Task 1: Helm Commands

### helm create
```bash
helm create my-app
# Creates scaffold with Chart.yaml, values.yaml, templates/
```

### helm install
```bash
helm install my-release ./my-app
# NAME: my-release
# STATUS: deployed
# REVISION: 1

helm install my-release ./my-app --set image.tag=1.25 --set replicaCount=3
```

### helm list
```bash
helm list
# NAME         REVISION   STATUS     CHART
# my-release   1          deployed   my-app-0.1.0
```

### helm status
```bash
helm status my-release
# NAME: my-release
# STATUS: deployed
# REVISION: 1
```

### helm get
```bash
helm get values my-release     # Show custom values
helm get manifest my-release   # Show rendered manifests
```

### helm upgrade
```bash
helm upgrade my-release ./my-app --set image.tag=1.26
# Release "my-release" has been upgraded. REVISION: 2
```

### helm history
```bash
helm history my-release
# REVISION   STATUS      DESCRIPTION
# 1          superseded  Install complete
# 2          deployed    Upgrade complete
```

### helm rollback
```bash
helm rollback my-release 1
# Rollback was a success! REVISION: 3
```

### helm uninstall
```bash
helm uninstall my-release
# release "my-release" uninstalled
```

### helm repo
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm repo list
```

### helm search
```bash
helm search repo nginx
# NAME            CHART VERSION   APP VERSION
# bitnami/nginx   15.4.4          1.25.3
```

---

## Task 2: Complete Rollback Workflow

```bash
# Install
helm install demo-app ./my-app --set image.tag=1.21
# REVISION: 1

# Upgrade 1
helm upgrade demo-app ./my-app --set image.tag=1.25
# REVISION: 2

# Upgrade 2 (simulate bad deploy)
helm upgrade demo-app ./my-app --set image.tag=99.99-broken
# REVISION: 3 - pods fail with ErrImagePull

# Rollback to revision 2
helm rollback demo-app 2
# Rollback was a success! REVISION: 4 (rollback = new revision)

helm history demo-app
# REVISION  STATUS      DESCRIPTION
# 1         superseded  Install complete
# 2         superseded  Upgrade complete
# 3         superseded  Upgrade complete
# 4         deployed    Rollback to 2

kubectl get pods
# demo-app-xxx   1/1   Running   0   30s  (nginx:1.25 restored!)
```
