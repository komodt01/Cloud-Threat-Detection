# Risks and Mitigations

## Risk: Overly aggressive remediation can disable legitimate users
Mitigation: Automate only for HIGH and CRITICAL findings; log all actions; notify security.

## Risk: SIEM ingestion delays may hide attack indicators
Mitigation: GuardDuty + Security Hub operate independently of SIEM; local alerts still trigger remediation.

## Risk: IAM permissions on the Lambda remediation function may be insufficient
Mitigation: Define only the required IAM permissions (UpdateAccessKey, DetachUserPolicy).

## Risk: Incorrect Kinesis configuration may drop logs
Mitigation: Test ingestion paths with sample events before connecting to SIEM.

## Risk: CloudTrail misconfiguration can lead to gaps in audit data
Mitigation: Always enable multi-region CloudTrail with log file validation.

## Risk: MFA non-compliance weakens identity security
Mitigation: AWS Config rule `IAM_USER_MFA_ENABLED` is included in this design.
