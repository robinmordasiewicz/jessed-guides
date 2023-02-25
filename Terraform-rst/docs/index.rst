Beginners Guide to Terraform
============================

.. topic:: Beginners Guide to Terraform

   This guide is a simple introduction to `Terraform <https://www.terraform.io/intro>`_, and we will be going over several of the basic elements of a basic Terraform deployment.

.. toctree::

   quickstart.rst
   providers.rst
   registry.rst
   configurations.rst
   resources.rst
   modules.rst
   runs.rst
   variables.rst
   commands/index.rst
   tips_and_tricks.rst
   examples/index.rst

Motivation
----------

The most frustrating aspect of Terraform is the "Day One" learning curve. When first starting out most of the examples I found (by which I mean: every single one), seemed to assume that you understand the basic operation of Terraform and focused on the more complex use-cases. The problem with that is that I held certain misconceptions that none of those guides actually addressed. The most significant one was "How do I download the package (provider) to interact with a specific service?". The answer is "You don't", but all of the guides I found seemed to assume that knowledge and didn't address the topic. In hindsight I understand why, but it's been over two years and I still remember the intense frustration of that first day working with Terraform (TF).

This guide is intended to answer those very basic beginner questions, as well as walk you through the creation of your first (extremely) simple Terraform Run so you can see how the various pieces for together.

Organization
------------

This guide is broken into several small parts intended to let you skip the frustration of discovering them yourself. It definitely does not replace the `Terraform Documentation <https://www.terraform.io/intro>`_, but as you'll discover if you click the link, this guide will reduce the time you need to "internalize" how to use Terraform.


