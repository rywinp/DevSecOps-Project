# Introduction to AWS Identity and Access Management (IAM)

Identity and Access Management (IAM) is a web service that allows one to oversees AWS resources by managing
- users
- security credentials
- access keys
- permissions

IAM Users
- They have their own individual security credentials
- We can manage what operations an IAM User can perform

IAM Roles
- Predetermined permissions (permission policy) that can be assumed by anyone who needs it

Federated Users
- We can allow **existing users** in our enterprise to have access to AWS resources
- No need to create an IAM User for an existing user.

## Task 1

IAM Dashboards -> Users
- Allows you to view users and their permissions
  - I was able to observe they had a console password, a password used to sign into AWS website

IAM Dashboards -> Users groups
  - Users and groups can be assigned managed policies
    - AWS managed policies
    - Customer managed policies
    - Inline policies
  - All Users and Groups are immediately affected by policy changes

Policy vs Permissions
- A policy is the high level name that contains a set of permissions

IAM Policy Structure
 - Version: version number for the policy
 - Statements: The permissions for a policy
   - Each statement has the following
     - Effect: *Allow* or *Deny*
     - Action: The API calls for an AWS Service (an operation)
       - eg s3:GetObject
     - Resource: The specific resource(s) the action applies to
       - eg Bucket A and Bucket B
       - \* is the wildcard for all resources


## IAM Policy Example
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Describe*",
                "ec2:GetSecurityGroupsForVpc"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:Describe*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "autoscaling:Describe*",
            "Resource": "*"
        }
    ]
}
```

