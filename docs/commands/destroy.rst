Destroy
==================

`terraform destroy <https://www.terraform.io/cli/commands/destroy>`_ is used to destroy/delete resources that have been deployed. The 'destroy' command will use the terraform.state file to remove objects in the opposite order of their deployment. The intent is to remove resources that have dependencies on other objects before attempting to remove those other objects. This process does work quite well, thoough it is not uncommon for an object in a public cloud to be 'marked for deletion' without having actually been deleted when Terraform attempts to delete the object it is dependent on. In these cases the 'destroy' operation will fail and you will need to run 'terraform destroy' again.

The scenario above occurs frequently enough that when dealing with certain public clouds I start out by running 'terraform destroy --auto-approve' three times, separated by semicolons so that the second and third calls will be occur immediately. Calling 'terraform destroy' when nothing is deployed doesn't cause problems because the 'destroy' command updates the 'terraform.state' file as each resource is destroyed, so subsequent calls only act on resources that are still deployed.
::

      terraform destroy --auto-approve; terraform destroy --auto-approve; terraform destroy --auto-approve

With a Bash alias (see :ref:`tips-and-tricks`) that command can be reduced to:
::

    tfda; tfda; tfda

.. note::
   The 'terraform apply' and 'terraform destroy' commands both require interactive approval before actually making any changes. To bypass the interactive approval use the '--auto-approve' command-line argument as shown here:

::

    terraform apply --auto-approve
    terraform destroy --auto-approve


