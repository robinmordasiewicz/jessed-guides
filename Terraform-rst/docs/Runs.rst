Run
===

A Terraform `run <https://www.terraform.io/docs/glossary#run>`_ consists of one or more `resources <https://www.terraform.io/docs/glossary#resource>`_. Resources are what will be renderedwhen you enter `terraform apply` to deploy your configuration.

Terraform `resources <https://www.terraform.io/docs/glossary#resource>`_ are blocks of Infrastructure-as-Code (IaC) elements, which define how the deployment *should* be and leave it up to the Terraform logic and the provider to make it happen. While several aspects of Terraform seem quite similar to a programming language, what you are actually "coding" is how things should be. When you run `terraform apply`, you are telling Terraform to make them that way.


