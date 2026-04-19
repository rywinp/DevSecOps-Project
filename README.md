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

As for the Resource, I stated that the IAM user has permission for this bucket "arn:aws:s3:::secops-assignment-rywin/*"

The reason why I added the wildcard * at the end is because when we use the put_object api call, we must specify the Key for the object we are uploading.
The Key acts as a path that is appended to the bucket resource so we essentially allow this IAM user to upload any objects with any Key name.

### Block 3 - FastAPI App

I know the specifications of this assignment is to use the permissions of an IAM User to access AWS resources in our FastAPI Application via Access Keys, but I learned during block one that there exists IAM Roles. If we were to deploy this application on the cloud, it would be better to use IAM Roles instead of an access key because AWS is able to issue temporary credentials to the application via permissions allowed by the IAM Role that is attached to our server on AWS (possibly on an EC2 server). These temporary credentials are rotated automatically as well. We also wouldn't need to create or manage an IAM User.

Currently, FastAPI leverages Uvicorn to run the server locally. Uvicorn itself accepts HTTP requests, but isn't ideal as a public entry point. If we were to deploy this application for clients in production, we need to secure the traffic by using TLS. AWS Security Fundamentals states that data must be protected at rest and **in transit**. Nginx is a popular tool used as a reverse proxy that will listen on the public port and proxies it to our application which would be hosted locally. TLS configuration is usually handled by Nginx on this reverse proxy layer. To configure HTTPS, we would need to obtain a certificate as well.

