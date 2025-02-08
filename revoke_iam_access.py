import boto3

def lambda_handler(event, context):
    iam = boto3.client("iam")
    user = event["detail"]["userIdentity"]["userName"]
    print(f"Revoking access for user: {user}")

    # Remove IAM permissions
    attached_policies = iam.list_attached_user_policies(UserName=user)
    for policy in attached_policies["AttachedPolicies"]:
        iam.detach_user_policy(UserName=user, PolicyArn=policy["PolicyArn"])

    return {"statusCode": 200, "body": f"Revoked access for {user}"}
