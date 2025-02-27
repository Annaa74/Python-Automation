import platform

def get_device_info():
    system_info = platform.uname()
    print("Device Information:")
    print(f"  - System: {system_info.system}")
    print(f"  - Node Name: {system_info.node}")
    print(f"  - Release: {system_info.release}")
    print(f"  - Version: {system_info.version}")
    print(f"  - Machine: {system_info.machine}")
    print(f"  - Processor: {system_info.processor}")

if __name__ == "__main__":
    get_device_info()