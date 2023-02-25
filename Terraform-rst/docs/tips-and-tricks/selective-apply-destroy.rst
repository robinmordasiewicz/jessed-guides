Selective apply / destroy
-------------------------

You can restrict Terraform to deploying or destroying specific objects by using the '--target=<resource_name>' command-line argument. This can be particularly useful if you have a large Run and are trying to debug or test one of the final resources being deployed. (i.e. trying to debug the cloud-init being used with BIG-IP). In those cases all of the time necessary to destroy, then re-deploy, all of the resources that the BIG-IP depends on is effectively wasted time - all you *need* to destroy and re-deploy is the BIG-IP itself. This is not an uncommon scenario, and the answer is the '--target=<name>' argument.

To use --target=name you enter the terraform destroy or plan command like you normally would, but you add the '--target=' argument afterwards. For example, let's say my BIG-IP is deployed in a module called 'bigip'. I can destroy all of the objects related to that object alone by using the following command:
::

    terraform destroy --auto-approve --target=module.bigip

That command will destroy the resources created in my 'bigip' module and nothing else. 

.. note::
   If the resource you are trying to destroy in this way is a dependency of a later resource, the command will fail. 

To re-deploy I have two options:
#. Use the '--target=' argument again when running the 'terraform apply' command
#. Run 'terraform apply [--auto-approve]' without the '--target=' argument and jsut let Terraform deploy everything that isn't already deployed (as per the terraform.state file).

.. note::
   According to Terraform the '--target=<name>' argument should only be used for debugging/testing.

