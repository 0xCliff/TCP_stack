from network_properties import NetworkProperties
from link import Link
from functools import total_ordering
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from device import Device


@total_ordering
class Interface:
    name: str
    connection: "Link"
    attached_device: "Device"
    network_properties: "NetworkProperties"

    def __init__(self, name: str) -> None:
        self.name = name

    def _is_valid_operand(self, other: "Interface") -> bool:
        return hasattr(other, "name")

    def __lt__(self, other: "Interface") -> bool | ValueError:
        if not self._is_valid_operand(other):
            return ValueError()
        return self.name.lower() < other.name.lower()

    def __repr__(self) -> str:
        return f"\t\033[36mInterface Name:\033[00m {self.name} \033[36mTo Device:\033[00m {self.connection.to_device.name} \033[36mvia\033[00m {self.connection.type}\033[00m \033[36mwith Cost:\033[00m {self.connection.cost}\n"
