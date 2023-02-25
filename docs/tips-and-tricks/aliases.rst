Bash Aliases
============

Bash aliases are a way to create Bash commands that call actual programs. Bash aliases are defined as so:
::

    alias alias_name="command_to_run <arguments>"

Aliases are usually placed in a file that will be sourced by Bash during initialization, such as the ~/.bashrc, ~/.profile, or ~/.bash_aliases. Here is the full contents of my ~/.terraform_aliases.bash file, which is source from ~/.bashrc during Bash initialization:
::

    alias tf='terraform'
    alias tfaa='terraform apply -auto-approve'
    alias tfda='terraform destroy -auto-approve'
    alias tfi='terraform init'
    alias tfp='terraform plan'

This command in my ~/.bashrc sources the ~/.terraform_aliases.bash file, ensuring that these aliases are present every time I open a terminal.
::

    source ~/.terraform_aliases.bash

.. note::
   The aliases could just as easily be located directly in the ~/.bashrc rather than being sourced. I source the file rather than having them in ~/.bashrc because I have (literally) hundreds of aliases, and breaking them into separate files helps keep them organized.

To use an alias you just type the alias name as if it were a command. To use the 'tfaa' alias I would enter the following on the command line:
::

    tfaa

...which would be the same as typing:
::

    terraform apply --auto-approve
