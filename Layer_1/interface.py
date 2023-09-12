from .node import Node
from .network_properties import NetworkProperties


class Interface:
    interface_name: str
    from_node: Node
    to_node: Node
    cost: int
    props: NetworkProperties

    def __init__(self, name: str) -> None:
        self.interface_name = name
