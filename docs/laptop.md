# Installing the ALICE software in your computer

## Install in your current operation system


First of all, ROOT, AliRoot/AliPhysics, and most of the software packages used for data analysis of particle
physics **only** work on the following operating systems:

* Linux (Ubuntu and derivatives or CentOS/Scientific Linux)
* Mac OS

If you are in one of these systems, the required software can then be installed with the Linux package manager,
by compilation, or download, following the 
[AliPhysics installation instructions](https://alice-doc.github.io/alice-analysis-tutorial/building/). 
If you are not not in one of these systems, you can install Ubuntu or use one of the other 
[installation options](laptop_intro.md) or consider to use the [quark cluster](quark_cluster.md). 

Make sure your laptop has **all** prerequisites before installation.


## Install Ubuntu in your computer

If you have a windows laptop and have enough room on your hard disk (50-100 Gb), it is very easy to install a
Linux distribution (Ubuntu) and use the laptop with dual boot. This way you will be asked to either start up Windows
or Ubuntu when you turn on the laptop.

To download Ubuntu, the only thing you have to do is create a USB stick with the
installation image. You can download the latest Long Term Service (LTS) version of Ubuntu from the
[download page](https://ubuntu.com/download/desktop) (make sure to get the LTS version and not one of the
regular releases). Installation instructions starting
from Windows are in the [Ubuntu website](https://ubuntu.com/tutorials/tutorial-create-a-usb-stick-on-windows#1-overview).

Now you can follow the instructions on the previous section.

## Install in a container

Containers are a recent technology that allows you to run isolated applications. This is super convenient if you
need to install different versions of the same software. Curious? You can check
[what containers are](https://www.docker.com/resources/what-container).
In our case, this can be achieved using [alidock](https://github.com/alidock/alidock/wiki),
which runs the ALICE software inside a container.

!!! warning
    Unfortunately, alidock is not officially supported by ALICE. It works well in most cases, but if you have some
    problems, get in touch with someone from our institute for help.
    
