import psutil
import platform
import datetime

def get_system_info():
    """
    Retrieves and displays detailed system information.
    """
    print("=" * 40 + " System Information " + "=" * 40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    print(f"Python version: {platform.python_version()}")
    print("=" * 40 + " CPU Info " + "=" * 40)
    print(f"Physical cores: {psutil.cpu_count(logical=False)}")
    print(f"Total cores: {psutil.cpu_count(logical=True)}")
    print(f"CPU Frequency: {psutil.cpu_freq().max:.2f}Mhz")
    print(f"CPU Usage: {psutil.cpu_percent()}%")
    print("=" * 40 + " Memory Info " + "=" * 40)
    svmem = psutil.virtual_memory()
    print(f"Total: {svmem.total / (1024**3):.2f} GB")
    print(f"Available: {svmem.available / (1024**3):.2f} GB")
    print(f"Used: {svmem.used / (1024**3):.2f} GB")
    print(f"Percentage: {svmem.percent}%")
    print("=" * 40 + " Disk Info " + "=" * 40)
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {partition_usage.total / (1024**3):.2f} GB")
        print(f"  Used Size: {partition_usage.used / (1024**3):.2f} GB")
        print(f"  Free Size: {partition_usage.free / (1024**3):.2f} GB")
        print(f"  Percentage: {partition_usage.percent}%")
    print("=" * 40 + " Network Info " + "=" * 40)
    ifaces = psutil.net_if_addrs()
    for interface_name, interface_addresses in ifaces.items():
        for address in interface_addresses:
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"=== Interface: {interface_name} ===")
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
    print("=" * 40 + " Boot Time " + "=" * 40)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

if __name__ == "__main__":
    get_system_info()