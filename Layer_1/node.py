from .network_properties import NetworkProperties


class Node:
    node_name: str
    interfaces: list
    props: NetworkProperties

    def __init__(self, name: str, ip: str, mac: str, subnet: int) -> None:
        self.node_name = name
        self.interfaces = list()
        self.props = NetworkProperties(ip, mac, subnet)

    def __repr__(self) -> str:
        output = f"\033[36mNode Name:\033[00m {self.node_name}\n"
        output += f"\t\033[36mIP Addr:\033[00m \033[35m{self.props.ip_addr}/{self.props.subnet_mask}\033[00m\n"
        for intf in self.interfaces:
            output += f"\t\033[36mInterface Name:\033[00m {intf.interface_name}\n"
            output += f"\t\033[36mFrom Node:\033[00m {intf.from_node.node_name}, \033[36mTo Node:\033[00m {intf.to_node.node_name}, \033[36mWeight:\033[00m {intf.cost}\n"
            output += f"\t\033[36mNode MAC Addr:\033[00m \033[35m{self.props.mac_addr}\033[00m\n"
        output += "\n"
        return output
