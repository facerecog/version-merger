<img src="https://raw.githubusercontent.com/facerecog/version-merger/gh-pages/images/version-merger-logo.png" align="left" height="130" width="170" />

&nbsp;

#  **Overview**

Version Merger is a Python script which can be used to automatically save snapshots of a file as it changes. 

### Features
	
- Track files across regular time intervals (specified by user)
- Save new versions of file efficiently 
- Merge files across regular time intervals (specified by user)
- Works with any Linux operating system
- 3-step configuration wizard that requires less than 1 minute to set-up

### System Requirements

- Python 2.7
- These instructions have been tested on Ubuntu 14.04.3 and 15.10.

-----------------------

# **Version-Merger Diagram**  

<img src="https://raw.githubusercontent.com/facerecog/version-merger/gh-pages/images/version-merger-explanation.png"/>

-----------------------

#  **Animated Tutorial**

<div style="float:left; width:100%">
    <img src="https://raw.githubusercontent.com/facerecog/version-merger/gh-pages/images/version-merger-tutorial.gif" align="left" width=640 height=360px  />


&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  
&nbsp;  


-----------------------

# **Getting started** 




### Download
Clone the latest repository version from Github (recommended):
`$ git clone https://github.com/facerecog/version-merger.git`

Alternatively, download the .tar.gz file from the top of this page and unpack it:
`$ wget https://github.com/facerecog/version-merger/tarball/master -O - | tar -xz`

Now `cd` into the newly extracted directory.

Alternatively, install using `pip`:  `sudo pip install version-merger`

-------------------------


# **How the script works** 

`version-merger.py` takes in the following parameters:
- -i: input file(s) you want to keep track of
- -o: output file
- -r: time interval (in seconds) between each snapshot
- -t: time interval (in seconds) between each merge

Every _r_ seconds, `version-merger.py` uses `git stash` to save any changes in the input file _i_. Every _t_ seconds, `version-merger.py` will merge all stashed content into output file _o_.


-------------------------

# **Verify that it works** 


Run the following script that writes a random value in `dump.csv` every second:  
`python example/randomizing_csv.py`

Open a *new terminal* and run version-merger.py as such:
`python version-merger.py -i dump.csv -o mastercopy.csv -t 60 -r 1`

If you have many files to track, you may use filename globbing as such:  
`python version-merger.py -i dump*.csv -o mastercopy.csv -t 60 -r 1`

# **Code Example** 
Code Example

For the sake of brevity, this example merges its stashed versions of `dump.csv` every 3 seconds:
```
$ python version-merger.py -i dump.csv -o mastercopy.csv -t 3 -r 1
Reinitialized existing Git repository in /home/di/Desktop/FaceRecog/t/version-merger/.git/
[master b1d1ef5] First Commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 clone.csv
Saved working directory and index state WIP on master: b1d1ef5 First Commit
HEAD is now at b1d1ef5 First Commit
Submitted
dump.csv
Saved working directory and index state WIP on master: b1d1ef5 First Commit
HEAD is now at b1d1ef5 First Commit
Submitted
dump.csv
Saved working directory and index state WIP on master: b1d1ef5 First Commit
HEAD is now at b1d1ef5 First Commit
Submitted
dump.csv
HEAD is now at b1d1ef5 First Commit
Done
cat: tempclone.csvtemp.csv: No such file or directory
HEAD is now at b1d1ef5 First Commit
Done
HEAD is now at b1d1ef5 First Commit
Done
Saved working directory and index state WIP on master: b1d1ef5 First Commit
HEAD is now at b1d1ef5 First Commit
Submitted
dump.csv
```
... and so on.

-------------------------

# **Uninstall**  

If you installed version-merger using pip, run the following to uninstall it:
`sudo pip uninstall version-merger`

Otherwise, simply delete the version-merger folder.


-------------------------

# **Support**  

If you want to support this project, please consider reaching out to me via  muhd.amrullah@facerecog.asia  


-------------------------  
Property of Facerecog Asia Pte. Ltd. and 26 Factorial