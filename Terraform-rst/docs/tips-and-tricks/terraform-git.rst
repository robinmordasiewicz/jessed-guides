Using Terraform with Git
========================

It is extremely common to use Git to provide source control for Terraform configurations. Entire DevOps ecosystems have been created around this relationship, and I would be remiss to not include a section on some best-practices related to the **.gitignore** file.

As you almost certainly know, the ``.gitignore`` file is used to exclude files from being included by git, and there are some files you really don't want included in your git repository. I've provided a list of these files below and urge you to use the ``.gitignore`` file to exclude them.

* .terraform/
   * Directory containing the dowloaded Providers and files pertaining to the modules defined in your Terraform configuration.
   * Add the following to .gitignore: ``.terraform*``
* .terraform.lock.hcl
   * File containing a list of the downloaded Providers and the hashes associated with each
   * Add the following to .gitignore: *.terraform\**
      * *.terraform\** excludes both the *.terraform.lock.hcl* file and the *.terraform/* directory
* .terraform.tfstate & .terraform.tfstate.backup
   * File containing the current state of any resources deployed by Terraform (see above)
   * Add the following to .gitignore: ``terraform.tfstate*``
      * Excludes both the *terraform.tfstate* and the *terraform.tfstate.backup* files.

More complex Terraform configurations might include an output directory for post-procesing template files, as well as a directory within which those template files might be stored. I names those directories *work_tmp* and *templates*, respectively. The *templates* directory should be included in a Git repository; however, the directory containing the post-processing versions of those templates should not, so I add that directory to my .gitignore.

The complete list of .gitignore additions would be:
::

    .terraform*
    .terraform.tfstate*
    work_tmp/

