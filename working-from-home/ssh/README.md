# SSH \(lxplus or nikhef\)

## Setup ssh

We can access a computer with most of the software we need using ssh. For that, the only thing you will need a computer with a ssh client and preferably a X windows system \(X11\). 

What does that means?  
[**ssh**](https://en.wikipedia.org/wiki/Secure_Shell) is a tool that allows you to interact with a remote computer by command line.  
[**X windows system**](https://en.wikipedia.org/wiki/X_Window_System) \(or X11\) is a software to manage windows on \(most\) Linux systems.

Depending on your system, you might need to install some additional software to make it possible to interact with other computers over SSH.

### Linux \(Ubuntu, Fedora, etc\)

You already have everything working. You can move to the next section.

### Mac

You are halfway there. Mac has a native SSH client, but no X. We need to install a program that will allow you to interact with the windows remotely. Install [XQuartz](https://www.xquartz.org/), the X11 app for MacOS .

### Windows

It is easy if you are running **Windows 10**, but the instructions for Putty should also work on previous versions. Please check the instructions in the link bellow.

[Easy: use Putty](installing-putty.md)  
[Advanced: Setup a Linux subsystem on Windows 10](setup-ubuntu-usage-on-windows-10.md)

