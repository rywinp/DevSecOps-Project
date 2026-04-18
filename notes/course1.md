# AWS Security Fundamentals (Second Edition)

### Course Introduction

We will learn how to leverage
- AWS Config
- AWS CloudTrail
  
to track our AWS resources and review event history

#### 7 Design Principles for Security
1) Have a strong identity foundation
   - Have minimal privileges
2) Enable traceability
   - Ability to monotor, alert, and audit actions in our environment
3) Security at all layers, not just one outer layer
4) Ability to **automate** security into your application
5) Protecting data in transit and at rest
   - During network requests and in database?
6) Principle of least privilege
   - Similiar to Rule 1, Have least privilege
   - Deny everything, and then grant access as needed
7) Prepare for secuirty events
   - Have an incident management process

![alt text](./images/security-responsibilities.png)

### AWS Global Infrastructure

Multiple Physical Data Centers are grouped together into logical units called **Availability Zones**

Multiple Availability Zones are grouped together in a **Region**

We must select which AWS Region to host our resource. Factors to choosing a region includes
- End User's location
- Cost
- Compliances to laws

Not every Region offers all AWS Services so we need to consider the services we need (now and in the future)

## AWS Actions to secure the cloud

### Data Center Security
- AWS Data centers have physical security in place
- AWS considers environmental risks when choosing data center locations
- Ensure climate control and power is reliable at the data centers
  
### Compliance and Governance
- AWS obtains certifications and independent third-party attestations
- Ensures their cloud infrastructure is secure

**NOTE:** It is our responsibility to secure our application and architectures

### AWS Artifacts
- AWS's security and compliance reports for customers to check

## Security INSIDE the cloud

How to create applications and design architectures in the cloud that are **secure**

