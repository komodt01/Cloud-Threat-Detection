# Technologies

This project uses AWS-native security services and external SIEM concepts to demonstrate a **design for cloud threat detection and automated response**.

The services below represent components of the proposed architecture. Their inclusion does not imply that every service was deployed or integrated in a live AWS environment.

## AWS CloudTrail

**Purpose:** API activity logging and audit visibility.

**Role in the architecture:**  
CloudTrail provides security-relevant AWS API activity that can support threat investigation, incident response, and forensic analysis.

## VPC Flow Logs

**Purpose:** Network traffic visibility.

**Role in the architecture:**  
VPC Flow Logs provide network-flow telemetry that can help identify unexpected communication patterns and support investigation of network activity.

## Amazon GuardDuty

**Purpose:** AWS-native threat detection.

**Role in the architecture:**  
GuardDuty represents the threat-detection layer responsible for identifying suspicious activity and generating findings for further analysis and response.

## AWS Security Hub

**Purpose:** Centralized security findings management.

**Role in the architecture:**  
Security Hub provides a central location for aggregating security findings from AWS security services.

The repository's `buildspec.yml` also contains a reference example that queries Security Hub for failed compliance findings.

## AWS Config

**Purpose:** Configuration and compliance evaluation.

**Role in the architecture:**  
AWS Config represents the configuration-monitoring layer.

The repository includes `AWS_Config_MFA.yml`, which defines the AWS-managed `IAM_USER_MFA_ENABLED` rule for evaluating MFA posture for IAM users.

## IAM Access Analyzer

**Purpose:** IAM access analysis.

**Role in the architecture:**  
IAM Access Analyzer represents an additional identity-security capability for evaluating access and supporting least-privilege decisions.

The `buildspec.yml` contains an example of AWS IAM service-access analysis as part of a security-validation workflow.

## AWS Lambda

**Purpose:** Event-driven security automation.

**Role in the architecture:**  
Lambda represents the automated-remediation component of the design.

The included `revoke_iam_access.py` provides reference logic that identifies an IAM user from an event and detaches the user's attached managed policies.

Production use would require additional validation, authorization, logging, exception handling, and recovery safeguards.

## Amazon SNS

**Purpose:** Security-event notification.

**Role in the architecture:**  
SNS represents the notification layer for informing security operations personnel about significant findings or automated remediation activity.

## Amazon Kinesis Data Firehose

**Purpose:** Security telemetry delivery.

**Role in the architecture:**  
Firehose represents a potential mechanism for forwarding AWS security telemetry to an external security analytics or SIEM platform.

## Splunk / Elastic

**Purpose:** Centralized security monitoring and investigation.

**Role in the architecture:**  
An external SIEM provides centralized dashboards, correlation, investigation, and security operations visibility across security telemetry.

The architecture does not depend exclusively on the SIEM for AWS-native threat detection.

## Checkov

**Purpose:** Infrastructure-as-Code security scanning.

**Role in the repository:**  
The included `buildspec.yml` installs Checkov and demonstrates scanning a Terraform directory for security and configuration issues.

## AWS CodeBuild

**Purpose:** Automated security-validation workflow.

**Role in the repository:**  
The `buildspec.yml` demonstrates how security checks such as Checkov scanning, IAM analysis, and Security Hub queries could be incorporated into a CodeBuild workflow.

This is a reference validation artifact rather than evidence of a complete production CI/CD implementation.

## Architecture Summary

Together, these technologies represent the following security lifecycle:

**Telemetry → Detection → Findings → Decision → Response → Notification → Investigation**

The architecture demonstrates how AWS-native security services, automation, and centralized security monitoring can be combined while maintaining a clear distinction between the **proposed architecture** and the **reference artifacts contained in this repository**.
