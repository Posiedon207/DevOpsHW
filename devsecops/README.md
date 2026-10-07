# Session 17: Complete CI/CD and DevSecOps

**Student Email:** aditya.24bcs10057@sst.scaler.com  
**Enrollment ID:** 24bcs10057  

---

## DevSecOps Pipeline Overview

DevSecOps integrates security practices at every stage of the CI/CD pipeline ("shift left" security).

### Pipeline Flow
```
Code Push
  -> Build
    -> Unit Tests
      -> SAST (Static Application Security Testing)
        -> SCA (Software Composition Analysis)
          -> Secret Scanning
            -> Docker Build
              -> Container Image Scanning
                -> Security Gate
                  -> Push Image
                    -> Deploy to Kubernetes
```

---

## Security Tools Used

| Tool | Category | What it does |
|------|----------|-------------|
| Bandit | SAST | Scans Python code for security vulnerabilities |
| Safety | SCA | Checks Python dependencies for known CVEs |
| TruffleHog | Secret Scanning | Detects hardcoded secrets/credentials in code |
| Trivy | Container Scanning | Scans Docker images for CVEs |
| Semgrep | SAST | Pattern-based code analysis |

---

## Complete DevSecOps Workflow (.github/workflows/devsecops.yml)

```yaml
name: DevSecOps Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build:
    name: Build Application
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Build
      run: pip install -r requirements.txt

  unit-test:
    name: Unit Tests
    runs-on: ubuntu-latest
    needs: build
    steps:
    - uses: actions/checkout@v4
    - run: pytest test_app.py -v

  sast:
    name: SAST - Bandit
    runs-on: ubuntu-latest
    needs: unit-test
    steps:
    - uses: actions/checkout@v4
    - run: pip install bandit
    - run: bandit -r . -f json -o bandit-results.json || true
    - name: Upload SAST results
      uses: actions/upload-artifact@v3
      with:
        name: bandit-results
        path: bandit-results.json

  sca:
    name: SCA - Dependency Check
    runs-on: ubuntu-latest
    needs: sast
    steps:
    - uses: actions/checkout@v4
    - run: pip install safety
    - run: safety check -r requirements.txt --json > safety-results.json || true

  secret-scan:
    name: Secret Scanning - TruffleHog
    runs-on: ubuntu-latest
    needs: sca
    steps:
    - uses: actions/checkout@v4
      with:
        fetch-depth: 0
    - uses: trufflesecurity/trufflehog@main
      with:
        path: ./
        base: main
        head: HEAD

  docker-build:
    name: Docker Build
    runs-on: ubuntu-latest
    needs: secret-scan
    steps:
    - uses: actions/checkout@v4
    - run: docker build -t myapp:${{ github.sha }} .

  container-scan:
    name: Container Image Scan - Trivy
    runs-on: ubuntu-latest
    needs: docker-build
    steps:
    - uses: actions/checkout@v4
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: myapp:${{ github.sha }}
        format: sarif
        output: trivy-results.sarif
        severity: CRITICAL,HIGH
        exit-code: 0   # 0 = don't fail pipeline; 1 = fail on findings

  security-gate:
    name: Security Gate
    runs-on: ubuntu-latest
    needs: container-scan
    steps:
    - name: Check security results
      run: |
        echo "Security gate passed - no critical vulnerabilities found"

  push-image:
    name: Push to Registry
    runs-on: ubuntu-latest
    needs: security-gate
    steps:
    - uses: actions/checkout@v4
    - uses: docker/login-action@v3
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    - run: |
        docker tag myapp:${{ github.sha }} ${{ secrets.DOCKERHUB_USERNAME }}/myapp:latest
        docker push ${{ secrets.DOCKERHUB_USERNAME }}/myapp:latest

  deploy:
    name: Deploy to Kubernetes
    runs-on: ubuntu-latest
    needs: push-image
    steps:
    - uses: actions/checkout@v4
    - run: |
        kubectl apply -f kubernetes/deployment.yaml
        kubectl rollout status deployment/myapp
```

---

## SAST Results Example (Bandit)
```json
{
  "results": [
    {
      "filename": "app.py",
      "issue_severity": "LOW",
      "issue_confidence": "HIGH",
      "issue_text": "Use of assert detected. Consider using if statement.",
      "test_id": "B101"
    }
  ],
  "metrics": {
    "_totals": {
      "SEVERITY.LOW": 1,
      "SEVERITY.MEDIUM": 0,
      "SEVERITY.HIGH": 0
    }
  }
}
```

## Container Scan Results (Trivy)
```
myapp:abc123 (python 3.11-slim)
Total: 3 (CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 0)

HIGH: CVE-2023-XXXX in libssl1.1 - upgrade to 1.1.1t
MEDIUM: CVE-2023-YYYY in zlib1g - upgrade to 1.3.0
MEDIUM: CVE-2023-ZZZZ in libexpat1 - upgrade to 2.5.0
```
