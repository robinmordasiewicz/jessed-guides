Apply
=====

`terraform apply <https://www.terraform.io/cli/commands/apply>`_ is used to actually apply your configuration. It goes through the same process as `terraform plan <https://www.terraform.io/cli/commands/plan>`_, but this time the changes are actually implemented. As the 'apply' is executed Terraform will be writing completed actions to the 'terraform.state' file. The 'terraform.state' file contains `state <https://www.terraform.io/language/state>`_ information about the current, successfully-deployed configuration. Only resources that are *successfully* deployed are written to the state file. This file is then used for if Terraform is called again to compare the current deployment with a changed configuration to determine what it actually has to do.

For example, if you deployed a BIG-IP and a server in a previous 'terraform apply', then change something about the server configuration, Terraform will use the 'terraform.state' file to determine what it actually needs to do to make the deployed configuration match your IaC configuration. If the change to the servers configuration in Terraform doesn't impact the BIG-IP, then the server would be redeployed with the new configuration while the BIG-IP wouldn't be modified.

