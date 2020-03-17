# Advanced: Setup WLS on Windows 10

The best option is to install Ubuntu using the WLS \([Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10)\). It only works if you are using windows 10.

## Install Xming X

This will allow you to interact with the ROOT TBrowser and other Linux applications. Download it [here](https://sourceforge.net/projects/xming/files/latest/download) and run it. You can use the default settings in the installation, just click on _Next_ until the end.

## Install Windows Subsystem for Linux

Microsoft has proved [detailed instructions](https://docs.microsoft.com/en-us/windows/wsl/install-win10) on its website on how to do it. I will give a step-by-step description bellow too, but if you have additional problems, please check first the Microsoft website.

First **update your Windows** installation to the latest version. If you have automatic updates, you are probably fine. If you not sure how to update your system, check [here](https://support.microsoft.com/en-us/help/4027667/windows-10-update).

Now let's start.

### Turning the Windows Subsystem Linux On

Open PowerShell as Administrator. For that, use the search bar at the bottom left. Type _PowerShell_ and on the menu on the right side, click on _Run as Administrator._ Click on _Yes_ when prompted, giving the program Administrator rights. This will open a command line called **Windows Power Shell**. Run the following code in it. You can paste to the Windows Power Shell, and other terminal on Windows, by clicking with the right mouse button.

```text
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Once completed, the program will ask for you to restart your computer. Type _Y and_ let the computer restart.

## Install Ubuntu

Now, it is time to install a Linux \(sub\)system on your Windows computer. I recommend to install Ubuntu 18.04 LTS.

Click on the [link](https://www.microsoft.com/store/apps/9N9TNGVNDL3Q), then in _Get_ \(or _Download_, depending on your language\).

This will prompt you to open the Microsoft Store. Open it. In the new window, click again in the _Get/Download_ button. Wait until the file is downloaded and installed.

Now go to the search bar \(on the bottom left of you screen\) and type _Ubuntu_ and open it. This will open a new terminal which will install Ubuntu itself. It will take a few minutes.

During the installation, you will be prompted to choose a username and password. Please make you will remember the password. The password will be used when we are installing new software.

From this point on, all the commands in this guide will be **executed in this "Ubuntu" terminal**. This will behave just like the one you have used in other Ubuntu installations

Run the following command to update the list of packages. This will tell the system where to find each package.  When the command starts with sudo, they will be executed with administrator privileges. That means that you will have to type your password \(the one you created during the installation\).

```bash
sudo apt-get update
```

Now, run the following code to install the necessary software. It will take a while, wait for the execution to finish.

```bash
sudo apt install ssh xauth xorg
```

Now, let's configure the ssh client to your needs. Do it by running the code bellow.

```bash
echo "Host *
    ForwardAgent yes
    ForwardX11 yes
    ForwardX11Trusted yes

XauthLocation /usr/bin/xauth" >>  ~/.ssh/ssh_config
```

Now, we will tell Ubuntu where to find Xming X. Run the following command:

```bash
 echo 'export DISPLAY=localhost:0' >> ~/.bashrc
```

Close your Ubuntu terminal and open it again. It should have all the basics needed to use ssh or even start an installation of AliPhysics from aliBuild.

