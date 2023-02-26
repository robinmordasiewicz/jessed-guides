Registry
========

Terraform Providers are retrieved from a Registry. The official Hashicorp Terraform registry is `registry.terraform.io <https://registry.terraform.io/>`_, which is used to download Providers for which a more specific source location is not provided. All of the examples shown on the :ref:`providers` page will use this default registry when downloading the specified providers.

Documentation
-------------

In addition to making the providers available for download by Terraform, the registry is also where the official documentation for each provider is located. For example, the documentation for the Azure provider is located at https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs. The link above is for the latest version of the Provider but the documentation for earlier versions can be viewed with the dropdown at the top of the page.

.. note::
   When creating or modifying a Terraform plan the documentation in the Registry is best documentation resource without question. It is very rare that I have to look elsewhere for help with getting a Resource to work.

Example Configurations
----------------------

All, or nearly all, resources supported by a provider are documented on the provider documentation page. Further, nearly all of the examples show you not just the usage of the specific resource but also include examples of any pre-requisite resources necessary to make use of the resource. For instance, the documentation at `azurerm_linux_virtual_machine <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_virtual_machine>`_ also includes examples for every resource necessary to use it. 

* `azurerm_resource_group <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group>`_
* `azurerm_virtual_network <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network>`_
* `azurerm_subnet <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet>`_
* `azurerm_network_interface <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/network_interface>`_

All of which are pre-requisites to creating a azurerm_linux_virtual_machine resource.

All of the resource configuration options (input) and attributes are shown below the examples.

.. note::
   When having a problem working with a resource it is frequently helpful to take a look at pages that require that resource. The configuration of other resources that require the one you are working with will include their own examples, and sometimes those examples enhance the examples in the documentation page. This situation isn't common, but I have encountered it enough times that this is one of the first things I do when I have a resource that repeatedly fails to deploy with some cryptic error message.

