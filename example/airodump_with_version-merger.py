import subprocess
import time
 
while True:
    subprocess.call('ifconfig wlan0 down', shell=True)
    time.sleep(1)
    subprocess.call('iwconfig wlan0 mode monitor', shell=True)
    time.sleep(1)
    subprocess.call('ifconfig wlan0 up', shell=True)
    time.sleep(1)
    file = open('clone.csv', 'w+')
    subprocess.Popen('sudo airodump-ng wlan0 -w dump', shell=True)
    print "Success Air"
    time.sleep(1)
    subprocess.Popen('python ../versioning.py', shell=True)
    print "Success Stash"
    time.sleep(900)
    subprocess.call('sudo pkill airodump-ng', shell=True)
    subprocess.call('sudo pkill versioning.py', shell=True)
    subprocess.call('sudo python ../merge.py', shell=True)
    time.sleep(1)
    file.close
