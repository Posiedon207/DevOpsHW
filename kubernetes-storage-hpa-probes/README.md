# Session 13: Kubernetes Storage, HPA and Probes

**Student:** posiedon2212@gmail.com
**Enrollment ID:** DEV-HW-2026

---

## Task 1: Kubernetes Volumes

### emptyDir
Temporary, Pod-lifetime storage. Shared between containers in same Pod.
```yaml
volumes:
- name: tmp-storage
  emptyDir: {}
```
Use case: Scratch space, inter-container data sharing.

### hostPath
Mounts host node path into Pod. Node-specific, not portable.
```yaml
volumes:
- name: host-logs
  hostPath:
    path: /var/log
    type: Directory
```
Use case: Access node logs, testing only.

### PersistentVolume (PV)
Admin-provisioned storage resource in the cluster.
- Has capacity, access modes (ReadWriteOnce, ReadWriteMany)
- Independent of Pod lifecycle

### PersistentVolumeClaim (PVC)
User request for storage. Binds to a matching PV.
- Pod mounts PVC, not PV directly

### StorageClass
Enables dynamic PV provisioning on demand.
- Cloud providers create EBS/GCE disk automatically when PVC created

### Dynamic Provisioning Flow
PVC created -> StorageClass provisions PV -> PVC binds to PV -> Pod mounts PVC

---

## Task 2: HPA Hands-On

Enabled metrics-server on Minikube:
```bash
minikube addons enable metrics-server
```

Deployed HPA:
```bash
kubectl apply -f hpa.yaml
kubectl get hpa
# NAME       TARGETS    MINPODS   MAXPODS   REPLICAS
# hpa-demo   2%/50%     1         10        1
```

Generated load:
```bash
kubectl run load-gen --image=busybox --rm -it -- sh -c   "while true; do wget -qO- http://hpa-demo-svc; done"
```

Observed scaling:
```bash
kubectl get hpa -w
# NAME       TARGETS    REPLICAS
# hpa-demo   2%/50%     1
# hpa-demo   78%/50%    4       <-- scaled up!
# hpa-demo   12%/50%    2       <-- scaled down
# hpa-demo   2%/50%     1

kubectl top pods
# NAME              CPU       MEMORY
# hpa-demo-xxx      450m      12Mi
# hpa-demo-yyy      423m      11Mi

kubectl describe hpa hpa-demo
# Conditions:
#   AbleToScale: True
#   ScalingActive: True
#   ScalingLimited: False
```

---

## Task 3: Liveness and Readiness Probes

### Liveness Probe
Restarts container if check fails.
```yaml
livenessProbe:
  httpGet:
    path: /healthz
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
  failureThreshold: 3
```

### Readiness Probe
Removes pod from Service endpoints if check fails (no traffic sent).
```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### Startup Probe
For slow-starting apps. Disables liveness until startup succeeds.
```yaml
startupProbe:
  httpGet:
    path: /healthz
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```
