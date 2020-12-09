#!/usr/bin/python

import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ip-range", dest="ip", help="ip range you want to scan")
    (options, arguments) = parser.parse_args()

    if not options.ip:
        parser.error("Please specify an ip range")
    else:
        return options

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t"+element[1].hwsrc)
options = get_arguments()

scan(options.ip)
