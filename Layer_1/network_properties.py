from dataclasses import dataclass


@dataclass
class NetworkProperties:
    ip_addr: str
    mac_addr: str
    subnet_mask: int
    is_configured: bool

    def __init__(self, ip: str, mac: str, subnet: int) -> None:
        self.ip_addr = ip
        self.mac_addr = mac
        self.subnet_mask = subnet
        self.is_configured = True
