# 🐾 PetClinic - CI/CD Test Automation Suite

A robust end-to-end test automation project for the **Spring PetClinic** application, showcasing advanced QA engineering practices including UI test automation, flaky test handling, parallel execution, reporting, dynamic test data generation, and CI/CD integration using GitHub Actions or Jenkins.

---

## ✅ Features Implemented

- 🔹 UI Test Automation with Selenium + PyTest  
- 🔹 Parallel Test Execution with `pytest-xdist`  
- 🔹 Flaky Test Handling with `pytest-rerunfailures`  
- 🔹 Dynamic Test Data with `Faker`  
- 🔹 HTML Reporting with `pytest-html`  
- 🔹 Screenshot Capture on Test Failure  
- 🔹 Headless Mode & Browser Config Support  
- 🔹 Docker & Kubernetes Support (Minikube)  
- 🔹 CI/CD Pipeline with GitHub Actions or Jenkins  
- 🔹 Test Reports & Artifacts Storage  
- 🔹 Full Documentation and Demo  

---

## 🗓️ 30-Day Plan Overview

| Week     | Focus Areas                                              |
|----------|----------------------------------------------------------|
| Week 1   | Project Setup, Basic Tests (POM), Docker/K8s             |
| Week 2   | HTML Reports, Screenshot Capture, Wait Strategies        |
| Week 3   | Flaky Test Handling, Parallelism, Test Data Strategy     |
| Week 4   | CI/CD Pipeline, Artifacts, Documentation, Demo           |

---

## 🧱 Project Structure

<pre>
petclinic-tests/
├── tests/                 # Test cases
├── pages/                 # Page Object Models
├── conftest.py            # PyTest fixtures
├── pytest.ini             # PyTest configuration
├── requirements.txt       # Python dependencies
├── .github/ or Jenkinsfile# CI/CD configuration
└── README.md              # Project documentation
</pre>

---

## ⚙️ Local Setup Instructions

### 🐳 Option 1: Docker Compose (Fallback Setup)
### ☸️ Option 2: Minikube Kubernetes Setup (Preferred)

## 🧪 Run Tests Locally

## 🚀 CI/CD Setup

# GitHub Actions
- CI Pipeline installs dependencies, runs headless Selenium tests.
- Artifacts (HTML reports + screenshots) are stored for each run.

# Jenkins (Optional)
- Use Jenkinsfile for job configuration.
- Leverages Docker / K8s runners for scalable parallel testing.

📸 Demo & Reporting
- 📂 Screenshots are captured for every failed test.
- 📄 Detailed HTML reports generated via pytest-html.
- 🎥 Loom or GIF demo walkthrough included in the repository.

📘 Resources
- Spring PetClinic
- PyTest Documentation
- Selenium with Python
- GitHub Actions Docs


| Phase                 | % Flaky Tests |
| --------------------- | ------------- |
| Initial               | 40%           |
| After Fixes & Retries | < 10%         |



## 🏁 Final Deliverables
- ✅ Public GitHub Repo with MIT License
- ✅ CI/CD Pipeline (GitHub Actions or Jenkins)
- ✅ Flaky Tests Analysis & Retry Strategy
- ✅ Dynamic Test Data with Faker
- ✅ HTML Reports + Screenshot Evidence
- ✅ Loom/GIF Demo for Showcase
- ✅ Well-Structured README Documentation

## 🙌 Contribute or Fork
Feel free to fork, clone, or open PRs for improvements.
This project is a demonstration of full-stack SDET capabilities and DevOps integration in automation frameworks.

