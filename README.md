# AnsibleTestingLab
This repository will act as a testing ground for my bachelor thesis where I will be looking for a workflow that improves the Ansible role testing experience. The goal is to set up a Travis CI system that can automatically build a Docker or Podman container with the necessary dependencies, instead of having to manually configure a Dockerfile with a standard shell script.

As of February 21st, the following technology stack is being used or is taken into consideration:

* Ansible
* Molecule
* Travis CI
* Docker
* Podman
* Vagrant with VirtualBox

Additionally, this thesis will also research the feasibility to replace Docker with an alternative like Red Hat's Podman. While both drivers are relatively "easy" to install (I had some installation issues with both drivers on Pop!OS), podman requires additional configuration in order to use it on a non-root account, which is in fact Podman's trademark. 
