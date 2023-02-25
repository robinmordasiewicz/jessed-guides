Terraform State
===============
Terraform keeps track of the state of configured resources using a file called `terraform.state <https://developer.hashicorp.com/terraform/language/state>`_, which is a JSON-formatted text file containing all of the attributes of every resource deployed by a Terraform Run. The 'terraform.state' file *can* be examined by using a tool like `jq <https://stedolan.github.io/jq/>`_; however, Terraform provides a set of commands for viewing the resources in the terraform.state file to view the current state of the Run.

You can list the resources in the terraform.state file with:
::

    terraform state list

Here is the output of 'terraform state list' for what is deployed by deploying :ref:`example4`.
::

    $ tf state list
    module.rg[0].azurerm_resource_group.rg
    module.rg[1].azurerm_resource_group.rg
    module.rg[2].azurerm_resource_group.rg

You can also view details of each object by using 'terraform state show *object_name*, as shown here:
::

    $ tf state show module.rg`0 .azurerm_resource_group.rg
    # module.rg`0 .azurerm_resource_group.rg:
    resource "azurerm_resource_group" "rg" {
        id       = "/subscriptions/0f92c295-b01d-47ab-a709-1868040254df/resourceGroups/my_lab-1-rg"
        location = "westus2"
        name     = "my_lab-1-rg"
    }

Examining the state of an object in Terraform is particularly useful when you need to use an attribute of an object that isn't well defined in the resource documentation. This doesn't come up often, but when it does being able to examine the object to see what attributes you can access is extremely helpful. Any resource attribute you can see in the terraform.state file is usable within Terraform code.

