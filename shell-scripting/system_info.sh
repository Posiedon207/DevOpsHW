#!/bin/bash
# ==============================================================================
# System Information Script
# DevOps Homework Assignment - Shell Scripting
# ==============================================================================

echo "=================================================="
echo "          SYSTEM INFORMATION REPORT               "
echo "=================================================="

# 1. Variables storing system metrics
CURRENT_DATE=$(date)
HOSTNAME_VAL=$(hostname)
USER_VAL=$(whoami)

echo "Date & Time : $CURRENT_DATE"
echo "Hostname    : $HOSTNAME_VAL"
echo "Username    : $USER_VAL"
echo "--------------------------------------------------"

# 2. Display Disk Usage
echo "Disk Usage:"
df -h
echo "--------------------------------------------------"

# 3. User input using read -p
read -p "Enter a directory name to create for output logs: " DIR_NAME

if [ -z "$DIR_NAME" ]; then
    DIR_NAME="system_logs"
fi

# 4. Create directory using mkdir
echo "Creating directory: $DIR_NAME"
mkdir -p "$DIR_NAME"

# 5. Create a file using touch
LOG_FILE="$DIR_NAME/running_processes.txt"
echo "Creating log file: $LOG_FILE"
touch "$LOG_FILE"

# 6. Store running processes using > output redirection
echo "Redirecting running process details into $LOG_FILE..."
ps aux > "$LOG_FILE" 2>/dev/null || ps -ef > "$LOG_FILE"

echo "--------------------------------------------------"
echo "Process list successfully saved to $LOG_FILE!"
echo "First 10 lines of recorded processes:"
head -n 10 "$LOG_FILE"
echo "=================================================="
