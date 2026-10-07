# Session 10: Kubernetes Pods, ReplicaSets and Deployments

**Student:** posiedon2212@gmail.com
**Enrollment ID:** DEV-HW-2026

---

## Task 1: Deployment Strategies

### 01. Rolling Update

YAML file (rolling-update.yaml):
- strategy type: RollingUpdate
- maxSurge: 1, maxUnavailable: 1
- image: nginx:1.21

Commands executed:
- kubectl apply -f rolling-update.yaml
- kubectl set image deployment/my-app-rolling my-app=nginx:1.25
- kubectl rollout status deployment/my-app-rolling

Output observed:
- Pods were replaced one by one
- Old pods stayed running until new pods were Ready
- Zero downtime during the update

### 02. Blue-Green Deployment

Created two deployments: app-blue (nginx:1.21) and app-green (nginx:1.25)
Used a Service to route traffic. Switched traffic by changing selector version label:
- kubectl patch svc my-app-service -p selector version=green
- All traffic instantly switched to green pods
- Blue pods remained running as fallback

### 03. Canary Deployment

Deployed 9 stable replicas + 1 canary replica sharing the same Service selector.
Traffic distribution: ~90% stable, ~10% canary.
Verified both versions serve traffic through the same Service.

### 04. Recreate Deployment

strategy type: Recreate
Result: ALL old pods terminated first, then new pods started.
Observed downtime window between termination and start of new pods.
Use case: When blue-green or rolling is not possible (DB migrations, config changes).

---

## Task 2: Pod Lifecycle

### Pod Lifecycle Phases

| Phase | Description |
|-------|-------------|
| Pending | Pod accepted but not yet running |
| Running | At least one container running |
| Succeeded | All containers exited with code 0 |
| Failed | All containers exited; at least one failed |
| Unknown | State cannot be determined |

### Demo: lifecycle-demo.yaml applied

`ash
kubectl apply -f lifecycle-demo.yaml
# pod/lifecycle-demo created

kubectl get pod lifecycle-demo
# NAME             READY   STATUS    RESTARTS   AGE
# lifecycle-demo   1/1     Running   0          15s

kubectl describe pod lifecycle-demo
# Events:
#   Normal Scheduled  default-scheduler  Successfully assigned default/lifecycle-demo
#   Normal Pulled     kubelet            Container image nginx pulled
#   Normal Created    kubelet            Created container lifecycle-demo-container
#   Normal Started    kubelet            Started container lifecycle-demo-container
`

### Observations
- postStart hook ran immediately after container start
- preStop hook provided graceful shutdown time (sleep 5)
- Pod transitioned: Pending -> ContainerCreating -> Running
- Container restart policy tested with exit code 1 -> CrashLoopBackOff observed

### Container Restart Policies
| Policy | Behavior |
|--------|---------|
| Always | Always restart container on exit (default for Deployments) |
| OnFailure | Restart only on non-zero exit code |
| Never | Never restart |
