import subprocess
import time

while True:
    # Creates a file clone.csv to temporarily store the cloned copies
    file = open('clone.csv', 'w+')
    subprocess.Popen('python randomizing_csv.py', shell=True)
    time.sleep(1)
    
    # Version controls the CSV or database file to be saved in 15 minutes
    subprocess.Popen('python ../versioning.py', shell=True)
    print "Success Stash"
    time.sleep(900)
    subprocess.call('sudo pkill -1 -f randomizing_csv.py', shell=True)
    subprocess.call('sudo pkill -1 -f versioning.py', shell=True)
    
    # Merges all the version controls of the CSV or database file
    subprocess.call('sudo python ../merge.py', shell=True)
    time.sleep(1)
    file.close
