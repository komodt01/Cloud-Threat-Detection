# Cloud Threat Detection & Automated Response (Design-Only Architecture)

This project documents a cloud-native threat detection and automated response architecture using AWS services. It focuses on how logs, findings, and alerts flow through the environment to detect suspicious activity, forward data to a SIEM, and trigger automated remediation.

This is a **design-only project**: it provides architecture, logic, security controls, and reference implementation examples, but it does not deploy cloud resources.

## Overview

The architecture integrates:
- CloudTrail for API logging
- VPC Flow Logs for network visibility
- GuardDuty for anomaly detection
- Security Hub for centralized findings
- AWS Config for MFA posture checking
- Lambda for automated IAM remediation
- Kinesis Firehose for forwarding logs into a SIEM (Splunk or ELK)
- SNS for security team notifications

## Architecture Summary

1. CloudTrail and VPC Flow Logs generate security-relevant telemetry.
2. GuardDuty analyzes patterns and detects suspicious activity.
3. Security Hub aggregates and normalizes findings.
4. AWS Config enforces MFA posture for IAM users.
5. Kinesis Firehose streams logs to Splunk or ELK.
6. Lambda automatically revokes IAM privileges on high-risk events.
7. SNS notifies security operations of critical actions.
8. All activity is visible in SIEM dashboards for investigation.

## Why This Architecture Matters

- Reduces detection and response time (MTTR)
- Automates credential revocation during compromise events
- Provides a full audit trail of actions
- Supports SOC 2, ISO 27001, HIPAA, PCI, and FedRAMP practices
- Demonstrates practical cloud security engineering skills

## Included Files

- `technologies.md` – describes each AWS service and SIEM component
- `security_requirements.md` – threat model and security objectives
- `risks_and_mitigations.md` – design risks and compensating controls
- `lessonslearned.md` – challenges and solutions encountered
- `revoke_iam_access.py` – example Lambda remediation logic
- `config-rules/AWS_Config_MFA.yml` – MFA enforcement rule for IAM users

