import platform
import subprocess


devices = [
    "127.0.0.1",
    "192.168.1.1",
    "192.168.1.10"
]


def ping_device(ip):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", parameter, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


for device in devices:
    if ping_device(device):
        print(f"{device} - UP")
    else:
        print(f"{device} - DOWN")