#!/bin/bash
# Soft Link and Hard Link Demonstration Script

echo "1. Creating original file..."
echo "DevOps Linux Fundamentals" > original.txt

echo "2. Creating Hard Link..."
ln original.txt hardlink.txt

echo "3. Creating Soft Link (Symlink)..."
ln -s original.txt softlink.txt

echo "4. Checking Inodes and details:"
ls -li original.txt hardlink.txt softlink.txt

echo "5. Deleting original file..."
rm original.txt

echo "6. Testing reading from Hard Link:"
cat hardlink.txt

echo "7. Testing reading from Soft Link (expected to fail):"
cat softlink.txt

echo "Cleaning up links..."
rm -f hardlink.txt softlink.txt
