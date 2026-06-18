# `AWS Cost Optimization Using Lambda Automation`

## Project Overview

This project is a serverless automation solution designed to reduce unnecessary AWS storage costs by automatically identifying and deleting unused EBS snapshots. 

The project leverages AWS Lambda and Python (Boto3) to scan EBS snapshots, verify their associated volumes, and remove orphaned snapshots linked to deleted or unattached volumes.

By automating the cleanup process, the solution improves resource utilization, minimizes storage expenses, and helps maintain a cost-efficient AWS environment.

-----
## Techs and AWS Services used 
1. Amazon EC2
2. Amazon EBS
3. AWS Lambda
4. IAM
5. Python boto3
6. JSON
-----

## Tasks Performed
### 1: Infrastructure Setup
- Created an EC2 instance
- Attached an EBS volume
- Generated EBS snapshots for testing

### 2: IAM Configuration
- Created a Lambda execution role
- Granted snapshot and volume management permissions

### 3: Lambda Automation
- Developed a Python (Boto3) Lambda function
- Retrieved and analyzed EBS snapshots
- Automated snapshot cleanup

### 4: Resource Validation
- Verified volume existence and attachment status
- Deleted orphaned or unused snapshots
------

## Project Workflow

         Create AWS Resources
                ↓
         Generate EBS Snapshots
                ↓
         Configure IAM Role
                ↓
         Develop Lambda Function
                ↓
         Identify Unused Snapshots
                ↓
         Delete Stale Snapshots
                ↓
         Optimize AWS Storage Costs
------

## My Learnings
- Gained hands-on experience with AWS Lambda and serverless automation
- Learned to use Boto3 for AWS resource management
- Understood EBS snapshots and storage optimization
- Automated cloud resource cleanup using Python
- Knowledge on AWS cost optimization practices
- Identified and removed unused resources
----

## Project Insights

Successfully automated EBS snapshot cleanup using AWS Lambda and Python, reducing unnecessary storage costs while gaining hands-on experience in AWS cost optimization, serverless automation, and cloud resource management.

-----
