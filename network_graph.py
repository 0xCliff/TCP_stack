from device import Device
from interface import Interface
from link import Link


class NetworkGraph:
    name: str
    device_list: list["Device"]
    device_count: int

    def __init__(self, name) -> None:
        self.name = name
        self.device_count = 0
        self.device_list = list()

    def add_device(self, name: str, ip: str, mac: str, subnet: int) -> "Device":
        new_device = Device(name, ip, mac, subnet)
        self.device_list.append(new_device)
        return new_device

    def add_link_between_devices(
        self,
        from_device: "Device",
        to_device: "Device",
        from_interface_name: str,
        to_interface_name: str,
        cost: int,
    ) -> None:
        from_interface = Interface(from_interface_name)
        from_interface.attached_device = from_device
        from_link = Link("Ethernet", from_device, to_device, 1)
        from_interface.connection = from_link
        from_device.ports.append(from_interface)

        to_interface = Interface(to_interface_name)
        to_interface.attached_device = to_device
        to_link = Link("Ethernet", to_device, from_device, 1)
        to_interface.connection = to_link
        to_device.ports.append(to_interface)

    def get_connected_devices(self, device: "Device") -> list["Device"]:
        connected_devices: list["Device"] = list()
        for interface in device.ports:
            connected_devices.append(interface.connection.to_device)
        return connected_devices

    def __repr__(self) -> str:
        output = ""
        for device in self.device_list:
            output += repr(device)
        return output
