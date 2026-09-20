# AWS Config Rules

This directory documents AWS Config rules included in the proposed cloud threat detection and automated-response architecture.

## IAM_USER_MFA_ENABLED

`IAM_USER_MFA_ENABLED` is an AWS-managed Config rule used to evaluate whether IAM users have MFA enabled.

### Security Objective

The rule supports identity-security monitoring by identifying IAM users that do not meet the expected MFA posture.

MFA helps reduce the risk that possession of a password alone is sufficient to compromise an IAM user account.

### Role in the Architecture

AWS Config provides configuration and compliance evaluation within the proposed architecture.

MFA non-compliance could be incorporated into broader security workflows such as:

- Security Hub findings and compliance visibility
- Security operations notification
- Investigation and remediation workflows
- Compliance reporting

The specific downstream integrations are architectural design components and are not represented here as a fully deployed workflow.

## Reference Artifact

The repository root contains `AWS_Config_MFA.yml`, which defines the `IAM_USER_MFA_ENABLED` managed rule for IAM users.

This artifact demonstrates how the MFA requirement can be represented as an AWS Config control within the architecture.
