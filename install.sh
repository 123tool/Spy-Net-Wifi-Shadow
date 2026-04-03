#!/bin/bash
# Installer for SPY-NET-WIFI-SHADOW
# SPY-E & 123Tool Official

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}[*] Memulai Instalasi Dependensi...${NC}"

if [[ -d /data/data/com.termux ]]; then
    pkg update && pkg upgrade -y
    pkg install python nmap tcpdump aircrack-ng -y
    pip install scapy
else
    sudo apt-get update
    sudo apt-get install -y python3-pip nmap aircrack-ng dsniff
    sudo pip3 install scapy tabulate
fi

chmod +x spy-shadow.py
echo -e "${GREEN}[+] Instalasi Selesai! Jalankan dengan: sudo python3 spy-shadow.py${NC}"
