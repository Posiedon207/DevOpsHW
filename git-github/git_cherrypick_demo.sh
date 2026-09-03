#!/bin/bash
# Git Cherry-Pick Demonstration Script

echo "1. Checking out main branch..."
git checkout main 2>/dev/null || git checkout -b main

echo "2. Making 2 commits on main branch..."
echo "Main Commit 1" > main_demo.txt && git add main_demo.txt && git commit -m "main commit 1"
echo "Main Commit 2" >> main_demo.txt && git add main_demo.txt && git commit -m "main commit 2"

echo "3. Creating feature branch..."
git checkout -b feature-test-branch

echo "4. Making 3 commits on feature branch..."
echo "Feature 1" > feature_demo.txt && git add feature_demo.txt && git commit -m "feature commit 1"
echo "Important Fix" > target_fix.txt && git add target_fix.txt && git commit -m "target bugfix commit"
echo "Feature 2" >> feature_demo.txt && git add feature_demo.txt && git commit -m "feature commit 2"

TARGET_HASH=$(git log --grep="target bugfix commit" --format="%H" -n 1)
echo "Target Commit Hash to Cherry-Pick: $TARGET_HASH"

echo "5. Switching back to main..."
git checkout main

echo "6. Cherry-picking target commit..."
git cherry-pick $TARGET_HASH

echo "7. Verification - Listing recent commits on main:"
git log --oneline -n 3

echo "Cleaning up test branch..."
git branch -D feature-test-branch 2>/dev/null
