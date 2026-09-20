# Risks and Mitigations

This document identifies key risks associated with the proposed cloud threat detection and automated-response architecture and the controls that should be considered when implementing the design.

## Risk: Automated Remediation Disrupts Legitimate Access

Automated identity remediation could remove permissions from a legitimate IAM user because of an incorrect or insufficiently validated security event.

**Mitigation:**
- Define explicit criteria for triggering automated remediation.
- Reserve destructive automated actions for sufficiently high-confidence events.
- Log all remediation actions.
- Notify security operations when remediation occurs.
- Maintain recovery and exception procedures.
- Consider human approval for actions with significant business impact.

## Risk: Excessive Lambda Permissions

A remediation function with broad IAM permissions could introduce additional security risk if the function or its execution role were compromised.

**Mitigation:**
- Apply least privilege to the Lambda execution role.
- Grant only the IAM actions required by the remediation workflow.
- Restrict applicable resources where practical.
- Monitor and audit use of the remediation role.

## Risk: Incorrect Event Context

Automated remediation depends on receiving sufficient and accurate information about the affected identity.

The reference `revoke_iam_access.py` expects an IAM user name within the incoming event structure.

**Mitigation:**
- Validate event structure before performing remediation.
- Confirm the affected identity and event type.
- Handle missing or unexpected event attributes safely.
- Test automation using representative security events before production use.

## Risk: SIEM Availability or Ingestion Delays

An external SIEM may experience outages, ingestion delays, or integration failures that reduce centralized security visibility.

**Mitigation:**
- Keep AWS-native detection capabilities independent of the external SIEM where practical.
- Monitor telemetry delivery failures.
- Retain source security data for later investigation.
- Test SIEM ingestion paths with representative events.

## Risk: Security Telemetry Gaps

Incorrect CloudTrail, VPC Flow Logs, or other telemetry configuration could create gaps in security visibility.

**Mitigation:**
- Define required logging coverage as an architecture standard.
- Monitor logging configuration for unauthorized changes.
- Protect security logs from modification or deletion.
- Validate that expected telemetry is being generated and retained.

## Risk: Configuration Drift

Security services or configuration controls may drift from the intended architecture over time.

**Mitigation:**
- Use AWS Config or equivalent controls to evaluate selected configuration requirements.
- Review compliance findings.
- Establish remediation or exception processes for identified deviations.

The repository includes `AWS_Config_MFA.yml` as a reference example for evaluating IAM-user MFA posture.

## Risk: False Positives

Threat-detection systems may generate findings that do not represent actual malicious activity.

Automatically acting on every finding could create unnecessary operational disruption.

**Mitigation:**
- Incorporate finding severity, confidence, context, and resource criticality into response decisions.
- Use automated notification or investigation for lower-confidence events.
- Reserve automated containment for scenarios where the associated risk justifies the action.

## Risk: Remediation Without Recovery

Automated containment may successfully stop suspicious activity but leave administrators without a documented way to restore legitimate access.

**Mitigation:**
- Define rollback and recovery procedures before enabling automated remediation.
- Preserve sufficient audit information to understand what action was performed.
- Require appropriate authorization before restoring access.
- Test recovery procedures alongside remediation procedures.

## Risk: Incomplete Security Operations Integration

Automated controls can reduce response time but should not operate without security operations visibility.

**Mitigation:**
- Notify security personnel of significant automated actions.
- Preserve findings and remediation activity for investigation.
- Integrate automated response into incident-response procedures.
- Define ownership for reviewing and resolving security events.

## Architecture Principle

Automation should be proportional to **event confidence, security severity, business impact, and reversibility**.

The objective is not to automate every security response. The objective is to use automation where it can reduce response time without introducing unacceptable operational risk.
