Variables
=========

`Variables <https://www.terraform.io/language/values/variables>`_ are just that. They are provided to the various `configurations <https://www.terraform.io/docs/glossary#terraform-configuration>`_ in lieu of static values to allow for simpler description of what should be deployed. That said, variables in Terraform are a source of frequent confusion and much gnashing of teeth.

There are two basic types of varibales: `input variables <https://www.terraform.io/language/values/variables>`_ and `local values <https://www.terraform.io/language/values/locals>`_.

Input Variables
---------------

`Input variables <https://www.terraform.io/language/values/variables>`_ are provided via configuration files, on the CLI, or pulled from environment variables. These are immutable (i.e. cannot be changed once defined), and they are defined when Terraform is executed. Dynamic values cannot be used, nor can one input variable receive its value from another input variable. These are static, immutable, and defined at run-time.

Local Values
------------

`Local values <https://www.terraform.io/language/values/locals>`_ are also immutable, however these can receive dynamically generated values rather than static values. Unlike Input variables, local values can use other variables as part of the value.

Variable Usage
--------------

Here is a simple example illustrating the defintion of both:
::

    variable "prefix" { default = "my_prefix" }
    locals { vnet_name = "${var.prefix}-vnet" }

The variable "prefix" would contain the value *my_prefix*, and the local value "vnet_name" would contain the value *my_prefix-vnet*. However, you would *not* be able to define input variable that leverage the existing value of the *prefix* variable.

.. tip:::
   All Input variable names are referenced using the 'var.' prefix, and all local values are referenced using the 'local.' prefix.

Defining Variables
------------------

There may be numerous variables in a moderately complex Terraform configuration. Variables may be seaprated to different files to isolate one group of objects, making it easier to manage changes.

By default Terraform will source certain files for variable definitions:

* vars.tf
* variables.tf
* terraform.tfvars
* terraform.tfvars.json

Additional files can be specified on the CLI using the \*-var-file* option as shown here:
::

    terraform apply -var-file="my_variables.tfvars"

That syntax applies to files with the following extensions:
* .tfvars
* .tfvars.json

To simplify the import of additional variable files, insert ".auto" between the filename and the ".tfvars" or ".tfvars.json" extension, which removes the need to specify the filenames using the '-var-file' CLI option.

.. important::
   Variable names may be defined in \*.tfvars or \*.auto.tfvars files. For example, a variable named "bigip" in a file "v_bigip.auto.tfvars", an empty "placeholder" variable defining that name must be located in one of the files that is imported automatically. Here is an example of how I would import a variable file called "v_bigip.auto.tfvars" containing a variable called "bigip":

**vars.tf**
::

    variable "bigip"   {}

**v_bigip.auto.tfvars**
::

    bigip = {
      name   = "my_ltm_01"
    }

Terraform will recognize a variable named "bigip" containing a nested variable named "use_paygo" with a string value of "my_ltm_01". If the placeholder variable is not present the variable(s)`_ within the v_bigip.auto.tfvars file would not be included. A runtime error will be thrown when Terraform attempts to import the variables define in the "v_bigip.auto.tfvars" file.

