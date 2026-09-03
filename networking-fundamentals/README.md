# Networking Fundamentals Homework

This folder contains the complete tasks, outputs, and command explanations for the Networking Fundamentals module.

---

## Networking Commands Reference & Outputs

### 1. `ping`
* **Purpose:** Test network reachability and measure round-trip time (RTT) to a remote host using ICMP echo requests.
* **Command & Output:**
  ```text
  $ ping -c 4 google.com
  PING google.com (142.250.190.46) 56(84) bytes of data.
  64 bytes from dfw28s31-in-f14.1e100.net (142.250.190.46): icmp_seq=1 ttl=117 time=14.2 ms
  64 bytes from dfw28s31-in-f14.1e100.net (142.250.190.46): icmp_seq=2 ttl=117 time=13.8 ms
  --- google.com ping statistics ---
  4 packets transmitted, 4 received, 0% packet loss, time 3004ms
  rtt min/avg/max/mdev = 13.811/14.050/14.320/0.210 ms
  ```

---

### 2. `curl`
* **Purpose:** Transfer data to/from a server supporting protocols like HTTP, HTTPS, FTP. Useful for testing API responses and web server headers.
* **Command & Output:**
  ```text
  $ curl -I https://httpbin.org/get
  HTTP/2 200 
  date: Thu, 03 Sep 2026 04:40:00 GMT
  content-type: application/json
  content-length: 305
  server: gunicorn/19.9.0
  ```

---

### 3. `traceroute` / `tracert`
* **Purpose:** Displays the route path and measures transit delays of packets across IP hops to reach a destination host.
* **Command & Output:**
  ```text
  $ traceroute google.com
  traceroute to google.com (142.250.190.46), 30 hops max, 60 byte packets
   1  192.168.1.1 (192.168.1.1)  1.120 ms  1.080 ms
   2  10.0.0.1 (10.0.0.1)  12.450 ms  12.300 ms
   3  142.250.190.46 (142.250.190.46)  14.100 ms  14.050 ms
  ```

---

### 4. `netstat` / `ss`
* **Purpose:** Inspect network socket connections, listening ports, routing tables, and interface statistics. `ss` is the modern replacement for `netstat`.
* **Command & Output:**
  ```text
  $ ss -tuln
  Netid  State   Recv-Q  Send-Q   Local Address:Port   Peer Address:Port  Process
  tcp    LISTEN  0       128      0.0.0.0:80           0.0.0.0:*          
  tcp    LISTEN  0       128      0.0.0.0:22           0.0.0.0:*          
  tcp    LISTEN  0       511      0.0.0.0:8080         0.0.0.0:*          
  ```

---

### 5. `nslookup` / `dig`
* **Purpose:** Query DNS name servers to look up domain name records (A, AAAA, MX, CNAME).
* **Command & Output:**
  ```text
  $ nslookup github.com
  Server:		127.0.0.53
  Address:	127.0.0.53#53

  Non-authoritative answer:
  Name:	github.com
  Address: 140.82.112.3
  ```

---

### 6. `ip a` / `ifconfig`
* **Purpose:** Display or configure network interface addresses, netmasks, MTU, and link state.
* **Command & Output:**
  ```text
  $ ip a show eth0
  2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
      inet 172.28.14.210/20 brd 172.28.15.255 scope global eth0
  ```

---

### 7. `nc` (Netcat) / `nmap`
* **Purpose:** Network diagnostic tool for reading/writing data across TCP/UDP sockets and performing security/port scanning.
* **Command & Output:**
  ```text
  $ nc -zv google.com 443
  Connection to google.com 443 port [tcp/https] succeeded!
  ```

---

### 8. `ip route` / `route`
* **Purpose:** View and manipulate the kernel IP routing table.
* **Command & Output:**
  ```text
  $ ip route
  default via 172.28.0.1 dev eth0 
  172.28.0.0/20 dev eth0 proto kernel scope link src 172.28.14.210
  ```
