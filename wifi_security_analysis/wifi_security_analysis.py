import os
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk
from scapy.all import sniff, Dot11, Dot11Beacon, Dot11Elt, EAPOL, wrpcap
import time


# Colors
def print_red(text):
    print(f"\033[91m{text}\033[0m")
def print_green(text):
    print(f"\t\t\033[92m{text}\033[0m")
def print_yellow(text):
    print(f"\033[93m{text}\033[0m")
def print_blue(text):
    print(f"\033[94m{text}\033[0m")
def print_magenta(text):
    print(f"\033[95m{text}\033[0m")
def print_cyan(text):
    print(f"\033[96m{text}\033[0m")


def enable_monitor_mode(interface):
    print_blue(f"Enabling monitor mode on {interface}")
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo iwconfig {interface} mode monitor")
    os.system(f"sudo ifconfig {interface} up")

def command_output(command, duration=0):
    try:
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        if duration > 0:
            time.sleep(duration)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print_red(f"Command '{command}' failed with error: {e}")
        print(f"Output:\n{e.output}")
        exit()

def get_interfaces():
    interfaces = []
    command = "iwconfig"
    output = command_output(command)
    for line in output.splitlines():
        if "IEEE 802.11" in line:
            interface = line.split()[0]
            interfaces.append(interface)
    return interfaces

def show_interfaces(interfaces):
    if not interfaces:
        print_red("No wireless interfaces found")
        exit()
    else:
        print_blue("Wireless interfaces found:")
        print("_" * 43)
        print("| Index |             Interfaces           |")
        print("|" + "-" * 7 + "|" + "-" * 34 + "|")
        for index, interface in enumerate(interfaces, start=1):
            print(f"| {index:5} | {interface: <32} |")
            print("|" + "-" * 7 + "|" + "-" * 34 + "|")

        print_blue("\nSelect which interface you want to use: ")
        while True:
            choice = input(" >> ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(interfaces):
                    print(interfaces[choice - 1])
                    return interfaces[choice - 1]
                else:
                    print_red(f"Choose a valid number between 1 and {len(interfaces)}")
            else:
                print_red("Please enter a number")

def scan_networks(interface, duration=100):
    networks = set()
    def packet_handler(pkt):
        if pkt.haslayer(Dot11Beacon):
            ssid = pkt[Dot11Elt].info.decode('utf-8', errors='ignore')
            bssid = pkt[Dot11].addr2
            if ssid and (ssid, bssid) not in networks:
                networks.add((ssid, bssid))
                network_list.insert(tk.END, f"{ssid} ({bssid})")
                print(f"Found network: SSID={ssid}, BSSID={bssid}")

    print_blue(f"Scanning for networks on {interface} for {duration} seconds...")
    sniff(iface=interface, prn=packet_handler, timeout=duration)
    print_red("Scan complete.")

def start_analysis():
    selected_network = network_list.get(tk.ACTIVE)
    if selected_network:
        ssid, bssid = selected_network.rsplit('(', 1)
        bssid = bssid.rstrip(')')
        messagebox.showinfo("Analysis Started", f"Started analysis on {selected_network}")
        # Perform analysis here (e.g., call capture_handshake, crack_password)
        capture_handshake(interfaceSelected, bssid)
        generate_report(selected_network)
    else:
        messagebox.showwarning("No Selection", "Please select a network to analyze.")

def capture_handshake(interface, bssid):
    def packet_handler(pkt):
        if pkt.haslayer(EAPOL):
            wrpcap("handshake.pcap", pkt, append=True)
            print_green("Handshake captured")

    print_blue(f"Capturing handshake on {interface} for BSSID={bssid}")
    sniff(iface=interface, prn=packet_handler, stop_filter=lambda x: x.haslayer(EAPOL))
    print_blue("Capture complete.")

def crack_password(pcap_file, wordlist):
    os.system(f"aircrack-ng -w {wordlist} -b {bssid} {pcap_file}")

def generate_report(network):
    report = f"Report for {network}\n\nVulnerabilities:\n- Weak password\n\nMitigations:\n- Use a stronger password\n- Enable WPA3\n"
    with open("report.txt", "w") as file:
        file.write(report)
    messagebox.showinfo("Report Generated", "Report generated successfully.")

# Main script
interfaces = get_interfaces()
interfaceSelected = show_interfaces(interfaces)
enable_monitor_mode(interfaceSelected)

# Tkinter GUI setup
app = tk.Tk()
app.title("WiFi Security Analysis Tool")
app.geometry("500x400")
app.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TListbox", font=("Helvetica", 12))

scan_frame = ttk.Frame(app, padding="10")
scan_frame.pack(pady=10)

scan_label = ttk.Label(scan_frame, text="Select an interface and click Scan:")
scan_label.grid(row=0, column=0, columnspan=2, pady=5)

scan_button = ttk.Button(scan_frame, text="Scan", command=lambda: scan_networks(interfaceSelected))
scan_button.grid(row=1, column=0, columnspan=2, pady=5)

network_list = tk.Listbox(app, font=("Helvetica", 12))
network_list.pack(pady=10, fill=tk.BOTH, expand=True)

analyze_button = ttk.Button(app, text="Analyze Network", command=start_analysis)
analyze_button.pack(pady=10)

app.mainloop()
