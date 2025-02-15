Providers
=========

A `Terraform Provider <https://www.terraform.io/docs/glossary#terraform-provider>`_ is a plugin which will communicate with a service API for resource configuration. For example, in order to configure Azure resources Terraform uses the `azurerm <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs>`_ provider. Providers are *usually* written by the organization that provides the product being configured, though that is not always the case. For example, the `BIG-IP <https://registry.terraform.io/providers/F5Networks/bigip/1.15.2>`_ is provided by F5, but the Azure provider is provided directly by Hashicorp (the same company that created Terraform). Terraform providers are downloaded and installed during the terraform init stage of the workflow.

There are two sections of a provider. The first section declares that a provider is required, and the second section is the provider configuration.

#. Declaration

   The 'terraform' block is not limited on only one Provider; more can be defined depending on what your Terraform Run requires. Here are a few example Provider configurations:

   ::

       terraform {
         required_providers {
           azurerm = { version = "3.14.0" }
         }
       }

#. Configuration


`Azure <https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs>`_
--------------------------------------------------------------------------------

.. note::
   Along with identifying and downloading the Provider, ``terraform init`` will also *upgrade* the provider if a newer one is available and the specific version isn't specified in the provider declaration. The example above defines the specific version of the provider to be used, and newer versions will be ignored. A version statement **'version ~> "3.14.0"**, may be used to specify an upgrade whenever a new version is available. If the newer version includes changes to the options/arguments in any of the resources, a refactor of the configuration may be required to suit the newer version, so it is best practice to restrict the provider to a specific version to control the upgrade.

The *Provider* configuration blocks define changes to the default provider behavior. Even without any changes each provider must still have a configuration block. Here is a default configuration block for the Azure Provider:
::

    provider "azurerm" { }

Provider configuration blocks can be much more complicated. Here is a configuration block for the Azure subscriber that includes a few modifications to the default behavior:
::

    provider "azurerm" {
      features {
        virtual_machine {
          # Necessary for license revocation when using BIG-IQ LM.
          graceful_shutdown                       = true
          delete_os_disk_on_deletion              = true
        }
        template_deployment {
          #  Allow the RG to be removed even if resources are still present
          delete_nested_items_during_deletion     = true
        }
        resource_group {
          # Allow the RG to be removed even if resources are still present
          prevent_deletion_if_contains_resources  = false
        }
      }
    }


`AWS  <https://registry.terraform.io/providers/hashicorp/aws/3.27.0/docs>`_
---------------------------------------------------------------------------

The Terraform AWS Provider configuration block shown here pulls the credentials and profile from local values (variables), and defines the default region for operations.
::

    terraform {
      required_providers {
        aws = {
          source = "hashicorp/aws"
          version = "~> 3.0"
        }
      }
    }

    provider "aws" {
      shared_credentials_file   = local.creds_file
      profile                   = local.profile
      region                    = var.region
    }

Notice that even the terraform configuration block differs from the Azure example. In this case the source of the provider is defined in addition to what version of the provider should be used.


`GCP <https://registry.terraform.io/providers/hashicorp/google/latest/docs>`_
-----------------------------------------------------------------------------

And finally, the GCP Provider.
::

    terraform {
      required_providers {
        google = {
          version = "4.40.0"
        }
      }
    }

    provider "google" {
      project                   = var.project
      region                    = var.region
      zone                      = var.zone
    }


