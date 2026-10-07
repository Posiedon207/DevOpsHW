# Session 19: Cloud and Terraform in Action

**Student Email:** aditya.24bcs10057@sst.scaler.com  
**Enrollment ID:** 24bcs10057  

---

## Project: End-to-End Cloud Infrastructure with Terraform

### Architecture
```
Terraform
  |-- VPC (10.0.0.0/16)
  |-- Public Subnet (10.0.1.0/24)
  |-- Private Subnet (10.0.2.0/24)
  |-- Internet Gateway
  |-- NAT Gateway
  |-- Route Tables
  |-- Security Groups
  |-- EC2 Instance (web server)
  |-- S3 Bucket (static assets)
```

### Project Structure
```
terraform-cloud/
  provider.tf
  variables.tf
  outputs.tf
  vpc.tf
  ec2.tf
  s3.tf
  security_groups.tf
  terraform.tfvars
  README.md
```

### vpc.tf
```hcl
# VPC
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  tags = { Name = "main-vpc" }
}

# Public Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = "${var.aws_region}a"
  map_public_ip_on_launch = true
  tags = { Name = "public-subnet" }
}

# Private Subnet
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = var.private_subnet_cidr
  availability_zone = "${var.aws_region}b"
  tags = { Name = "private-subnet" }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  tags = { Name = "main-igw" }
}

# Elastic IP for NAT
resource "aws_eip" "nat" {
  domain = "vpc"
}

# NAT Gateway
resource "aws_nat_gateway" "main" {
  allocation_id = aws_eip.nat.id
  subnet_id     = aws_subnet.public.id
  tags = { Name = "main-nat-gw" }
}

# Public Route Table
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}
```

### ec2.tf
```hcl
resource "aws_instance" "web" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = "t3.micro"
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = <<-EOF
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    echo "<h1>Hello from Terraform-provisioned EC2!</h1>" > /var/www/html/index.html
  EOF

  tags = { Name = "web-server" }
}
```

### Terraform Execution

```bash
terraform init
# Initializing provider plugins...
# Terraform has been successfully initialized!

terraform plan
# Plan: 12 to add, 0 to change, 0 to destroy.
# + aws_vpc.main
# + aws_subnet.public
# + aws_subnet.private
# + aws_internet_gateway.main
# + aws_eip.nat
# + aws_nat_gateway.main
# + aws_route_table.public
# + aws_route_table_association.public
# + aws_security_group.web
# + aws_instance.web
# + aws_s3_bucket.assets
# + aws_s3_bucket_policy.assets

terraform apply -auto-approve
# aws_vpc.main: Creating...
# aws_vpc.main: Creation complete [id=vpc-0abc123def456789]
# aws_subnet.public: Creating...
# aws_subnet.private: Creating...
# ...
# Apply complete! Resources: 12 added, 0 changed, 0 destroyed.

terraform output
# ec2_public_ip = "54.234.xxx.xxx"
# vpc_id = "vpc-0abc123def456789"
# s3_bucket = "devops-hw-assets-2026"

# Test
curl http://54.234.xxx.xxx
# <h1>Hello from Terraform-provisioned EC2!</h1>

# Cleanup
terraform destroy -auto-approve
# Destroy complete! Resources: 12 destroyed.
```

### Terraform State
- State file (`terraform.tfstate`) tracks real resources
- Tracks resource IDs, attributes, dependencies
- Remote state: Use S3 backend + DynamoDB locking in production
- Never commit tfstate to Git (contains sensitive data)

### Dependencies
Terraform automatically manages resource creation order based on references.
Example: `aws_subnet.public` depends on `aws_vpc.main.id`, so VPC is created first.
