from .node import Node
from .interface import Interface


class NetworkGraph:
    topology_name: str
    node_list: list[Node]
    num_nodes: int

    def __init__(self, name) -> None:
        self.topology_name = name
        self.num_nodes = 0
        self.node_list = list()

    def add_node(self, name: str, ip: str, mac: str, subnet: int) -> Node:
        new_node = Node(name, ip, mac, subnet)
        self.node_list.append(new_node)
        return new_node

    def add_link_between_nodes(
        self,
        from_node: Node,
        to_node: Node,
        intf_1: str,
        intf_2: str,
        weight: int,
    ) -> None:
        interface_1 = Interface(intf_1)
        interface_2 = Interface(intf_2)

        interface_1.from_node = from_node
        interface_1.to_node = to_node
        interface_1.cost = weight

        interface_2.from_node = to_node
        interface_2.to_node = from_node
        interface_2.cost = weight

        from_node.interfaces.append(interface_1)
        to_node.interfaces.append(interface_2)

    def get_neighbour_node(self, node: Node):
        pass

    def __repr__(self) -> str:
        output = ""
        for node in self.node_list:
            output += repr(node)
        return output
