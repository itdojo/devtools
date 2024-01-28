import os.path
import re
import devgru_tools.macFormatter as mac_formatter


def oui_lookup(mac_address, case="upper", seperator=""):
    """
    Lookup the OUI for a given MAC address.

    Args:
        mac_address (str): MAC address to lookup.

    Returns:
        OUI (str) if found, None otherwise.
    """
    if not check_for_oui_file():
        download_oui_file()

    ouifile = "oui.txt"

    mac_address = mac_formatter.format_mac_address(mac_address, case, seperator)
    mac_address = re.sub(r"[^A-F0-9]", "", mac_address)
    node_oui = mac_address[:6]

    with open(ouifile, 'r') as f:
        filedata = f.readlines()
        for line in filedata:
            if node_oui in line:
                vendor = line.replace("\t", "").replace("(base 16)", "").replace("\n", "")[8:]
                return vendor
        return "Vendor Unknown"


# OUI Lookup
def check_for_oui_file():
    """
    Check if the oui.csv and oui.txt files are present in the current directory.

    Returns:
        True if oui.csv and oui.txt are present, False otherwise.
    """
    oui_txtfile = "oui.txt"  # http://standards-oui.ieee.org/oui/oui.txt

    oui_txt = os.path.isfile(oui_txtfile)
    if oui_txt:
        return True
    else:
        return False


def download_oui_file():
    """
    Download the oui.txt file from the IEEE website.

    Returns:
        True if the file is downloaded successfully, False otherwise.
    """
    import requests

    oui_url = "http://standards-oui.ieee.org/oui/oui.txt"
    ouifile = "oui.txt"

    try:
        r = requests.get(oui_url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"Error downloading oui.txt: {err}")
        return False

    with open(ouifile, "wb") as f:
        f.write(r.content)

    return True
