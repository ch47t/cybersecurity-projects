# WiFi Security Analysis Tool

The **WiFi Security Analysis Tool** is designed to scan WiFi networks, capture WPA/WPA2 handshakes, analyze network security, and attempt to crack network passwords using a wordlist. It provides a GUI to manage operations and generates reports on network vulnerabilities.

## Requirements

To run the WiFi Security Analysis Tool, ensure your environment meets the following requirements:

### Python Version

- Python 3.x (Tested on Python 3.11)

### Required Modules

- `os`: For interacting with the operating system to manage network interfaces and run commands.
- `subprocess`: To run shell commands for enabling monitor mode, scanning, and password cracking.
- `tkinter`: To create the graphical user interface (GUI).
- `scapy`: To handle network packet sniffing and capture WPA/WPA2 handshakes.
- `time`: For timing delays and operations during scans.

### External Tools

- **Aircrack-ng**: Required for cracking WPA/WPA2 handshake packets.
- **Wordlist**: A password list used to attempt cracking the captured handshake (e.g., `rockyou.txt`).

### Operating System

- Linux OS with root privileges (required to access and manage wireless interfaces).

### Hardware

- A wireless network adapter capable of monitor mode.

## Usage

1. Run the script to launch the tool and list available wireless interfaces.
2. Select a wireless interface and enable monitor mode.
3. Scan for nearby WiFi networks.
4. Select a network to analyze, capture the WPA/WPA2 handshake, and attempt to crack the password using a wordlist.
5. Generate a security report for the selected network.

```sh
python3 wifi_security_tool.py
