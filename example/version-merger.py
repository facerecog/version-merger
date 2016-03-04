import subprocess
import time
import shutil
import os
import glob

def stash(name_of_file):
    shutil.copy(name_of_file, './clone.csv')
    subprocess.call('git add clone.csv', shell=True)
    subprocess.call('git stash', shell=True)
    print 'Submitted'
    time.sleep(5)

def startGit():
    subprocess.call('git init', shell=True)
    subprocess.call('git config --global user.email "you@example.com"', shell=True)
    subprocess.call('git config --global user.name "Your Name"', shell=True)
    subprocess.call('git add clone.csv', shell=True)
    subprocess.call('git commit -m "First Commit"', shell=True)

#A substring is chosen for the script to stop the loop once it reaches the end of git stash list
def file(name_of_file):
    string_for_file_script = 'cat %s temp%stemp.csv > temp%soutput.csv' % (name_of_file, name_of_file, name_of_file)
    string_for_convert_script = 'cat temp%soutput.csv > temp%stemp.csv' % (name_of_file, name_of_file)
    subprocess.call(string_for_file_script, shell=True)
    subprocess.call(string_for_convert_script, shell=True)

# A function for Git to change the stash
def runGit(): 
    subprocess.call('git reset --hard', shell=True) 
    subprocess.call('git stash pop -q', shell=True)
    print 'Done'

# A function to start version control for n seconds
def versionControl(second_delay):
    t_end = time.time() + second_delay
    while time.time() < t_end:
        removeJunk()
        newest = max(glob.iglob("dump*.csv"), key=os.path.getctime)
        stash(newest)
        print newest

# A function to remove the excess files
def removeJunk():
    for fl in glob.glob("*kismet.csv"):
        os.remove(fl)
    for gl in glob.glob("*.cap"):
        os.remove(gl)
    for hl in glob.glob("*.netxml"):
        os.remove(hl)

def removeExcess():
    for jl in glob.glob("*temp.csv"):
	os.remove(jl)
    subprocess.call('cat *output.csv >> master.csv', shell=True)
    for kl in glob.glob("*output.csv"):
	os.remove(kl)

def unPop():
    while True:
    	substring = 'stash@{0}:'
    	outputfromList = subprocess.check_output('git stash list', shell=True)
    	if substring in outputfromList:
	    runGit()
	    for abc in glob.glob("clone*.csv"):
   		file(abc)
	else:	
	    removeExcess()
	    break

if __name__=="__main__":
    try:
        startGit()
        versionControl(60)
        unPop()
    except IOError:
        pass
