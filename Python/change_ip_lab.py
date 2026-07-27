# change_ip_labview.py
import sys
import subprocess

def change_ip(interface_name, new_ip, subnet_mask, gateway):
    try:
        subprocess.run([
            "netsh", "interface", "ip", "set", "address",
            f"name={interface_name}",
            "static", new_ip, subnet_mask, gateway
        ], check=True)
        return f"✅ IP address changed to {new_ip} successfully."
    except subprocess.CalledProcessError as e:
        return f"❌ Failed to change IP. Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("❗ Usage: python change_ip_labview.py <interface_name> <new_ip> <subnet_mask> <gateway>")
        sys.exit(1)

    interface_name = sys.argv[1]
    new_ip = sys.argv[2]
    subnet_mask = sys.argv[3]
    gateway = sys.argv[4]

    result = change_ip(interface_name, new_ip, subnet_mask, gateway)
    print(result)
