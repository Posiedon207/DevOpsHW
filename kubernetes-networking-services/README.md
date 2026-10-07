# Session 11: Kubernetes Networking and Services

**Student:** posiedon2212@gmail.com
**Enrollment ID:** DEV-HW-2026

---

## Task 1: All 5 Kubernetes Service Types

### 1. ClusterIP (Default)
Internal-only service. Only reachable from within the cluster.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: backend-clusterip
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
  - port: 80
    targetPort: 80
```

Output:
```
kubectl get svc backend-clusterip
NAME               TYPE        CLUSTER-IP     PORT(S)
backend-clusterip  ClusterIP   10.96.45.123   80/TCP
```

### 2. NodePort
Exposes on each Node IP at a static port (30000-32767).

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-nodeport
spec:
  type: NodePort
  selector:
    app: frontend
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
```

Output:
```
kubectl get svc frontend-nodeport
NAME               TYPE       CLUSTER-IP    PORT(S)
frontend-nodeport  NodePort   10.96.100.1   80:30080/TCP
```

### 3. LoadBalancer
Provisions cloud load balancer. On Minikube, use `minikube tunnel`.

```
kubectl get svc app-lb
NAME     TYPE           CLUSTER-IP     EXTERNAL-IP
app-lb   LoadBalancer   10.96.200.50   <pending>
```

### 4. ExternalName
Maps service name to an external DNS hostname.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-db
spec:
  type: ExternalName
  externalName: mydb.example.com
```

### 5. Headless Service
No ClusterIP. DNS returns individual Pod IPs (used with StatefulSets).

```yaml
apiVersion: v1
kind: Service
metadata:
  name: headless-svc
spec:
  clusterIP: None
  selector:
    app: stateful-app
  ports:
  - port: 80
```

---

## Task 2: Kubernetes Object Comparison

### Deployment vs ReplicaSet

| Aspect | Deployment | ReplicaSet |
|--------|-----------|------------|
| Purpose | Manage updates and rollbacks | Maintain Pod count |
| Rolling Updates | Yes | No |
| Rollback | Yes | No |
| Use Case | Primary app resource | Managed by Deployment |

### Deployment vs DaemonSet vs StatefulSet

| Aspect | Deployment | DaemonSet | StatefulSet |
|--------|-----------|-----------|-------------|
| Use Case | Stateless apps | Node-level daemons | Stateful apps |
| Pod per Node | No | Yes (one per node) | No |
| Stable Identity | No | No | Yes |
| Examples | Nginx, APIs | Fluentd, Prometheus Node Exporter | MySQL, Kafka |

### ReplicaSet vs Service

| Aspect | ReplicaSet | Service |
|--------|-----------|---------|
| Role | Ensure Pod replicas exist | Expose Pods to network |
| Provides | Pod availability | Stable IP + Load balancing |

---

## Task 3: FQDN in Kubernetes

Naming convention: `<service-name>.<namespace>.svc.cluster.local`

Examples:
- `backend.default.svc.cluster.local`
- `mysql.production.svc.cluster.local`
- `mysql-0.mysql-headless.default.svc.cluster.local` (StatefulSet Pod)

Within same namespace: use service name directly.
Cross-namespace: must use full FQDN.

---

## Task 4: CoreDNS

CoreDNS is the default DNS server in Kubernetes (replaced kube-dns in v1.13+).

Service Discovery Flow:
1. Pod queries service name
2. Query sent to CoreDNS (at kube-dns ClusterIP)
3. CoreDNS resolves to Service ClusterIP
4. kube-proxy routes traffic to a healthy Pod

Troubleshooting:
```bash
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl run dns-test --image=busybox --rm -it -- nslookup kubernetes.default
kubectl exec -it <pod> -- cat /etc/resolv.conf
```
