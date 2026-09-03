# Linux Fundamentals Homework

This folder contains the complete tasks and documentation for the Linux Fundamentals module.

---

## Task 1: Soft Link & Hard Link

### Technical Comparison
| Feature | Soft Link (Symbolic Link / Symlink) | Hard Link |
| :--- | :--- | :--- |
| **Inode** | Has its own unique inode number pointing to target path. | Shares the exact same inode number as the target file. |
| **Data Pointer** | Points to the original file path. | Points directly to the data blocks on disk. |
| **Original File Deletion**| Link becomes broken (dangling symlink). | Data remains accessible via hard link until link count drops to 0. |
| **Cross-Filesystem** | Can span across different filesystems/disks. | Cannot span across different filesystems. |
| **Directories** | Can link to directories. | Cannot link to directories (in standard Linux filesystems). |
| **Creation Command** | `ln -s target link_name` | `ln target link_name` |

### Demonstration Script & Output
Run the helper script [`links_demo.sh`](file:///c:/Users/adigo/OneDrive/Desktop/DevOpsHW/linux-fundamentals/links_demo.sh):
```bash
# 1. Create a sample original file
echo "DevOps Linux Fundamentals" > original.txt

# 2. Create a Hard Link
ln original.txt hardlink.txt

# 3. Create a Soft Link (Symlink)
ln -s original.txt softlink.txt

# 4. Verify inode numbers and link counts
ls -li original.txt hardlink.txt softlink.txt

# 5. Delete original file and test links
rm original.txt
cat hardlink.txt   # Returns: "DevOps Linux Fundamentals"
cat softlink.txt   # Returns: cat: softlink.txt: No such file or directory
```

### Interview Q&A
* **Q: What happens to a hard link when the original file is deleted?**  
  *A:* The data remains intact on disk and accessible through the hard link because the file's inode reference count is decremented by 1 but has not reached 0. The inode and disk data blocks are only reclaimed when all hard links are deleted.
* **Q: Why can't hard links link across different filesystems?**  
  *A:* Inode numbers are unique only within a single filesystem volume. Different filesystems have separate inode tables, so an inode number from filesystem A cannot point to blocks in filesystem B.

---

## Task 2: adduser vs useradd

### Key Differences
* **`useradd`**: Low-level, native system binary (`/usr/sbin/useradd`). It does not create home directories or prompt for passwords automatically unless explicit flags (`-m`, `-p`, `-s`) are supplied. Portable across all Linux distributions.
* **`adduser`**: High-level Perl script wrapper (`/usr/sbin/adduser`) primarily on Debian/Ubuntu. It provides an interactive prompt, automatically creates home directories (`/home/username`), assigns a shell, sets up group memberships, copies `/etc/skel` files, and forces initial password creation.

### Recommended Command on Ubuntu
On Debian and Ubuntu, **`adduser`** is preferred for manual administrative user creation because it enforces best practices interactively without requiring a complex combination of flags.

```bash
# Recommended Ubuntu interactive command:
sudo adduser testuser

# Equivalent non-interactive useradd command:
sudo useradd -m -s /bin/bash -g users testuser
sudo passwd testuser
```

---

## Task 3: journalctl

### Purpose
`journalctl` is the command-line utility used to query and view system logs collected by systemd's logging daemon, `systemd-journald`.

### Commands & Logs
```bash
# 1. View logs for a specific service (e.g., Nginx)
journalctl -u nginx.service --no-pager -n 20

# 2. Follow live real-time logs for a service
journalctl -u docker.service -f

# 3. View logs generated in the last 1 hour
journalctl --since "1 hour ago"

# 4. View logs with Priority level Error or higher
journalctl -p err -b
```

---

## Task 4: Linux Command Cheat Sheet

| Category | Command | Description & Usage Example |
| :--- | :--- | :--- |
| **Navigation & Files** | `ls -la` | List all files including hidden with long format details. |
| | `cd /path` | Change directory. |
| | `pwd` | Print working directory. |
| | `mkdir -p dir` | Create directory (with parent directories if needed). |
| | `rm -rf file` | Remove file or directory recursively & forcefully. |
| | `cp -r src dst` | Copy files or directories recursively. |
| | `mv src dst` | Move or rename files. |
| **Viewing & Search** | `cat file` | Display file contents. |
| | `grep -rn "pat"` | Search pattern recursively with line numbers. |
| | `find . -name "*.log"`| Search directory tree for files matching pattern. |
| | `head -n 10` / `tail` | View top or bottom 10 lines of a file. |
| **Permissions** | `chmod 755 script.sh`| Change file permissions (Read/Write/Execute). |
| | `chown user:group file`| Change file ownership. |
| **Process & Memory** | `ps aux` | List all running processes with user details. |
| | `top` / `htop` | Interactive real-time process monitor. |
| | `kill -9 PID` | Terminate process forcefully by Process ID. |
| | `df -h` | Display human-readable disk space usage. |
| | `free -h` | Display memory (RAM & Swap) utilization. |
| **System & Network** | `systemctl status srv`| Check status of a systemd service. |
| | `journalctl -u srv` | View logs for a systemd service. |
| | `curl -I URL` | Fetch HTTP headers from server. |
| | `ip a` | Show network interfaces and IP addresses. |
