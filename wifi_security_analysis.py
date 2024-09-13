import os

import subprocess

import platform

import time

from scapy.all import *

from threading import Thread



def getOutputCommand(command, duration=0):

    try:

        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        if duration > 0:

            time.sleep(duration)

        return result.stdout

    except subprocess.CalledProcessError as e:

        print(f"Command '{command}' failed with error: {e}")

        print(f"Output:\n{e.output}")

        exit()



def getInterfaces():

    interfaces = []

    command = "iwconfig"

    output = getOutputCommand(command)

    for line in output.splitlines():

        if "IEEE 802.11" in line:

            interface = line.split()[0]

            interfaces.append(interface)

    return interfaces



def showInterfaces(interfaces):

    if not interfaces:

        print("No wireless interfaces found")

        exit()

    else:

        print("Wireless interfaces found:")

        print("_" * 43)

        print("| Index |            Interfaces           |")

        print("|" + "-" * 7 + "|" + "-" * 34 + "|")

        for index, interface in enumerate(interfaces, start=1):

            print(f"| {index:5} | {interface: <32} |")

            print("|" + "-" * 7 + "|" + "-" * 34 + "|")



        print("Select which interface you want to use: ")

        while True:

            choice = input(" >> ")

            if choice.isdigit():

                choice = int(choice)

                if 1 <= choice <= len(interfaces):

                    return interfaces[choice - 1]

                else:

                    print(f"Choose a valid number between 1 and {len(interfaces)}")

            else:

                print("Please enter a number")



def enable_monitor_mode(interface):

    os.system(f"sudo ifconfig {interface} down")

    os.system(f"sudo iwconfig {interface} mode monitor")

    os.system(f"sudo ifconfig {interface} up")

    os.system(f"sudo airmon-ng check kill")



def scan_networks(interface):

    def packet_handler(pkt):

        if pkt.haslayer(Dot11Beacon):

            ssid = pkt[Dot11Elt].info.decode()

            bssid = pkt[Dot11].addr2

            print(f"SSID: {ssid}, BSSID: {bssid}")



    sniff(iface=interface, prn=packet_handler, timeout=10)





"""def run_airodump(interface, duration):

    try:

        # Start airodump-ng process

        process = subprocess.Popen(['sudo', 'airodump-ng', interface], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        

        # Wait for the specified duration

        time.sleep(duration)

        

        # Terminate the airodump-ng process

        process.terminate()

        process.wait()



        # Read and return the output

        output, errors = process.communicate()

        if process.returncode != 0:

            print(f"Error in airodump-ng: {errors}")

        return output

    except Exception as e:

        print(f"Error running airodump-ng: {e}")

        exit()

"""

def main():

    #os_type = str(platform.system())

    os_type = "Linux"

    if os_type in ['Linux', 'Darwin']:

        interfaces = getInterfaces()

        selected_interface = showInterfaces(interfaces)

        enable_monitor_mode(selected_interface)

        monitor_interface = selected_interface+"mon"

        scan_networks(monitor_interface)

    else:

        print(f"This script is incompatible with {os_type}")

        exit()



if __name__ == "__main__":

    main()

