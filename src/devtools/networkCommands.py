def link_down(iface):
    return f"ip link set dev {iface} down"

def link_up(iface):
    return f"ip link set dev {iface} up"

def set_mode(iface, mode):
    return f"iw dev {iface} set type {mode}"

def set_channel(iface, channel):
    return f"iw dev {iface} set channel {channel}"

def get_iface_mode(iface):
    return f"iw {iface} info"
