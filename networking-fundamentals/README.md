# Networking Fundamentals Homework

This folder contains my homework tasks, command outputs, and screenshots for the Networking Fundamentals module.

---

## Tasks & Command Summaries

### 1. `ping`
* **My Understanding:** Used to test connectivity to a server and check network latency (round-trip time).
* **Command:** `ping -c 4 google.com`

### 2. `curl`
* **My Understanding:** Used to fetch web pages or test HTTP APIs directly from the terminal.
* **Command:** `curl -I https://httpbin.org/get`

### 3. `traceroute` / `tracert`
* **My Understanding:** Shows the path (network hops) packets take to reach a target IP/domain.
* **Command:** `traceroute google.com`

### 4. `ss` / `netstat`
* **My Understanding:** Shows open network ports, active socket connections, and listening services on the machine. `ss` is the faster modern command.
* **Command:** `ss -tuln`

### 5. `nslookup` / `dig`
* **My Understanding:** Used for DNS lookups to check IP addresses associated with a domain name.
* **Command:** `nslookup github.com`

### 6. `ip a` / `ifconfig`
* **My Understanding:** Displays network interfaces and assigned IP addresses on Linux.
* **Command:** `ip a`

### 7. `nc` (Netcat)
* **My Understanding:** Used for checking port connectivity and testing network sockets.
* **Command:** `nc -zv google.com 443`

### 8. `ip route`
* **My Understanding:** Shows the Linux kernel routing table and default gateway.
* **Command:** `ip route`

---

## Screenshots

### 1. `ping` & `curl` Output
![Ping and Curl Output](./screenshots/networking_ping_curl.png)

### 2. `ss` & `nslookup` Output
![SS and Nslookup Output](./screenshots/networking_ss_nslookup.png)
