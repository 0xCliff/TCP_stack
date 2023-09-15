from network_graph import NetworkGraph
from utils import make_mac_address


def build_ring_topology() -> NetworkGraph:
    ring = NetworkGraph("Ring topology")

    R0 = ring.add_device("Router_0", "192.168.1.0", make_mac_address(), 24)
    R1 = ring.add_device("Router_1", "192.168.2.0", make_mac_address(), 24)
    R2 = ring.add_device("Router_2", "192.168.3.0", make_mac_address(), 24)

    ring.add_link_between_devices(R1, R2, "FastEthernet 0/1", "FastEthernet 0/0", 1)
    ring.add_link_between_devices(R2, R0, "FastEthernet 0/1", "FastEthernet 0/0", 1)
    ring.add_link_between_devices(R0, R1, "FastEthernet 0/1", "FastEthernet 0/0", 1)

    return ring


def build_star_topology() -> NetworkGraph:
    star = NetworkGraph("Star topology")

    switch = star.add_device("Switch", "192.168.1.1", make_mac_address(), 24)
    PC1 = star.add_device("PC1", "192.168.1.2", make_mac_address(), 24)
    PC2 = star.add_device("PC2", "192.168.1.3", make_mac_address(), 24)
    PC3 = star.add_device("PC3", "192.168.1.4", make_mac_address(), 24)
    PC4 = star.add_device("PC4", "192.168.1.5", make_mac_address(), 24)
    PC5 = star.add_device("PC5", "192.168.1.6", make_mac_address(), 24)

    star.add_link_between_devices(
        switch, PC1, "FastEthernet 0/0", "FastEthernet 0/0", 1
    )
    star.add_link_between_devices(
        switch, PC2, "FastEthernet 0/1", "FastEthernet 0/0", 1
    )
    star.add_link_between_devices(
        switch, PC3, "FastEthernet 0/2", "FastEthernet 0/0", 1
    )
    star.add_link_between_devices(
        switch, PC4, "FastEthernet 0/3", "FastEthernet 0/0", 1
    )
    star.add_link_between_devices(
        switch, PC5, "FastEthernet 0/4", "FastEthernet 0/0", 1
    )

    return star
