#! usr/bin/env python

import subprocess
import optparse
import re

pa=optparse.OptionParser()

pa.add_option("-i","--interface",dest="Interface",help="use to select interface")
pa.add_option("-m","--mac",dest="New_mac",help="use to give new mac")
(options,args)=pa.parse_args()

def changemac(interface,nmac):
    if not interface:
        pa.error("[-] specify interface , use -h for more info")
    elif not nmac:
        pa.error("[-] specify mac , use -h for more info")
    else:
        print("[+] Changing Mac address")
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",nmac])
        subprocess.call(["ifconfig",interface,"up"])



def get_current_mac(interface):
    output = subprocess.check_output(["ifconfig", options.Interface]).decode("utf-8")
    mac_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)

    if mac_output:
        return mac_output.group(0)
    else:
        print("[-]Mac not found")

getmc= get_current_mac(options.Interface)
print("old mac = ",str(getmc))
changemac(options.Interface,options.New_mac)
changedmac=get_current_mac(options.Interface)
print("changed mac=",changedmac)
