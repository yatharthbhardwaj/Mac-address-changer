import random
import subprocess


def generate_mac_address():
    return '00:' + ':'.join(f'{random.randint(0, 255):02x}' for _ in range(5))


def change_mac_address(device, new_mac):
    try:
        subprocess.run(["ifconfig", device, "down"], check=True)
        subprocess.run(["ifconfig", device, "hw", "ether", new_mac], check=True)
        subprocess.run(["ifconfig", device, "up"], check=True)
        print(f"Successfully changed the MAC address for {device} to {new_mac}")
    except subprocess.CalledProcessError as cpe:
        print(f"Command Error: {cpe}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    device = input(
        "Please enter the device's name you want to change the MAC address for (e.g., eth0, wlan0): ").strip()

    random_mac = input("Do you want a random MAC address? (yes/no): ").strip().lower() == 'yes'
    if random_mac:
        new_mac = generate_mac_address()
    else:
        new_mac = input("Please enter the new MAC address: ").strip()

    change_mac_address(device, new_mac)


if __name__ == "__main__":
    main()
