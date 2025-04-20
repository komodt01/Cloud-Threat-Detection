provider "aws" {
  region = "us-east-1"
}

# Enables Security Hub for the account
resource "aws_securityhub_account" "example" {
  enable_default_standards = true
}

# Lambda function for automated remediation
resource "aws_lambda_function" "revoke_iam_access" {
  filename      = "lambda/revoke_iam_access.zip"
  function_name = "RevokeIAMAccess"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "revoke_iam_access.lambda_handler"
  runtime       = "python3.9"
}

# IAM role for Lambda execution
resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}

# IAM policy for Lambda to manage IAM permissions
resource "aws_iam_role_policy" "lambda_policy" {
  name   = "lambda_policy"
  role   = aws_iam_role.lambda_exec.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["iam:DetachUserPolicy", "iam:ListAttachedUserPolicies"]
        Effect   = "Allow"
        Resource = "*"
      }
    ]
  })
}