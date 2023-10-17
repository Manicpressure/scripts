# IP Address Fetcher

This script is designed to retrieve and display both the public and private IP addresses for a specified network interface controller (NIC) on a machine. It provides IPv4 and IPv6 information, where available.

I recommend you download it to /usr/local/bin for easy access through terminal.

## Usage
### Setup:
Open the script in your preferred text editor.
Locate the line NIC=**CHANGEME**.
Replace **CHANGEME** with the desired NIC name (e.g., eth0 for an Ethernet connection or wlan0 for a wireless connection).

Execute the Script:
Make the script executable, if not already.
`chmod +x ipInfo`

Run the script to see your ip address
`ipInfo`

### Output
The script provides the following output:

    Public IPv4 address.
    Private IPv4 address for the specified NIC.
    Private IPv6 address for the specified NIC.

If any IP information is not available, "Disconnected" will be displayed.

## Dependencies
curl: Used for fetching the public IP.
ip: Used for checking NIC existence and fetching private IPs.

Make sure you have these utilities installed on your machine.

## Notes
Ensure that the NIC name you enter in the script exists on your machine. The script will exit if the specified NIC is not found.
If your machine doesn't have a connection to the internet, the script will show "Disconnected" for the public IP.
