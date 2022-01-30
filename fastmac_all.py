#!/usr/bin/env python
# (c) J~Net 2017
# python fastmac_all.py wlan0

import random
import pwd
import os
import sys
import re

if len(sys.argv)<2:
    os.system("clear")
    os.system("ifconfig")
    adaptor=raw_input("Choose Adapter & Press Enter To Continue. ");
    
else:
    adaptor=sys.argv[1]

def randomMAC():
    return [ 0x00, 0x16, 0x3e,
        random.randint(0x00, 0x7f),
        random.randint(0x00, 0xff),
        random.randint(0x00, 0xff) ]

def MACprettyprint(mac):
    return ':'.join(map(lambda x: "%02x" % x, mac))

if __name__ == '__main__':
    newmac = (MACprettyprint(randomMAC()))
   # raw_input("Press Enter To Start Mac Changer...");
    os.system("sudo ifconfig " + adaptor + " down")
    combined = ' '.join([newmac,adaptor])
    os.system("sudo macchanger -m " + combined + "")
    os.system("sudo service network-manager restart")
    os.system("sudo ifconfig " + adaptor + " up")
