# 🌑 SPY NET WIFI SHADOW
> **The Ultimate Wireless Security & Network Vulnerability Auditor**

![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Termux%20(Root)-red.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Premium%20Audit%20Tool-orange.svg)

**SPY-NET-SHADOW** adalah framework audit keamanan jaringan tingkat lanjut yang dirancang untuk mendeteksi kerentanan pada infrastruktur Wi-Fi. Dikembangkan untuk profesional keamanan siber di bawah bendera **SPY-E & 123Tool**.

## 🛡️ Core Capabilities
- **Advanced Reconnaissance:** Pemindaian perangkat dengan identifikasi vendor otomatis.
- **Deauth-Force:** Pengujian ketahanan client terhadap serangan deautentikasi (MFP detection).
- **Traffic Analysis:** Sniffing paket data secara real-time untuk audit enkripsi.
- **Vulnerability Testing (MITM):** Simulasi kerentanan ARP spoofing & DNS redirection untuk edukasi.
- **Rogue AP Simulation:** Pengujian kesadaran pengguna melalui Captive Portal tiruan.

## 📦 Installation & Setup

### Linux (Kali / Parrot / Ubuntu)
```bash
git clone https://github.com/123tool/Spy-Net-Wifi-Shadow.git
cd Spy-Net-Wifi-Shadow
sudo chmod +x install.sh
sudo ./install.sh
```
### Termux (Rooted Only)
​Gunakan external adapter yang mendukung Monitor Mode & Packet Injection
```bash
pkg update && pkg upgrade
pkg install python git tshark aircrack-ng root-repo
git clone https://github.com/123tool/Spy-Net-Wifi-Shadow.git
cd Spy-Net-Wifi-Shadow
python spy-shadow.py
```
### How to Run
```bash
sudo python3 spy-shadow.py
```
# Disclaimer

**​Alat ini disediakan hanya untuk tujuan Edukasi dan Pengujian Penetrasi Resmi. Penggunaan tanpa izin tertulis dari pemilik aset jaringan adalah tindakan ilegal. SPY-E & 123Tool tidak bertanggung jawab atas penyalahgunaan alat ini.**
