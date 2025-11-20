# Lessons Learned

- IAM permissions are critical for automated remediation. Lambda requires explicit permissions to disable keys or detach policies.
- Testing AWS CLI commands before embedding them into automation avoids debugging issues during CodeBuild or pipelines.
- YAML indentation errors cause silent failures in CodeBuild; multi-line scripts require literal block formatting.
- Kinesis Firehose ingestion must be validated with sample logs before connecting to Splunk or ELK.
- Maintaining a clean GitHub repo structure improves readability and long-term maintainability.
