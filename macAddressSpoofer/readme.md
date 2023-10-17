# MAC Address Spoofer
This script allows users to spoof their MAC address to a randomly generated one or reset it to its original value.

## Dependencies
Linux: This script uses Linux commands and utilities, hence it is intended for Linux environments.

## Configuration
Before running the script, please configure the following values inside the script:

MAC Address: Replace block1 and block2 with the two halves of your actual MAC address.
block1 represents your device manufacturer. If this block doesn't match your actual device manufacturer, and the fingerprinting entity is able to see this, it becomes clear that you are spoofing your MAC address.

block2 is the numbers you can change with less suspicion.

```
block1="12:34:56"
block2="78:91:01"
```

To find out your mac address simply type in the following into your terminal and identify which NIC your computer is using. The MAC address will be apparent.
`ip a`

Network Interface Device: By default, the script uses wlan0 as the network interface card (NIC). Replace it if you use a different one. Then you will not need to type in your NIC when executing this script.

`NIC="wlan0"`

## Usage
Spoof MAC Address:

`macSpoof.sh [NIC] --change`
If you don't specify a NIC, it will use the default wlan0.

Reset MAC Address to Original:
`macSpoof.sh [NIC] --reset`

## How it Works
The script either spoofs or resets the MAC address of the specified NIC.
For spoofing, it uses the first half of your MAC address and then randomly generates the second half.
For resetting, it uses the entire MAC address you provided.

## Notes
Ensure you have the required permissions to change your MAC address. You might need to run this script with sudo to get elevated privileges.
