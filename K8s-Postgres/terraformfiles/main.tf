terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region  = var.region
}

data "aws_caller_identity" "current" {}

data "aws_region" "current" {}


locals {
  name = "abbabe"   # change here, optional
}


# KUBERNETES CLUSTER MASTER AND WORKER NODE
resource "aws_instance" "master" {
  ami                  = "ami-04505e74c0741db8d"
  instance_type        = "t3a.medium"
  key_name             = var.key-name
  iam_instance_profile = aws_iam_instance_profile.ec2connectprofile.name
  security_groups      = ["${local.name}-k8s-master-sec-gr"]
  user_data            = data.template_file.master.rendered
  tags = {
    Name = "${local.name}-kube-master"
  }
}

resource "aws_instance" "worker" {
  ami                  = "ami-04505e74c0741db8d"
  instance_type        = "t3a.medium"
  key_name             = var.key-name
  iam_instance_profile = aws_iam_instance_profile.ec2connectprofile.name
  security_groups      = ["${local.name}-k8s-master-sec-gr"]
  user_data            = data.template_file.worker.rendered
  tags = {
    Name = "${local.name}-kube-worker"
  }
  depends_on = [aws_instance.master]
}


data "template_file" "worker" {
  template = file("worker.sh")
  vars = {
    region = data.aws_region.current.name
    master-id = aws_instance.master.id
    master-private = aws_instance.master.private_ip
  }

}

data "template_file" "master" {
  template = file("master.sh")
}




