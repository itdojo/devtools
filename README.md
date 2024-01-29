# Devtools

This python package is a comprised of a growing number of modules that are aimed as simplifying things that I commonly do when scripting using python.

The modules include:
* [**`drawLine`**](#drawline) - Draws a line separator across the screen matching the width of your terminal. There are several line separator styles.
* [**`getOS`**](#getos) - Returns the OS the script is running on (Windows, MacOS, Linux).  I use it to determine if my script can continue (Example: if my script will only run on Linux).  getOS only returns the OS, it's up to you to do decide what to do with that info in your script.
* [**`macFormatter`**](#macformatter) - Returns a MAC address in the format you desire, regardless of the input format.  If you give it aa-bb-cc-dd-ee-ff it can return aa:bb:cc:dd:ee:ff or aabbccddeeff or aa.bb.cc.dd.ee.ff, etc.  It can also toggle case if that matters.  This is very helpful for cleaning up MAC addresses to be in the right format for your scripts.
* [**`ouiLookup`**](#ouilookup) - Given a MAC address it will use the IEEE oui.txt file to look up the name of the vendor.  If oui.txt is not available in the local directory, the module will download it from the Internet.  This may cause a delay the first time it is used.  Subsequent lookups are fast.  If desired, you can pre-download the oui.txt file from http://standards-oui.ieee.org/oui/oui.txt.
* [**`rootCheck`**](#rootcheck) - Checks to see if the script is running as root.  If not root, it will exit the script you are running (so don't use this if you script does not need to be root).
* [**`shellCommand`**](#shellcommand) - Provide a command as a string (Ex. "`ip link set {iface} down`") to this module and it will return the result (STDIN and STDERR).
* [**`wifiSelector`**](#wifiselector) - This tool only works on Linux and retrieves all wlan interfaces on the system.  It also has a function to create a list of the available interfaces to the user.  Optionally, it will also show the interface MAC address and OUI vendor name.

## devtools Modules

### drawline

### getOS

### macFormatter

### ouiLookup

### rootCheck

### shellCommand

### wifiSelector