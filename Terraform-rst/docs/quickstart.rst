Quick Start
===========

.. topic:: tldr
   
   Just get straight to the point

   Write your Terraform code

   * I describe this below; however, if you are actually starting with this know that I have experienced your pain and have no sympathy. Helping you avoid that pain is the whole purpose of this guide.

#. ``terraform init``

   * Initialize your TF environment, which includes a basic syntax check.

     .. note::
        This will download the required providers and enumerate your modules.

#. ``terraform plan``

   * More thorough syntax check
   * Determine order of operations based on dependencies
   * Logic check - checks for unmet dependencies, circular logic, missing variables, etc...

#. ``terraform apply [--auto-approve]``

   * Deploy the configuration.
   * Communication/authentication/authorization issues will be caught at this stage.
   * Failures will *not* be rolled back automatically.

#. ``terraform destroy [--auto-approve]``

   * Destroy/delete deployed objects
   * Reverses the order of operations determined at the time of deployment


