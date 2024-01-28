#!/usr/bin/env python3

# Standard library imports
import sys

# devgru modules
import devgru_tools.wifiSelector as wifiSelector
import devgru_tools.rootCheck as rootCheck
import devgru_tools.getOS as getOS
import devgru_tools.ouiLookup as ouiLookup
import devgru_tools.macFormatter as macFormatter
import devgru_tools.shellCommand as shellCommand


def fatal_error(error_msg, code=1):
    print(f"\n❌  {error_msg}")
    sys.exit(code)


def config_wlan_interface(iface, mode, channel=None):
    link_down = f"ip link set dev {iface} down"
    link_up = f"ip link set dev {iface} up"
    set_mode = f"iw dev {iface} set type {mode}"
    set_channel = f"iw dev {iface} set channel {channel}"
    get_iface_mode = f"iw {iface} info"
    cmd_result = []
    cmd_result = shellCommand.run_shell_cmd(link_down)
    shellCommand.run_shell_cmd(set_mode)
    if channel is not None:
        shellCommand.run_shell_cmd(set_channel)
    shellCommand.run_shell_cmd(link_up)
    shellCommand.run_shell_cmd(get_iface_mode)


def main():
    rootCheck.check_root()  # Confirm script is run as root

    # Check OS
    if getOS.os_is() != "Linux":
        error_msg = f"This tool only runs on Linux.\n"
        fatal_error(error_msg)

    # Get list of wireless interfaces
    wifi_interfaces = wifiSelector.get_wifi_interfaces()
    if wifi_interfaces is None:
        error_msg = f"No wireless interfaces found.\nExiting."
        fatal_error(error_msg)
    
    # Present the user with a list of interfaces to choose from
    # linetype = 1 to 5
    sniffer_iface = wifiSelector.interface_selector(wifi_interfaces, showmac=True, linetype=1)
    if sniffer_iface is None:
        error_msg = "No interface selected.\nExiting."
        fatal_error(error_msg)


if __name__ == "__main__":
    main()
