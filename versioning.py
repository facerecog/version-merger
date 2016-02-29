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

def removeJunk():
    for fl in glob.glob("*kismet.csv"):
        os.remove(fl)
    for gl in glob.glob("*.cap"):
        os.remove(gl)
    for hl in glob.glob("*.netxml"):
        os.remove(hl)
def startGit():
    subprocess.call('git init', shell=True)
    subprocess.call('git config --global user.email "you@example.com"', shell=True)
    subprocess.call('git config --global user.name "Your Name"', shell=True)
    subprocess.call('git add clone.csv', shell=True)
    subprocess.call('git commit -m "First Commit"', shell=True)

startGit()
while True:
    removeJunk()
    newest = max(glob.iglob("dump*.csv"), key=os.path.getctime)
    stash(newest)
    print newest
