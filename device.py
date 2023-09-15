from network_properties import NetworkProperties
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from interface import Interface


class Device:
    name: str
    ports: list["Interface"]
    network_properties: "NetworkProperties"

    def __init__(self, name: str, ip: str, mac: str, subnet: int) -> None:
        self.name = name
        self.ports = list()
        self.network_properties = NetworkProperties(ip, mac, subnet)

    def __repr__(self) -> str:
        output = f"\033[36mDevice Name:\033[00m {self.name}\n"
        output += f"\t\033[36mIP Addr:\033[00m \033[35m{self.network_properties.ip_addr}/{self.network_properties.subnet_mask}\033[00m\n"
        output += f"\t\033[36mMAC Addr:\033[00m \033[35m{self.network_properties.mac_addr}\033[00m\n"
        for interface in sorted(self.ports):
            output += repr(interface)
        output += "\n"

        return output
