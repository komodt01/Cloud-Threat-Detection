# Cloud Threat Detection & Automated Response Architecture

## Project Overview

This project presents a design for cloud-native threat detection and automated security response in AWS.

The architecture focuses on how security telemetry, threat findings, compliance signals, automated remediation, and security operations can work together to reduce the time between detection and response.

This is a **design-focused architecture project**. It documents the architecture, security requirements, control logic, and selected reference implementation examples. It does not represent a fully deployed production environment.

## Business Problem

Cloud environments generate large volumes of identity, network, configuration, and API activity.

Security teams need an architecture that can:

- Collect security-relevant telemetry.
- Detect suspicious identity and network behavior.
- Aggregate security findings.
- Identify configuration and compliance issues.
- Notify security operations teams.
- Support automated response to high-risk events.
- Forward security information to centralized monitoring platforms.
- Preserve evidence for investigation and audit.

The architectural challenge is connecting these capabilities into a coordinated detection-and-response workflow rather than operating them as isolated security tools.

## Architecture Approach

The design uses AWS security and monitoring services to represent several layers of the detection-and-response lifecycle.

### Security Telemetry

**AWS CloudTrail** provides API activity that can be used to investigate actions performed within the AWS environment.

**VPC Flow Logs** provide network-flow telemetry that can support network visibility and anomaly investigation.

### Threat Detection

**Amazon GuardDuty** represents the managed threat-detection layer for identifying suspicious activity and potential threats within AWS.

### Findings Aggregation

**AWS Security Hub** provides a centralized location for aggregating and evaluating security findings.

The repository also includes a CodeBuild example that queries Security Hub for failed compliance findings.

### Configuration Monitoring

**AWS Config** is included in the design for evaluating configuration and security posture.

The repository contains an MFA-related AWS Config rule definition as a reference artifact.

### Automated IAM Response

AWS Lambda is used as the reference remediation mechanism.

The included `revoke_iam_access.py` example demonstrates logic that receives an identity-related event, identifies an IAM user, enumerates attached managed policies, and detaches those policies.

This illustrates an automated containment pattern. Production implementations would require additional validation, authorization, exception handling, logging, and safeguards before performing destructive identity actions.

### SIEM Integration

Amazon Kinesis Data Firehose is included in the architecture as the forwarding layer for security telemetry destined for an external SIEM such as Splunk or an Elastic-based platform.

The architecture separates AWS-native detection from centralized security operations so that AWS detection capabilities can continue operating independently of the external SIEM.

### Security Notification

Amazon SNS represents the notification layer for communicating significant security events and automated-response activity to security operations teams.

## Detection and Response Flow

The conceptual security workflow is:

1. CloudTrail and VPC Flow Logs generate security telemetry.
2. AWS-native security services analyze activity and security posture.
3. GuardDuty produces threat findings.
4. Security Hub centralizes security findings.
5. AWS Config evaluates selected configuration requirements.
6. High-risk events can trigger automated Lambda remediation.
7. Security events can be forwarded to centralized SIEM capabilities.
8. SNS can notify security operations teams of significant events or remediation actions.
9. Security teams investigate findings using AWS and SIEM telemetry.

This represents the intended architecture rather than evidence that every component was deployed and integrated in a live environment.

## Security Architecture Principles

### Defense in Depth

The architecture combines multiple security capabilities rather than relying on a single detection mechanism.

Identity activity, network telemetry, threat detection, configuration monitoring, centralized findings, and response automation provide different layers of visibility and control.

### Detection and Response Integration

Detection alone does not contain a threat.

The architecture connects security findings with response mechanisms so selected events can lead to automated containment or security-team notification.

### Controlled Automation

Automated remediation can reduce response time but also introduces operational risk.

Actions such as removing IAM permissions should therefore be governed by clear triggering conditions, appropriate IAM permissions, logging, testing, exception handling, and recovery procedures.

### Security Observability

Security telemetry must provide sufficient information for investigation and response.

CloudTrail, network telemetry, AWS security findings, configuration results, and SIEM data collectively provide visibility into security-relevant activity.

### Resilience of Detection

AWS-native threat detection should not depend entirely on an external SIEM remaining available.

The architecture therefore separates AWS detection and response capabilities from external security analytics and investigation platforms.

## Reference Implementation Artifacts

The repository contains several artifacts supporting the architecture:

- `revoke_iam_access.py` – example Lambda logic for IAM containment.
- `AWS_Config_MFA.yml` – MFA-related AWS Config rule definition.
- `buildspec.yml` – CodeBuild example incorporating Checkov, IAM analysis, and Security Hub validation.
- `security_requirements.md` – detection, response, logging, and availability requirements.
- `risk_mitigations.md` – documented security risks and mitigation considerations.
- `technologies.md` – technologies and services used in the architecture.
- `lessons_learned.md` – implementation and design observations.

Additional AWS Config content is maintained under `Config_Rules/`.

## CodeBuild Security Validation Example

The included `buildspec.yml` demonstrates several security-validation activities within an AWS CodeBuild workflow.

The example includes:

- Installation of Terraform and Checkov.
- Checkov scanning of Terraform content.
- IAM service-access analysis.
- Querying AWS Security Hub for failed compliance findings.
- Verification of enabled Security Hub standards.

This file should be treated as a reference security-validation workflow rather than evidence of a complete CI/CD implementation.

## Security Requirements

The documented architecture includes requirements for:

- Detecting anomalous IAM activity.
- Identifying high-risk GuardDuty findings.
- Capturing AWS API activity.
- Monitoring network activity.
- Evaluating MFA posture.
- Supporting automated identity containment.
- Alerting security operations.
- Forwarding telemetry to centralized security monitoring.
- Preserving security evidence for investigations.
- Maintaining detection capabilities when external monitoring platforms are unavailable.

These requirements describe the intended security properties of the architecture.

## Architecture Tradeoffs

Automated response improves containment speed but increases the importance of accurate detection and appropriate safeguards.

Centralized SIEM integration improves enterprise visibility but introduces an external dependency for centralized investigation.

AWS-native detection capabilities can reduce that dependency by allowing detection and selected response actions to continue within the AWS environment.

The appropriate level of automation should therefore depend on event confidence, business impact, resource criticality, and the reversibility of the remediation action.

## Project Scope

This repository demonstrates **cloud threat detection and automated-response architecture concepts** using AWS services and selected reference implementation artifacts.

It does not represent a complete production deployment.

Production implementation would require additional work including:

- Deployment automation
- IAM permission hardening
- Event-routing configuration
- Remediation approval and exception workflows
- False-positive handling
- Comprehensive logging
- Testing and rollback procedures
- SIEM integration validation
- Operational monitoring
- Incident-response procedures

## Repository Structure

```text
Cloud-Threat-Detection/
├── Config_Rules/
├── AWS_Config_MFA.yml
├── buildspec.yml
├── lessons_learned.md
├── README.md
├── revoke_iam_access.py
├── risk_mitigations.md
├── security_requirements.md
└── technologies.md
