import subprocess
import time

while True:
    # Configures the Wi-Fi card interface to enter into monitor-mode. wlan0 is set as default.
    subprocess.call('ifconfig wlan0 down', shell=True)
    time.sleep(1)
    subprocess.call('iwconfig wlan0 mode monitor', shell=True)
    time.sleep(1)
    subprocess.call('ifconfig wlan0 up', shell=True)
    time.sleep(1)
    
    # Creates a file clone.csv to temporarily store the cloned copies
    file = open('clone.csv', 'w+')
    subprocess.Popen('sudo airodump-ng wlan0 -w dump', shell=True)
    time.sleep(1)
    
    # Version controls the CSV or database file to be saved in 15 minutes
    subprocess.Popen('python ../versioning.py', shell=True)
    print "Success Stash"
    time.sleep(900)
    subprocess.call('sudo pkill airodump-ng', shell=True)
    subprocess.call('sudo pkill versioning.py', shell=True)
    
    # Merges all the version controls of the CSV or database file
    subprocess.call('sudo python ../merge.py', shell=True)
    time.sleep(1)
    file.close
