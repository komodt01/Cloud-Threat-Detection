# Technical Case Study – Cloud Threat Detection & Automated Response

## Technical Objective

Design an AWS cloud security architecture that connects security telemetry, threat detection, configuration monitoring, centralized findings, automated response, notification, and SIEM integration.

The objective is to demonstrate how these capabilities can operate as a coordinated security lifecycle while maintaining governance over automated remediation.

This is a design-focused architecture with selected reference implementation artifacts rather than a fully deployed production environment.

## Security Architecture

The architecture follows this conceptual flow:

**Telemetry → Detection → Findings → Decision → Response → Notification → Investigation**

Each layer addresses a different security responsibility.

## 1. Security Telemetry

### AWS CloudTrail

CloudTrail provides AWS API activity used for auditing, investigation, and incident-response context.

The architecture treats API activity as foundational security telemetry for understanding actions performed within the AWS environment.

### VPC Flow Logs

VPC Flow Logs provide network-flow information that can supplement identity and API telemetry during investigation.

Together, CloudTrail and network telemetry provide visibility across multiple dimensions of cloud activity.

## 2. Threat Detection

Amazon GuardDuty represents the managed threat-detection layer.

Its role in the architecture is to analyze AWS activity and generate findings for potentially suspicious behavior.

Detection is deliberately separated from remediation. A finding provides security information but does not inherently authorize a destructive response.

## 3. Findings Management

AWS Security Hub represents the centralized findings layer.

Security findings can be aggregated into a common security view where they can support:

- Investigation
- Prioritization
- Compliance visibility
- Notification
- Response decisions

The repository's `buildspec.yml` contains a reference example that queries Security Hub for failed compliance findings.

## 4. Configuration Monitoring

AWS Config provides configuration and compliance evaluation.

The repository contains `AWS_Config_MFA.yml`, which defines the AWS-managed:

`IAM_USER_MFA_ENABLED`

rule for IAM users.

This demonstrates how an identity-security requirement can be represented as a configuration control.

AWS Config identifies compliance state; downstream architecture determines what should happen when non-compliance is detected.

## 5. Automated IAM Remediation

The repository includes `revoke_iam_access.py` as a reference Lambda remediation function.

The function:

1. Creates an IAM client using Boto3.
2. Reads the IAM user name from the incoming event.
3. Retrieves managed policies attached directly to the IAM user.
4. Iterates through those policies.
5. Detaches each managed policy.
6. Returns a response indicating the user whose access was processed.

The reference code demonstrates the mechanics of an automated containment action.

It does not represent a complete production remediation workflow.

## 6. Remediation Safeguards

Production automation would require controls beyond the reference Lambda logic.

These include:

- Event-schema validation
- Trigger validation
- Least-privilege Lambda execution permissions
- Error handling
- Remediation logging
- False-positive handling
- Exception management
- Notification
- Approval requirements where appropriate
- Recovery and rollback procedures

Automated response should be proportional to event confidence and business impact.

## 7. Security Notification

Amazon SNS represents the notification layer.

Security operations personnel should receive appropriate notification when significant security findings occur or automated containment actions execute.

Notification provides human visibility into machine-driven security actions.

## 8. SIEM Integration

Amazon Kinesis Data Firehose represents a potential telemetry-delivery mechanism between AWS and an external SIEM.

Splunk or an Elastic-based platform can provide:

- Centralized security dashboards
- Event correlation
- Investigation
- Alerting
- Cross-platform security visibility

The architecture does not make AWS-native detection dependent exclusively on SIEM availability.

This separation helps preserve cloud-native detection capabilities if external security analytics become temporarily unavailable.

## 9. Security Validation Workflow

The repository includes `buildspec.yml` as a reference AWS CodeBuild security-validation workflow.

The file demonstrates:

- Environment detection
- Terraform installation
- AWS CLI installation
- Checkov installation
- Terraform security scanning with Checkov
- IAM service-access analysis
- Security Hub compliance queries
- Security Hub standards validation

This represents an example of incorporating security validation into an automated workflow rather than evidence of a complete production CI/CD pipeline.

## 10. IAM Security

Identity is a central security domain within the architecture.

The design incorporates:

- MFA posture evaluation
- IAM access analysis
- Least-privilege considerations
- Automated containment concepts

A key architectural concern is ensuring that the remediation mechanism itself does not introduce excessive IAM privilege.

The Lambda execution role should therefore receive only the permissions required by the approved remediation workflow.

## 11. Detection vs. Enforcement

One of the primary architecture decisions is separating detection from enforcement.

A security finding can result in different actions depending on context:

- Logging
- Notification
- Investigation
- Approval
- Automated remediation

This allows response policy to account for severity, confidence, resource criticality, business impact, and reversibility.

## 12. Resilience

External security platforms should enhance AWS security visibility without becoming the sole dependency for threat detection.

AWS-native detection and configuration-monitoring capabilities can continue providing security information independently of the centralized SIEM.

Telemetry delivery and SIEM ingestion should also be monitored so security teams can identify visibility gaps.

## 13. Logging and Forensics

Security telemetry must be protected sufficiently to support investigation.

The architecture identifies requirements for:

- API activity logging
- Network telemetry
- Security findings
- Configuration results
- Remediation activity
- Appropriate retention
- Protection of forensic evidence

These requirements would need to be translated into specific implementation controls during production deployment.

## Technical Tradeoffs

### Automated Response vs. False Positives

Immediate automated containment can reduce response time but increases the impact of an incorrect detection.

### Native AWS Detection vs. Centralized SIEM

AWS-native capabilities provide cloud-specific detection and resilience, while centralized SIEM platforms provide broader enterprise correlation and investigation.

The architecture uses both rather than treating them as mutually exclusive.

### Broad Remediation Permissions vs. Least Privilege

Automation becomes easier when remediation functions have broad permissions, but this increases security risk.

Production implementation should constrain remediation permissions to the minimum actions and resources required.

## Reference Artifacts

The repository contains implementation examples supporting the architecture:

- `AWS_Config_MFA.yml` – MFA configuration-control example
- `revoke_iam_access.py` – IAM remediation logic
- `buildspec.yml` – automated security-validation example
- `security_requirements.md` – security architecture requirements
- `risk_mitigations.md` – architecture risk analysis
- `technologies.md` – component responsibilities
- `Config_Rules/` – AWS Config documentation

These artifacts demonstrate selected portions of the design without implying that the complete architecture was deployed.

## Technical Takeaway

The primary technical lesson is that cloud threat detection is not a single security service.

Effective detection and response requires coordination across:

**logging, network visibility, threat detection, configuration monitoring, findings management, identity controls, automation, notification, SIEM integration, and incident response.**

The architecture deliberately places a decision layer between detection and remediation so automation can improve response speed without turning every security finding into an uncontrolled enforcement action.
