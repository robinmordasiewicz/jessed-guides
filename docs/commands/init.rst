init
====

When you run 'terraform init' Terraform will read all of the configuration files in your current directory and download all of the required *providers* for you. These will be placed in a directory called '.terraform/providers/...'. It will also identify every `module <https://www.terraform.io/docs/glossary#module>`_ used in your configuration and write the list to '.terraform/modules/modules.json'.

When you run 'terraform init' Terraform reads every file that ends with '.tf' in the current directory and looks for a block called  'terraform', which contains a sub-block called 'required_providers'. The 'required_providers' block contains a list of every 3rd party "provider" required by your terraform configuration. It does not need to include default terraform providers - only 3rd party providers that provide additional functionality.

.. important::
   The first thing to understand here is that, other than the Terraform package itself, **nothing is manually downloaded**. Terraform will automatically download the components it requires when it is *initialized*. (I spent a humiliating amount of time figuring this out.) The second thing to understand is that Terraform initialization *is not the first step* in creating a new plan/deployment. Counter-intuitively, terraform initialization takes place after you've written all of the code and right before you actually try to run the plan to do something.

.. note::
   Running `terraform init` does not verify that your code is without flaws or actually does anything at all. It *does* perform a basic syntax check, but that's it.

