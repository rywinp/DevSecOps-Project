# DevSecOps-Project

### Block 2 - S3 Bucket

Bucket Versioning - Enabled
- It was defaulted to disabled but I wanted to enable it so that we are able to recover any previous versions for objects stored in this bucket in the case of any incidents.

### Block 2 - IAM Policy Explanation

We need to follow the Least Privilege Principle so I my thought was to only select the lowest permissions required to list objects, read objects, and write objects to a specific bucket.

The actions I chose were

1) s3:PutObject - grants permission to add an object to a bucket
2) s3:GetObject - grants permissions to retrieve objects from an Amazon S3
3) s3:ListBucket - grants permission to list some or all of the objects in an Amazon S3 Bucket (up to 1000)

I didn't select anything else because this IAM User account didn't need any other permissions.