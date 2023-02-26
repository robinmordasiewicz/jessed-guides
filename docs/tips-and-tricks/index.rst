.. _tips-and-tricks:

Tips and Tricks
===============

Terraform has a few execution quirks that can become bothersome with frequent usage. One example is that both 'terraform apply' and 'terraform destroy' require an interactive approval. Bypassing this is possible with the use of the '--auto-approve' argument, but that's a lot to be typing everytime you want to perform or clean-up a terraform run. (And, being exceptionally lazy, I don't want to be typing that much every time I run a terraform command.) So what follows are the Bash aliases I use with terraform, as well as a few other things I do to a) simplify terraform usage and b) diagnose problems with terraform runs.

.. toctree::
   :maxdepth: 1
   :numbered: 1
   :hidden:

   aliases.rst
   azure-terraform-state.rst
   selective-apply-destroy.rst
   terraform-git.rst
   terraform-state-file.rst
   terraform-state.rst
   plugin_cache.rst
