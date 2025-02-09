# 🔐 Cloud Threat Detection & Automated Response System

## 🎯 Overview
This project implements **real-time cloud threat detection and automated response** in AWS. It integrates **AWS Security Hub, GuardDuty, IAM Analyzer, and AWS Lambda** to detect security incidents and automatically remediate threats.

# 🔐 Cloud Threat Detection & Automated Response System

## 🎯 Overview
This project implements **real-time cloud threat detection and automated response** in AWS. It integrates **AWS Security Hub, GuardDuty, IAM Analyzer, and AWS Lambda** to detect security incidents and automatically remediate threats.  
Additionally, security logs are forwarded to **SIEM (Splunk or ELK)** for advanced threat correlation and incident response.

---

# 🔐 Cloud Threat Detection & Automated Response System

## 🎯 Overview
This project implements **real-time cloud threat detection and automated response** in AWS. It integrates **AWS Security Hub, GuardDuty, IAM Analyzer, AWS Lambda, and SIEM (Splunk or ELK)** to detect security incidents, forward security logs for analysis, and automatically remediate threats.

---

## 🚀 Key Features
✅ **Security Log Monitoring** – Collects logs from **CloudTrail, VPC Flow Logs, and GuardDuty**  
✅ **Threat Detection & Compliance Checks** – Uses **AWS Security Hub & IAM Access Analyzer**  
✅ **SIEM Integration** – Security logs are forwarded to **Splunk or ELK** for analysis  
✅ **Automated Threat Remediation** – **AWS Lambda dynamically revokes IAM access for detected threats**  
✅ **Security Logging & Alerting** – Sends **alerts via AWS SNS**  

---

## 📜 **Architecture Diagram**
This diagram illustrates the security architecture, including **SIEM log ingestion and automated threat response**:

![Cloud Security Architecture](architecture/cloud_security_diagram.jpeg)

---

## 🏗️ **Technology Stack**
- **AWS Services:** AWS CloudTrail, AWS GuardDuty, AWS Security Hub, AWS Lambda, AWS IAM Analyzer, AWS SNS  
- **SIEM (Security Information and Event Management):** **Splunk or ELK Stack**  
- **Security Automation:** AWS CodeBuild, Terraform, Checkov  
- **CI/CD Pipeline:** GitHub → AWS CodeBuild  
- **Logging & Analysis:** AWS CloudWatch, AWS Kinesis Firehose  

---

## 🛠️ **Deployment Guide**
### **1️⃣ Clone the Repository**

git clone https://github.com/YOUR_GITHUB_USERNAME/Cloud-Security-Projects.git
cd cloud-threat-detection

2️⃣ Deploy AWS Resources with Terraform
terraform init
terraform apply -auto-approve

3️⃣ Run Security Compliance Checks
checkov -d terraform/
aws securityhub get-findings --filters '{"ComplianceStatus": [{"Value": "FAILED", "Comparison": "EQUALS"}]}' --output json

4️⃣ Configure SIEM (Splunk or ELK)
Splunk:

Install Splunk and enable AWS Kinesis Firehose ingestion
Use Splunk's AWS Security Add-on to parse logs
Query logs using index=aws_security_logs
ELK Stack:

Deploy Logstash with AWS S3 input
Use Kibana to create security dashboards
Query logs with:
{
  "query": {
    "match": { "logGroup": "security-logs" }
  }
}

5️⃣ Deploy AWS Lambda for Automated Threat Remediation
AWS Lambda is triggered when high-risk security events are detected.
It automatically revokes IAM access or disables credentials based on Security Hub findings.
Deploy the Lambda Function
cd lambda/
terraform init
terraform apply -auto-approve

Test AWS Lambda
To manually trigger the function and simulate revoking access:
aws lambda invoke --function-name RevokeIAMAccess output.json

 How Automated Threat Response Works
🔄 How Automated Threat Detection & SIEM Work
1️⃣ AWS GuardDuty detects an anomaly (e.g., suspicious login).
2️⃣ AWS Security Hub aggregates findings.
3️⃣ AWS Kinesis Firehose forwards security logs to SIEM (Splunk/ELK).
4️⃣ SIEM correlates events and raises alerts.
5️⃣ AWS Lambda triggers automated response (e.g., revoking IAM access).
6️⃣ AWS SNS sends notifications to security teams.

🛑 Cleanup: Avoid AWS Charges
terraform destroy -auto-approve
aws securityhub disable-security-hub
aws guardduty disable-organization-admin-account --admin-account-id <AWS_ACCOUNT_ID>
aws iam delete-role --role-name SecurityAdminRole
aws lambda delete-function --function-name RevokeIAMAccess
aws logs delete-log-group --log-group-name security-logs


