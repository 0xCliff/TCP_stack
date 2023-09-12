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
        output = f"{self.node_name}: {self.props.ip_addr}/{self.props.subnet_mask}, {self.props.mac_addr} \n"
        for intf in self.interfaces:
            output += f"Interface: {intf.interface_name} connected to {intf.to_node.node_name}, Weight: {intf.cost}\n"
        output += "\n"
        return output
