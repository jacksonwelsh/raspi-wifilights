#!/usr/local/bin/python

import time, sys
import config.py
import pifacedigitalio                                                                  #Library for pifacedigitalio
from ubidots import ApiClient                                                           #Library for Ubidots

try:
    pifacedigital = pifacedigitalio.PiFaceDigital()                                     #Declare piface object
except:
    print "PiFace not connected"
    sys.exit(0)

def setPin(pin, value):
    for a in value:
        if(a['value']):                                                                  
                pifacedigital.output_pins[pin + 2].turn_on()
        else:
                pifacedigital.output_pins[pin + 2].turn_off()

#Connect to Ubidots

try:
    print "Requesting Ubidots token"
    api = ApiClient(config.ACCOUNT_KEY)                           # Replace with your Ubidots API Key here
except:
    print "No internet connection"
    sys.exit(0)

print "Getting variables"
try:
    output2_control = api.get_variable(config.OUTPUT2_KEY)                         #Put here your output2 variable ID
    relay0_control = api.get_variable(config.RELAY0_KEY)                          #Put here your R0 control variable ID
    print "Connected to Ubidots"

except:
    print "No internet connection or no variables found"
    sys.exit(0)

while(True):
    # Read control variables

    lastValue0 = relay0_control.get_values(1)
    lastValue2 = output2_control.get_values(1)

    # Set pins to the values received

    setPin(0,lastValue0)
    setPin(2,lastValue2)
