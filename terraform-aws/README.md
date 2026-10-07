# Session 18: Terraform and Infrastructure as Code

**Student Email:** aditya.24bcs10057@sst.scaler.com  
**Enrollment ID:** 24bcs10057  

---

## Task 1: Terraform S3 Demo

### Project Structure
```
terraform-s3-demo/
  main.tf
  variables.tf
  outputs.tf
  provider.tf
  terraform.tfvars
  README.md
```

### provider.tf
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.5.0"
}

provider "aws" {
  region = var.aws_region
}
```

### variables.tf
```hcl
variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
}

variable "environment" {
  description = "Environment tag"
  type        = string
  default     = "dev"
}
```

### main.tf
```hcl
resource "aws_s3_bucket" "demo_bucket" {
  bucket = var.bucket_name
  tags = {
    Name        = var.bucket_name
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

resource "aws_s3_bucket_versioning" "demo_versioning" {
  bucket = aws_s3_bucket.demo_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "demo_encryption" {
  bucket = aws_s3_bucket.demo_bucket.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

### outputs.tf
```hcl
output "bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.demo_bucket.bucket
}

output "bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.demo_bucket.arn
}
```

### terraform.tfvars
```hcl
aws_region  = "us-east-1"
bucket_name = "devops-hw-demo-bucket-2026"
environment = "dev"
```

### Terraform Workflow Executed
```bash
# Initialize
terraform init
# Initializing the backend...
# Initializing provider plugins...
# - Finding hashicorp/aws versions matching "~> 5.0"...
# - Installing hashicorp/aws v5.31.0...
# Terraform has been successfully initialized!

# Format
terraform fmt
# main.tf

# Validate
terraform validate
# Success! The configuration is valid.

# Plan
terraform plan
# Plan: 3 to add, 0 to change, 0 to destroy.
# + aws_s3_bucket.demo_bucket
# + aws_s3_bucket_versioning.demo_versioning
# + aws_s3_bucket_server_side_encryption_configuration.demo_encryption

# Apply
terraform apply -auto-approve
# aws_s3_bucket.demo_bucket: Creating...
# aws_s3_bucket.demo_bucket: Creation complete after 3s [id=devops-hw-demo-bucket-2026]
# Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

# Show
terraform show
# aws_s3_bucket.demo_bucket:
#   bucket = "devops-hw-demo-bucket-2026"
#   arn = "arn:aws:s3:::devops-hw-demo-bucket-2026"

# Output
terraform output
# bucket_arn = "arn:aws:s3:::devops-hw-demo-bucket-2026"
# bucket_name = "devops-hw-demo-bucket-2026"

# Destroy
terraform destroy -auto-approve
# Destroy complete! Resources: 3 destroyed.
```

---

## Task 2: AWS Services Research

### 01. IAM (Identity and Access Management)
- **What is IAM?** Controls who can access AWS services and what they can do
- **Users:** Individual AWS identities (people/applications)
- **Groups:** Collections of users sharing same permissions
- **Roles:** Temporary identities assumed by services/apps
- **Policies:** JSON documents defining allowed/denied actions
- **Least Privilege:** Grant only the minimum permissions needed
- **Best Practices:** MFA, no root access for daily work, rotate keys

### 02. EC2 (Elastic Compute Cloud)
- **What is EC2?** Virtual servers in the cloud
- **AMI:** Amazon Machine Image - template for instance OS and software
- **Instance types:** t3.micro (general), c5 (compute), r5 (memory), p3 (GPU)
- **Key pairs:** SSH public/private keys for secure login
- **Security Groups:** Virtual firewall for inbound/outbound traffic
- **EBS:** Elastic Block Store - persistent disk for EC2
- **Instance Lifecycle:** Pending -> Running -> Stopping -> Stopped -> Terminated

### 03. S3 (Simple Storage Service)
- **What is S3?** Object storage for unlimited data
- **Buckets:** Containers for objects (globally unique names)
- **Objects:** Files with metadata, up to 5TB each
- **Storage Classes:** Standard, Intelligent-Tiering, Glacier, Glacier Deep Archive
- **Versioning:** Keep multiple versions of same object
- **Encryption:** SSE-S3, SSE-KMS, SSE-C
- **Use cases:** Backups, static websites, data lakes, media storage

### 04. VPC (Virtual Private Cloud)
- **What is VPC?** Isolated virtual network in AWS
- **CIDR:** IP address range (e.g., 10.0.0.0/16 = 65,536 IPs)
- **Subnets:** Subdivisions of VPC (public or private)
- **Route Tables:** Control traffic routing between subnets/internet
- **Internet Gateway:** Enables internet access for public subnets
- **NAT Gateway:** Lets private subnets reach internet (outbound only)
- **Security Groups:** Stateful firewall at instance level
- **Network ACLs:** Stateless firewall at subnet level

### 05. DynamoDB and RDS

**DynamoDB (NoSQL):**
- Fully managed NoSQL key-value/document database
- Tables, Items (rows), Attributes (columns)
- Partition Key (required), Sort Key (optional)
- Use cases: Gaming leaderboards, IoT, session data, shopping carts

**RDS (Relational Database Service):**
- Managed relational DB (MySQL, PostgreSQL, Oracle, SQL Server, MariaDB, Aurora)
- Automated backups, Multi-AZ for high availability
- Read replicas for performance
- Use cases: Traditional apps, e-commerce, ERP systems
