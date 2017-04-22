import md5
from datetime import datetime
import time
from time import sleep

now = datetime.now()
the_hour = now.hour
the_min = now.minute
the_sec = now.second

counter = 1

pass_in = raw_input("\nPlease Enter the MD5 Hash: ")
pwfile = raw_input("\nPlease Enter the File Name: ")

try:
    pwfile = open(pwfile, "r")
except:
    print("\nERROR: Could not Find File")
    quit()

for password in pwfile:
    filemd5 = md5.new(password.strip()).hexdigest()
    print("Password Attempt %d: %s") % (counter, password.strip())

    counter += 1

    if pass_in == filemd5:
        print("\nMatch Found. \nPassword is: %s") % password

        now2 = datetime.now()
        the_hour2 = now2.hour
        the_min2 = now2.minute
        the_sec2 = now2.second

        print('\nStarted at ' + str(the_hour) + ":" + str(the_min) + "." + str(the_sec))
        print('Ended at ' + str(the_hour2) + ":" + str(the_min2) + "." + str(the_sec2) + "\n")
        break

else:
    now2 = datetime.now()
    the_hour2 = now2.hour
    the_min2 = now2.minute
    the_sec2 = now2.second

    print("\nPassword Not Found")

    print('\nStarted at ' + str(the_hour) + ":" + str(the_min) + "." + str(the_sec))
    print('Ended at ' + str(the_hour2) + ":" + str(the_min2) + "." + str(the_sec2) + "\n")
