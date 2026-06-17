# `AWS Cost Optimization Using Lambda`

## About the Project
This project demonstrates a secure and scalable AWS infrastructure using VPC, private subnets, NAT Gateway, ALB, EC2, and Auto Scaling Group (ASG).

The ALB distributes traffic across EC2 instances hosted in private subnets, while the NAT Gateway provides secure internet access for private servers.

Auto Scaling improves availability and scalability by automatically managing EC2 instances based on traffic demand.

This project provides hands-on experience with AWS networking, load balancing, and real-world DevOps deployment architecture.

-----
## Used AWS Services
1. Virtual Private Cloud (VPC)
2. Auto Scaling Group (ASG)
3. Elastic Cloud Compute (EC2)
4. Target Groups
5. Application Load Balancer (ALB)
6. Security Groups
-----

## Tasks Performed
1. Created VPC with public and private subnets
2. Configured NAT Gateway and Auto Scaling
3. Launched EC2 instances in private subnets
4. Used Bastion Host for SSH access
5. Deployed web application on EC2
6. Configured Target Group and ALB
7. Verified load-balanced traffic flow
8. Access application via Load Balancer DNS Name
------

## Project Workflow
1. User requests are received by the Application Load Balancer (ALB).
2. ALB distributes traffic to healthy EC2 instances through the Target Group.
3. EC2 instances are hosted inside private subnets for enhanced security.
4. Auto Scaling Group (ASG) automatically manages EC2 instances based on traffic demand.
5. NAT Gateway enables private EC2 instances to securely access the internet.
6. The VPC manages networking, routing, and secure communication between resources.

        Users → ALB → Target Group → Private EC2 Instances → ASG Scaling → NAT Gateway → Internet
------

## Learning Outcome
- AWS VPC architecture
- NAT Gateway and ALB setup
- Auto Scaling configuration
- Bastion Host SSH access
- Traffic routing and load balancing
- Gained hands-on AWS deployment experience
----

## Project Insights
This architecture provides a secure and highly available AWS environment using VPC, private subnets, NAT Gateway, ALB, and Auto Scaling to manage traffic distribution, scalability, and secure server communication.

-----
