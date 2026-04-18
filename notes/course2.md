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
- Roles are attached to an AWS Services and that service recieves credentials to use them for API calls
- Example
  - On an EC2 instance, you can request the security credentials (roles attached to this EC2 instance) and make API request to access other AWS resources
- **Temporary** credentials are issued, making it more secure instead of something that is permanent

Federated Users
- We can allow **existing users** in our enterprise to have access to AWS resources
- No need to create an IAM User for an existing user.

Long-Term Access Keys (Legacy, use IAM roles)
- a permanent key pair used to access an AWS resource

## Task 1

IAM Dashboards -> Users
- Allows you to view users and their permissions
  - I was able to observe they had a console password, a password used to sign into AWS website

IAM Dashboards -> **Users groups**
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
       - *Describe* is a common term used for read operations
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

## Task 2
Putting a user into a group will alow them to inherit the group's permissions via it's policies

## Task 3
When one creates an AWS account, they become the **root user**

Root User
- Owns everything and manages everything

IAM User
- A user that has their access limited by the Root User for AWS resources by policy and permissions

Console Sign-in Link
- The sign-in link for a specific AWS Account (Account ID specifies the unique AWS Account)
- Must sign in as the root user or an IAM user 