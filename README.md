# 🔐 Cloud Threat Detection & Automated Response System

## 🎯 Overview
This project implements **real-time cloud threat detection and automated response** in AWS. It integrates **AWS Security Hub, GuardDuty, IAM Analyzer, and AWS Lambda** to detect security incidents and automatically remediate threats.

## 🚀 Key Features
✅ **Security Log Monitoring** – Collects logs from **CloudTrail, VPC Flow Logs, and GuardDuty**  
✅ **Threat Detection & Compliance Checks** – Uses **AWS Security Hub & IAM Access Analyzer**  
✅ **Automated Remediation** – **AWS Lambda** triggers responses (e.g., revoking IAM permissions)  
✅ **Security Logging & Alerting** – Sends **alerts via AWS SNS**  

---

## 📜 **Architecture Diagram**
This diagram illustrates the security architecture:

![Cloud Security Architecture](architecture/cloud_security_diagram.jpeg)

---

## 🏗️ **Technology Stack**
- **AWS Services:** AWS CloudTrail, AWS GuardDuty, AWS Security Hub, AWS Lambda, AWS IAM Analyzer, AWS SNS  
- **Security Automation:** AWS CodeBuild, Terraform, Checkov  
- **CI/CD Pipeline:** GitHub → AWS CodeBuild  
- **Logging & Analysis:** AWS CloudWatch, AWS Kinesis Firehose  

---

## 🛠️ **Deployment Guide**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/Cloud-Security-Projects.git
cd cloud-threat-detection
