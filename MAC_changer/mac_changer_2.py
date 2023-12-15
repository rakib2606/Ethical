#!/usr/bin/env python

import subprocess
import optparse
import re

def argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help= "Interface for changing mac adderess")
    parser.add_option("-m", "--mac", dest = "new_mac", help= "Getting New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please Provide interface")
    elif not options.new_mac:
        parser.error("[-] Please Provide New MAC Address")
    return options


def changing_mac(interface,new_mac):
    print("[+] Changing new MAC for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down" ])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    check_output = subprocess.check_output(["ifconfig", interface])
    mac_change = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", check_output)
    if mac_change:
        return mac_change.group(0)
    else:
        print("MAC did not change")

options = argument()
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac))
changing_mac(options.interface, options.new_mac)
new_current_mac = get_current_mac(options.interface)
if new_current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + new_current_mac)
else:
    print("[-] MAC did not changed")
