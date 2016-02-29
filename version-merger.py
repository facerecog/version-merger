import subprocess
import time

while True:
    file = open('clone.csv', 'w+')
    subprocess.Popen('python versioning.py', shell=True)
    time.sleep(900)
    subprocess.call('python merge.py', shell=True)
    time.sleep(1)
    file.close
