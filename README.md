# 🔐 Cloud Threat Detection & Automated Response System

![AWS](https://img.shields.io/badge/AWS-CloudSecurity-orange)
![Terraform](https://img.shields.io/badge/Terraform-Infrastructure-blue)
![License](https://img.shields.io/badge/License-MIT-green)

![Cloud Security Architecture](architecture/cloud_security_diagram.jpeg)

## 📝 Overview
This project implements a **real-time cloud threat detection and automated response system** on AWS. It integrates **AWS Security Hub**, **GuardDuty**, **IAM Access Analyzer**, **AWS Lambda**, and **SIEM (Splunk/ELK)** to monitor, detect, and remediate security threats automatically.

## 🚀 Key Features
- **Security Log Monitoring**: Collects logs from CloudTrail, VPC Flow Logs, and GuardDuty.
- **Threat Detection**: Uses AWS Security Hub and IAM Access Analyzer for compliance checks.
- **SIEM Integration**: Forwards logs to Splunk or ELK Stack for analysis.
- **Automated Remediation**: AWS Lambda revokes IAM access for detected threats.
- **Alerting**: Sends notifications via AWS SNS.

## 🏗️ Technology Stack
- **AWS Services**: CloudTrail, GuardDuty, Security Hub, Lambda, IAM Access Analyzer, SNS, Kinesis Firehose, CodeBuild
- **SIEM**: Splunk or ELK Stack
- **Tools**: Terraform, Checkov, AWS CLI
- **CI/CD**: GitHub → AWS CodeBuild
- **Logging**: CloudWatch, Kinesis Firehose

## 📦 Prerequisites
- AWS account with permissions for Security Hub, GuardDuty, Lambda, and IAM.
- Terraform (v1.5.0 or later) installed.
- AWS CLI configured.
- Splunk or ELK Stack for SIEM (optional).

## 🛠️ Deployment Guide
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/cloud-threat-detection.git
   cd cloud-threat-detection