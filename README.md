# Pulumi Kubernetes DevSecOps CI/CD Project

## 🚀 Overview

This project demonstrates a **production-style DevOps & DevSecOps pipeline** using **Pulumi (Python)**, **Kubernetes**, **GitHub Actions**, and **Trivy**.

The goal of this project is to show **end-to-end infrastructure provisioning, application deployment, and security enforcement** using modern DevOps best practices.

The pipeline is designed to run **manually** (via GitHub Actions `workflow_dispatch`) to avoid accidental infrastructure changes.

---

## 🏗️ Architecture

```
Developer
   │
   │  (Manual Trigger)
   ▼
GitHub Actions (CI/CD)
   │
   ├── Build Docker Image
   ├── Trivy Security Scan
   ├── Create Kind Kubernetes Cluster
   ├── Pulumi Deploy (IaC)
   ▼
Kubernetes (kind)
   │
   ├── Namespace
   ├── Deployment (Hardened Container)
   └── Service (NodePort)
```

---

## 🧰 Tech Stack

| Category          | Tool               |
| ----------------- | ------------------ |
| IaC               | Pulumi (Python)    |
| Container         | Docker             |
| Orchestration     | Kubernetes (kind)  |
| CI/CD             | GitHub Actions     |
| Security Scanning | Trivy              |
| Language          | Python (Flask app) |

---

## 🔐 Security & DevSecOps Features

This project intentionally includes **security best practices**:

### ✅ Container Hardening

* Runs as **non-root user**
* Drops all Linux capabilities
* Prevents privilege escalation
* Read-only root filesystem
* CPU & memory limits enforced

### ✅ Image Security

* No `latest` tag usage
* Versioned Docker images
* Trivy image scanning
* Pipeline fails on **CRITICAL vulnerabilities**

### ✅ Policy-as-Code (Pulumi)

* Blocks `:latest` images
* Enforces resource limits
* Stops insecure deployments before they reach Kubernetes

---

## 🔄 CI/CD Workflow

The pipeline is triggered **manually** using `workflow_dispatch`.

### CI/CD Steps

1. Checkout source code
2. Create ephemeral Kubernetes cluster using kind
3. Build Docker image
4. Run Trivy security scan
5. Install Pulumi dependencies
6. Deploy infrastructure and application using Pulumi

If **Trivy fails**, deployment is automatically blocked.

---

## 📁 Repository Structure

```
Pulumi-Project/
├── app/
│   ├── app.py
│   └── Dockerfile
├── infra/
│   ├── __main__.py
│   ├── Pulumi.yaml
│   └── requirements.txt
├── policy/
│   └── __main__.py
├── .github/workflows/
│   └── pulumi-k8s-local.yml
├── .trivyignore
└── README.md
```

---

## ▶️ How to Run Locally

### Prerequisites

* Docker
* kind
* kubectl
* Python 3.10+
* Pulumi CLI

### Steps

```bash
# Build Docker image
docker build -t pulumi-demo:v1 app/

# Create kind cluster
kind create cluster --name pulumi-local

# Load image into kind
kind load docker-image pulumi-demo:v1 --name pulumi-local

# Deploy using Pulumi
cd infra
pulumi up --yes
```

Verify:

```bash
kubectl get pods -n demo-ns
kubectl get svc -n demo-ns
```

---

## 🔍 Trivy Security Scan (Local)

```bash
trivy image pulumi-demo:v1
```

Fail on critical issues:

```bash
trivy image pulumi-demo:v1 --severity CRITICAL --exit-code 1
```

---

## 🧪 Troubleshooting

### ImagePullBackOff

* Ensure image is loaded into kind
* Check `imagePullPolicy: IfNotPresent`

### CrashLoopBackOff

* Check container logs:

```bash
kubectl logs <pod-name> -n demo-ns
```

### Pulumi Errors

* Ensure you are inside `infra/` directory
* Verify `PULUMI_ACCESS_TOKEN` is set

---

## 💬 Interview Talking Points

You can confidently say:

* "I used Pulumi with Python to manage Kubernetes infrastructure"
* "I integrated Trivy into CI/CD as a security gate"
* "I enforced security using policy-as-code"
* "I debugged real Kubernetes issues like ImagePullBackOff and CrashLoopBackOff"

---

## 🚀 Future Improvements

* NetworkPolicies for zero-trust networking
* Helm-based deployments
* Multi-environment stacks (dev/stage/prod)
* Observability (Prometheus + Grafana)
* GitHub Environments with approvals

---

## 👨‍💻 Author

Built as a **hands-on DevOps & DevSecOps learning project** to demonstrate real-world CI/CD, Kubernetes, and security practices.

---
