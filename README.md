<img src="https://raw.githubusercontent.com/facerecog/version-merger/gh-pages/images/version-merger-logo.png" align="left" height="130" width="170" />

&nbsp;

#  **Overview**

Version Merger is a Python script which can be used to automatically save snapshots of a file as it changes. 


### Features
	
- Track files
- Save changes in files by overwriting previous versions
- Consolidate all changed files into a single master file 
- Specify when to merge changes into the master file
- Works with any Linux operating system
- 3-step configuration wizard that requires less than 1 minute to set-up

### System Requirements

- Python 2.7
- These instructions have been tested on Ubuntu 14.04.3 and 15.10.


-----------------------

#  **Animated Tutorial**


&nbsp;  



-----------------------

# **Getting started** 




### Download
Clone the latest repository version from Github (recommended):
`$ git clone https://github.com/facerecog/version-merger.git`

Alternatively, download the .tar.gz file from the top of this page and unpack it:
`$ wget https://github.com/facerecog/version-merger/tarball/master -O - | tar -xz`

Now `cd` into the newly extracted directory.



-------------------------


# **How the script works** 

`version-merger.py` takes in the following parameters:
- i (input file(s))
- o (output file)
- r (time interval between each snapshot)
- t (time interval between each merge)

Every _r_ seconds, `version-merger.py` uses `git stash` to save any changes in the input file _i_. Every _t_ seconds, `version-merger.py` will merge all stashed content into output file _o_.


-------------------------

# **Verify that it works** 


Run the following script that writes a random value in `dump.csv` every second:
`python example/randomizing_csv.py`

Open a *new terminal* and run version-merger.py as such:
`python version-merger.py -i dump.csv -o mastercopy.csv -t 60 -r 1`

If you have many files to track, you may use filename globbing as such:
`python version-merger.py -i dump*.csv -o mastercopy.csv -t 60 -r 1`



-------------------------

# **Version-Merger Diagram**  

<img src="https://raw.githubusercontent.com/facerecog/version-merger/gh-pages/images/version-merger-explanation.png"/>

&nbsp;  

-------------------------

# **Uninstall**  

To uninstall:




-------------------------

# **Support**  

If you want to support this project, please consider reaching out to me via  muhd.amrullah@facerecog.asia  


-------------------------  
Property of Facerecog Asia Pte. Ltd. and 26 Factorial