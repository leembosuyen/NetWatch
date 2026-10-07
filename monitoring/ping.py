import platform
import subprocess


def ping_device(ip):
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    result = subprocess.run(
        ["ping", parameter, "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0

ip = input("Enter IP address: ")

if ping_device(ip):
    print(f"{ip} is UP")
else:
    print(f"{ip} is DOWN")