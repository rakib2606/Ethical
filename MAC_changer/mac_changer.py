#!/bin/usr/env python
import subprocess
import optparse
import re

def argument ():
    parser= optparse.OptionParser()
    parser.add_option("-i", "--interface", dest= "interface", help="Interface for changing MAC")
    parser.add_option("-m", "--mac", dest= "new_mac", help="Getting MAC")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[+] Please Provide interface")
    elif not options.new_mac:
        parser.error("[+] Please Provide MAC address")
    return options

def changing_mac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface +  " to " + new_mac )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def current_mac(interface):
    check_output = subprocess.check_output(["ifconfig", interface])
    mac_change = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", check_output)
    if mac_change:
        return mac_change.group(0)
    else:
        print("MAC don't read")

options = argument()
new_current_mac = current_mac(options.interface)
print("Current MAC = " + str(new_current_mac) )
# changing_mac(options.interface, options.new_mac)





