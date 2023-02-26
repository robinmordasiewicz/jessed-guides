Quick Start
===========

#. Create a new working folder for a Terraform project and change directory into the new folder.

   .. bash:: [ ! -d terraform ] && mkdir terraform
      :display-command: mkdir terraform

   .. bash:: cp ../terraform/hello-world.tf terraform/hello-world.tf
      :display-command: cd terraform

#. Create a file named hello-world.tf

   .. bash:: cat <<EOF > terraform/hello-world.tf
      :display-command: cat <<EOF > hello-world.tf

      terraform {
        required_version = ">= 0.12.26"
      }
      output "hello_world" {
        value = "Hello, World!"
      }
      EOF

#. Initialize your TF environment, which includes a basic syntax check.

   .. bash:: cd terraform && terraform init
      :display-command: terraform init

#. Syntax, dependency, logic check.

   .. bash:: cd terraform && terraform plan
      :display-command: terraform plan

#. Deploy the configuration

   .. bash:: cd terraform && terraform apply --auto-approve
      :display-command: terraform apply --auto-approve

#. Delete deployed objects, reverses the order of operations.

   .. bash:: cd terraform && terraform destroy --auto-approve
      :display-command: terraform destroy --auto-approve

