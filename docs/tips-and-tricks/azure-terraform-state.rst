Azure Terraform State Trick
~~~~~~~~~~~~~~~~~~~~~~~~~~~

My favorite aspect of the 'terraform.state' file is that it is the **sole** source of truth for Terraform. This means that if you want to completely reset Terraform's "view" of the current run all you need to do is delete or rename this file. Why is this great? Well, sometimes destroying a complex environment deployed by Terraform can take a really long time. I've been stuck waiting for an Azure lab to be destroyed for 15+ minutes in the past. (This is actually an Azure responsiveness issue rather than an Terraform issue, but knowing that doesn't make the time go by any faster.)

If you organize your lab naming scheme around a single *prefix* value that is incorporated into the name of all objects created by that run, what you can do to save time is just go to the Azure Portal and delete the resource-group(s) created by your Terraform Run. Then delete the 'terraform.state' file itself. Finally, change the *prefix* you are using with all of your object names. At this point all of the following will be true:

#. Azure will be deleting the Resource-Group and all of the objects it contains. It won't matter if this takes two minutes or an hour because...
#. Terraform will believe nothing is deployed because there is no state file. You can immediately begin testing your most recent changes to the Terraform configuration because...
#. With the new prefix none of the object names Terraform attempts to deploy will collide with existing objects.

  * Technically the concern regarding name collisions only applies to the resource-group name itself; however, there are a couple other objects that also require globally (or at least, organizationally) unique names, such as Log Analytics Workbooks and Storage Accounts.

Using this trick will spare you a lot of time if you start to create Terraform Runs with many levels of dependencies.

.. note::
   This trick is only really only useful when you are working in an environment that allows a simple, hands-off group deletion option, like deleting an Azure Resource-Group or Kubernetes namesspace. GCP, and especially AWS, have no simple administrative container that can be deleted at-will to destroy all of the grouped objects.

.. warning::
   The corallary to the note above is that you should avoid deleting your terraform state file in all other cases; especially when working with AWS or GCP. I once had a corrupted deployment to AWS that caused the 'terraform destroy' command to fail due to an AWS error, so I had to track down every oject I had deployed with Terraform and delete them all manually. This was an incredible PITA. Deleting your terraform.state file without first running the 'terraform destroy' command will result in the same thing: to clean up your deployed resources you'll end up having to track all of them down to manually delete them. You have been warned.

