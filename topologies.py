from Layer_1 import NetworkGraph
from utils import make_mac_address


def build_ring_topology() -> NetworkGraph:
    ring = NetworkGraph("Ring topology")

    R0 = ring.add_node("R0", "192.168.1.0", make_mac_address(), 24)
    R1 = ring.add_node("R1", "192.168.2.0", make_mac_address(), 24)
    R2 = ring.add_node("R2", "192.168.3.0", make_mac_address(), 24)

    ring.add_link_between_nodes(R0, R1, "eth0/0", "eth0/0", 1)
    ring.add_link_between_nodes(R1, R2, "eth0/1", "eth0/0", 1)
    ring.add_link_between_nodes(R2, R0, "eth0/1", "eth0/1", 1)

    return ring


def build_star_topology() -> NetworkGraph:
    star = NetworkGraph("Star topology")

    R0 = star.add_node("R0", "192.168.1.0", make_mac_address(), 24)
    R1 = star.add_node("R1", "192.168.2.0", make_mac_address(), 24)
    R2 = star.add_node("R2", "192.168.3.0", make_mac_address(), 24)
    R3 = star.add_node("R3", "192.168.4.0", make_mac_address(), 24)
    R4 = star.add_node("R4", "192.168.5.0", make_mac_address(), 24)
    R5 = star.add_node("R5", "192.168.6.0", make_mac_address(), 24)

    star.add_link_between_nodes(R0, R1, "eth0/0", "eth0/0", 1)
    star.add_link_between_nodes(R0, R2, "eth0/1", "eth0/0", 1)
    star.add_link_between_nodes(R0, R3, "eth0/2", "eth0/0", 1)
    star.add_link_between_nodes(R0, R4, "eth0/3", "eth0/0", 1)
    star.add_link_between_nodes(R0, R5, "eth0/4", "eth0/0", 1)

    return star
