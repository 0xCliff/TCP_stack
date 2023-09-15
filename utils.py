import random


def make_mac_address() -> str:
    address = ""
    for i in range(6):
        byte_1 = hex(random.randint(0, 15))[2:].upper()
        byte_2 = hex(random.randint(0, 15))[2:].upper()
        address += f"{byte_1}{byte_2}"
        if i < 5:
            address += ":"
    return address
