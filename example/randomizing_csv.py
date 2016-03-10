import random
import time

# A function which creates and overwrite a csv file called dump.csv
while True:
    file = open('dump.csv','w')
    file.seek(0) # Changes the first line  
    random_string = str(random.randint(1,20))
    file.write(random_string)
    file.close()
    time.sleep(1)
