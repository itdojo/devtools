import os
from sys import exit
from devgru_tools import getOS
from devgru_tools import ouiLookup
from devgru_tools import drawLine


def get_wifi_interfaces():
    if getOS.os_is() != "Linux":
        print("\nThis tool only runs on Debian/Ubuntu versions of Linux.\nExiting.\n")
        exit(1)
    
    if_dir = "/sys/class/net"
    interfaces = os.listdir(if_dir)
    wlan_interfaces = {}
    for iface in interfaces:
        wireless_dir = os.path.join(if_dir, iface, 'wireless')
        if os.path.isdir(wireless_dir):
            address_file = os.path.join(if_dir, iface, 'address')
            if os.path.isfile(address_file):
                with open(address_file, 'r') as f:
                    mac_address = f.read().strip()
            wlan_interfaces[iface] = mac_address

    return wlan_interfaces


def interface_selector(wlan_interfaces, showmac=True, linetype=1):
    drawLine.draw_line(linetype)
    print(" WLAN Interface Selector")
    drawLine.draw_line(linetype)
    for count, (interface, mac_address) in enumerate(wlan_interfaces.items(), start=1):
        if showmac:
            oui = ouiLookup.oui_lookup(mac_address)
            print(f"{count}. {interface}  ({mac_address}) ({oui.strip()})")
        else:
            print(f"{count}.  {interface}")
    print()

    attempt_count = 0
    max_attempts = 3

    while attempt_count < max_attempts:
        choice = input("#️⃣  Enter WLAN interface by number ('q' to quit, 'r' to refresh): ").strip()
        if choice.lower() == 'r':
            wlan_interfaces = get_wifi_interfaces()
            refresh = interface_selector(wlan_interfaces, showmac)
            if refresh is None:
                return None
        elif choice.lower() == 'q':
            print("Quitting WLAN Interface Selection.")
            return None

        if choice.isdigit() and 1 <= int(choice) <= len(wlan_interfaces.keys()):
            return [x for x in wlan_interfaces.keys()][int(choice) - 1]
        else:
            print("❌  Invalid. Enter a number from the list (1, 2, etc.).\n")
            attempt_count += 1

    print("Maximum attempts reached. Exiting.")
    return None







