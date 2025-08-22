Network Automation CLI Tool
This project is a command-line interface (CLI) tool built with Python to automate the configuration of network devices such as routers and switches. It uses the powerful netmiko library to establish SSH connections and execute a series of commands read from an external file.

This tool is designed to save time, reduce human error, and make repetitive network configuration tasks efficient and reliable.

Features
CLI-Based: A lightweight and fast tool that runs entirely in the terminal with no graphical user interface.

Multi-Vendor Support: Leverages netmiko to support a wide range of network devices (e.g., Cisco IOS, Arista EOS, Juniper Junos).

External Command File: Reads configuration commands from a simple commands.txt file, making it easy to manage and reuse different configuration scripts.

Secure Credential Input: Uses Python's getpass module to securely prompt for passwords without displaying them on screen.

Detailed Logging: Includes built-in logging to provide step-by-step feedback and simplify the debugging process.

How It Works
The script prompts the user for four key pieces of information:

Device IP Address / Hostname

Device Type (e.g., cisco_ios)

SSH Username

SSH Password

Once the information is provided, the script reads the commands from the commands.txt file, establishes an SSH connection to the target device, executes the commands in configuration mode, and prints the device's output directly to the terminal.

Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x

Netmiko: A multi-vendor library to simplify SSH connections to network devices.

Setup & Usage
Follow these steps to get the project running:

1. Clone the Repository
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

2. Install Dependencies
Install the required netmiko library using pip:

pip install netmiko

3. Create the Commands File
In the project's root directory, create a file named commands.txt. This is where you will list the configuration commands you want to execute. Each command must be on a new line.

Example commands.txt:

interface GigabitEthernet0/1
 description Configured_by_Python_Automation_Tool
 ip address 10.10.30.5 255.255.255.0
 no shutdown

4. Run the Script
Execute the main script from your terminal:

python network_config_tool.py

The script will then guide you through the prompts for the device IP, type, and your credentials. After you provide the inputs, it will connect to the device and apply the configuration.
