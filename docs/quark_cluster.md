# Quark Cluster: running larger/multiple jobs


For simple code development and reading/plotting data, you can use the desktop PCs and/or your laptop. 
However, if you need or produce larger data files, or need more computing power, you can use the *quark cluster*.

!!! important
    To get access to the quark cluster, please ask your supervisor. They will ask one of the system administrators to
    add your account to the list of people who have access.

## What is a computing cluster/batch farm?


A computing cluster is a number of computers that can be used to perform calculations. The quark cluster consists of a
*head node* to which you log in and where you can run code interactively and 7 *batch nodes* on which you can run
programs. Each batch node has 6 cores, so a total of 42 jobs can run in parallel.
The idea of a batch farm is that you develop code on the head node and then *submit jobs* to a *batch queue* to
run multiple jobs in parallel, for example to generate independent sets of events or to run over data files that
each contain a subset of events.

## Specifics of the setup of quark


You can reach the quark cluster by logging into its head node:

```bash
    ssh -Y quark.science.uu.nl
```

from any computer at the university network.

!!! note
    The ``-Y`` option specifies that a graphical ('X11') connection also needs to be opened.
    You can also set this option in the ssh options file. Nikhef has a
    [guide](https://www.nikhef.nl/grid/computing-course/work/ssh.html) to help you configuring ssh connections.
    If you are curious, you can get more information on the 
    [ssh X11 forwarding](https://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch09_03.htm).

To access the cluster from outside the university, you need to first ssh
to the gateway machine ``gemini.science.uu.nl`` (or use VPN). Use your solis-id as username (no capital letter at the
start) and your solis password to log in. Your account has to be activated for access to quark; if this is not the
case, ask your project supervisor.

There is a [graphical interface](http://quark.science.uu.nl>) (only accessible from university computers) to see the
main parameters of the cluster and find a user manual.

Some more technical information:

  * Home directories are not mounted from the university network. You can copy files to and from the cluster with ``scp``.
  * There are two files systems:
    * ``/data1``: (20 Tb) Contains all home directories and software (ROOT, AliRoot).
    * ``/data2``: (100 Tb) To keep larger (shared) data sets, like AODs (ALICE event data files) and simulation output.
  * The batch system on the farm is SGE (more details below)
    * ``qsub -V -cwd <exec>`` to submit a job; ``<exec>`` is the name of the executable, usually a shell script
      that invokes your program with suitable arguments.
    * ``qstat`` to see your jobs in the queue.
    * ``qdel`` to delete a job from the queue.

!!! note
    Not sure what a bash script is? You can check 
    [some examples](<https://www.ubuntupit.com/simple-yet-effective-linux-shell-script-examples/)
    or search for some tutorials.
    
  * Software is installed locally in ``/data1/software/``

    To set up some basic environment, add the following to your .bashrc file:
        
```bash
 module load python/2.7
 export PATH=/cm/local/apps/environment-modules/3.2.10/Modules/3.2.10/bin/:$PATH
 export ALIBUILD_WORK_DIR=/data1/software/alisoft
```
   
   To load the environment before starting aliroot (you can also define an alias in your ``.bashrc`` file), use:
```bash
    alienv enter --shellrc AliPhysics/latest-master-root6
```
   
