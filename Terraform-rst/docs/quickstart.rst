Quick Start
===========

#. Create a file named hello-world.tf

   .. literalinclude:: ../terraform/hello-world.tf
      :language: terraform

#. Initialize your TF environment, which includes a basic syntax check.

   .. code-block:: bash

      $ terraform init

#. Syntax, dependency, logic check.

   .. code-block:: bash

      $ terraform plan

#. Deploy the configuration

   .. code-block:: bash

      $ terraform apply --auto-approve

#. Delete deployed objects, reverses the order of operations.

   .. code-block:: bash

      $ terraform destroy --auto-approve

