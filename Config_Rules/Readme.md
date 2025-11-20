# AWS Config Rules Used in This Architecture

## IAM_USER_MFA_ENABLED
This rule checks whether all IAM users have MFA enabled.  
It supports the threat model by ensuring:

- IAM users cannot authenticate with only a password
- Credential compromise is significantly harder
- Identity misuse is detected early through Config non-compliance

Compliance events from this rule are forwarded to Security Hub and can trigger notifications or automated workflows.

