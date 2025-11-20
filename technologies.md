# Technologies Used

## CloudTrail
Collects all API calls for auditing and forensics. Provides the baseline telemetry for SIEM ingestion.

## VPC Flow Logs
Captures accepted and rejected network connections. Useful for lateral movement detection.

## Amazon GuardDuty
Applies machine learning and threat intelligence to identify anomalous behavior such as unusual IAM activity, port scanning, or credential compromise.

## AWS Security Hub
Aggregates findings from GuardDuty, IAM Access Analyzer, AWS Config, and other security services.

## AWS Config
Evaluates resource compliance against policies. This project includes a rule that checks whether IAM users have MFA enabled.

## IAM Access Analyzer
Identifies overly-permissive access paths and unintended external access.

## AWS Lambda
Hosts the automated remediation logic that disables or revokes IAM access during high-severity incidents.

## Amazon SNS
Delivers notifications to security teams when automated remediation occurs.

## Kinesis Firehose
Streams logs and findings into SIEM platforms (Splunk or ELK Stack) with minimal infrastructure.

## Splunk / ELK
Provides SOC dashboards, alerting, and threat correlation analytics.

