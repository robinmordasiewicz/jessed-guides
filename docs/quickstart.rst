Quick Start
===========

#. Create a new working folder for a Terraform project and change directory into the new folder.

   .. bash:: mkdir terraform
      :do-not-run:

   .. bash:: cd terraform
      :display-command:
      :do-not-run:

#. Create a file named hello-world.tf

   .. bash:: cat hello-world.tf

#. Initialize your TF environment, which includes a basic syntax check.

   .. bash:: terraform init

#. Syntax, dependency, logic check.

   .. bash:: terraform plan

#. Deploy the configuration

   .. bash:: terraform apply --auto-approve

#. Delete deployed objects, reverses the order of operations.

   .. bash:: terraform destroy --auto-approve

