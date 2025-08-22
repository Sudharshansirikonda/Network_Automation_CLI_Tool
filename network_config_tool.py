# network_config_tool.py
import logging
import getpass
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

def get_credentials():
    """Securely prompts the user for their username and password."""
    username = input("Enter your SSH username: ")
    password = getpass.getpass() # Hides password input
    return username, password

def get_device_info():
    """Prompts the user for device connection details."""
    host = input("Enter the device IP address or hostname: ")
    device_type = input("Enter the device type (e.g., cisco_ios, arista_eos): ")
    return {
        'device_type': device_type,
        'host': host,
    }

def get_commands_from_file(filename="commands.txt"):
    """Reads a list of commands from a specified file."""
    try:
        with open(filename, 'r') as f:
            commands = [line.strip() for line in f if line.strip()]
        print(f"--- Successfully loaded {len(commands)} commands from '{filename}' ---")
        return commands
    except FileNotFoundError:
        print(f"[ERROR] The command file '{filename}' was not found.")
        print("Please create this file and add one command per line.")
        return None

def main():
    """
    Main function to connect to a network device and apply configurations.
    """
    logging.basicConfig(filename='netmiko_debug.log', level=logging.DEBUG)
    # 1. Gather all necessary information
    device = get_device_info()
    username, password = get_credentials()
    device['username'] = username
    device['password'] = password
    
    commands_to_send = get_commands_from_file()

    if not commands_to_send:
        return # Exit if no commands were loaded

    print(f"\nAttempting to connect to {device['host']}...")

    # 2. Establish SSH connection and execute commands
    try:
        with ConnectHandler(**device) as net_connect:
            # Use send_config_set for configuration commands.
            # This method automatically enters and exits configuration mode.
            print("--- Connection established. Sending configuration commands... ---")
            output = net_connect.send_config_set(commands_to_send)
            
            print("\n--- Configuration applied successfully. Device output: ---")
            print(output)

            # Optional: Save the running configuration
            save_choice = input("\nDo you want to save the configuration? (yes/no): ").lower()
            if save_choice == 'yes':
                print("--- Saving configuration... ---")
                save_output = net_connect.save_config()
                print(save_output)
                print("--- Configuration saved. ---")

    # 3. Handle potential errors
    except NetmikoAuthenticationException:
        print("\n[FATAL ERROR] Authentication failed. Please check your username and password.")
    except NetmikoTimeoutException:
        print(f"\n[FATAL ERROR] Connection timed out. The device at {device['host']} is not reachable.")
    except Exception as e:
        print(f"\n[FATAL ERROR] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
