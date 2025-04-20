import boto3
import json

def lambda_handler(event, context):
    """
    AWS Lambda function to revoke IAM access for a user based on Security Hub findings.
    
    Args:
        event (dict): Event data from Security Hub or CloudWatch.
        context (object): Lambda context object.
    
    Returns:
        dict: Status code and message indicating success or failure.
    """
    try:
        iam = boto3.client("iam")
        user = event["detail"]["userIdentity"]["userName"]
        print(f"Revoking access for user: {user}")

        # Remove IAM permissions
        attached_policies = iam.list_attached_user_policies(UserName=user)
        for policy in attached_policies["AttachedPolicies"]:
            iam.detach_user_policy(UserName=user, PolicyArn=policy["PolicyArn"])

        return {
            "statusCode": 200,
            "body": json.dumps(f"Revoked access for {user}")
        }
    except Exception as e:
        print(f"Error revoking access: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps(f"Failed to revoke access: {str(e)}")
        }