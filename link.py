from device import Device


class Link:
    type: str
    from_device: "Device"
    to_device: "Device"
    cost: int

    def __init__(self, type: str, from_: "Device", to: "Device", cost: int):
        self.type = type
        self.from_device = from_
        self.to_device = to
        self.cost = cost
