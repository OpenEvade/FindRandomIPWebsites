import ipaddress
import socket
from os import system as s
import random


def new():
  return str(random.randrange(255)) + "." + str(random.randrange(255)) + "." + str(random.randrange(255)) + "." + str(random.randrange(255))

common_ports = [443, 8080, 80]
for x in range(19):
  add = new()
  for i in common_ports:
      
    print("[+] Scanning " + add + ":" + str(i))

    print(" Status:")
    s(f"curl http://ip-api.com/line/{add}?fields=status")
    print(" Message:")
    s(f"curl http://ip-api.com/line/{add}?fields=message")
    print(" Country:")
    
    s(f"curl http://ip-api.com/line/{add}?fields=country")
    print("-" * 8)
