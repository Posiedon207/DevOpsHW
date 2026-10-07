# Session 14: Kubernetes Troubleshooting

**Student Email:** aditya.24bcs10057@sst.scaler.com  
**Enrollment ID:** 24bcs10057  

---

## Task 1: Kubernetes Troubleshooting Commands

### kubectl get
```bash
kubectl get pods                          # List pods
kubectl get pods -o wide                  # With node and IP details
kubectl get all -n my-namespace           # All resources in namespace
kubectl get events --sort-by=.lastTimestamp  # Recent events
```

### kubectl describe
```bash
kubectl describe pod <pod-name>           # Full details + events
kubectl describe node <node-name>         # Node health and capacity
kubectl describe svc <svc-name>           # Service endpoints
```

### kubectl logs
```bash
kubectl logs <pod-name>                   # Current logs
kubectl logs <pod-name> --previous        # Previous container logs
kubectl logs <pod-name> -f                # Follow in real-time
kubectl logs <pod-name> -c <container>    # Specific container
```

### kubectl exec
```bash
kubectl exec -it <pod-name> -- /bin/bash           # Interactive shell
kubectl exec <pod-name> -- curl http://backend     # Test connectivity
kubectl exec <pod-name> -- env | grep DB           # Check env vars
```

### kubectl get events
```bash
kubectl get events
# LAST SEEN  TYPE     REASON    OBJECT       MESSAGE
# 5m         Warning  BackOff   Pod/broken   Back-off restarting failed container
```

### kubectl explain
```bash
kubectl explain pod.spec.containers
kubectl explain deployment.spec.strategy
```

### kubectl top
```bash
kubectl top nodes      # Node resource usage
kubectl top pods       # Pod resource usage
```

---

## Task 2: Common Issues

### CrashLoopBackOff
```bash
kubectl get pods
# broken-app   0/1   CrashLoopBackOff   5   10m

kubectl logs broken-app --previous
# Error: connection refused to database

# Fix: Correct the service/env config, restart pod
kubectl rollout restart deployment my-app
```

### ImagePullBackOff
```bash
kubectl describe pod app-pod | grep -A5 Events
# Warning  Failed  Failed to pull image "wrong-tag": not found

# Fix: Correct image name/tag
kubectl set image deployment/my-app app=correct-image:tag
```

### Pending Pod
```bash
kubectl describe pod pending-pod | grep -A5 Events
# Warning  FailedScheduling  0/1 nodes: Insufficient cpu

# Fix: Free resources or add nodes
```

### Service Connectivity Issues
```bash
# Check endpoints exist
kubectl get endpoints my-service
# NAME         ENDPOINTS
# my-service   <none>    <- Problem! No pods matching selector

# Check labels
kubectl get pods --show-labels
kubectl describe svc my-service | grep Selector
```

### DNS Issues
```bash
kubectl run dns-debug --image=busybox --rm -it -- nslookup kubernetes.default
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns
```
