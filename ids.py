from datetime import datetime
from scapy.all import IP, TCP, sniff

ips, ports = {"192.168.1.100", "10.0.0.5"}, {4444, 5555}

def alert(p):
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip, tcp = p[IP], p[TCP]
    if ips & {ip.src, ip.dst}:
        print(f"[ALERT] [{t}] Suspicious IP: {ip.src} -> {ip.dst}")
    if ports & {tcp.sport, tcp.dport}:
        print(f"[ALERT] [{t}] Suspicious Port: {ip.src}:{tcp.sport} -> {ip.dst}:{tcp.dport}")

print("Starting IDS... Press Ctrl+C to stop.")
sniff(filter="ip and tcp", prn=alert, store=0)