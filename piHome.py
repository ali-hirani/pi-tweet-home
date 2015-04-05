#!/usr/bin/python

import subprocess
import time


from twython import Twython

APP_KEY = ''  # Customer Key here
APP_SECRET = ''  # Customer secret here
OAUTH_TOKEN = ''  # Access Token here
OAUTH_TOKEN_SECRET = ''  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def checkIfHome(ip):
        output = subprocess.Popen(["ping","-c", "1", ip],stdout = subprocess.PIPE,shell=False)
        check = output.communicate()[0]
        check = output.returncode

        return check


ipAddress = "" # Device IP here
sleepTime = 2

run = True

try:
        while(run):

                residentHome = checkIfHome(ipAddress)

                if residentHome == 0:
                        print ("Welcome Home!")
                        time.sleep(sleepTime)
            twitter.update_status(status="You've arrived home at: " + time.strftime("%X"))
            quit()
                else:
                        print ("No one home")
                        time.sleep(sleepTime)

except KeyboardInterrupt:
        print ("Done")