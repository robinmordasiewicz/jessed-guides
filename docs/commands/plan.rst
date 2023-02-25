Plan
====

`terraform plan <https://www.terraform.io/cli/commands/plan>`_ is used to perform an exhaustive check of your code, very similar to a 'dry-run' option. It will check the syntax, variable assignments, and attempt to identify circular references. <Circular references occur when one resource depends on another, but that other object depends on the first one. Sometimes the dependency chain can include three or four objects, making identification of the circular reference difficult.>`_

Performing a `terraform plan` is always recommended prior to actually applying the configuration, and will most likely become an internalized part of your deployment process.


