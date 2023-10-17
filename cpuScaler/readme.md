# CPU Governor Toggle Script

This script provides functionality to toggle the CPU governor between performance and powersave modes. 

This script is for use on Acer Aspire 3 with Arch linux installation. 
This computer has two power modes: 'performance' and 'powersave'. If your computer has other powermodes, they will need to be added into the script. I have not made any adjustments for other power modes. 
To find out what power modes you have on your computer, make sure you have the package `linux-tools` installed.

`pacman -Q linux-tools`
`pacman -S linux-tools`

If you have it, type the following into your terminal to find out what modes you have available on your system

`cpupower frequency-info --governors`

I recommend you download it to `/usr/local/bin` for easy access.

- This script was originally for use on waybar. I wanted to be able to switch power modes by clicking on the icon. I haven't been able to get this working due to sudo permissions being required. However, the icon should indicate what power mode you are in so you can change it yourself manually.

- Not a great solution I know :(

## Features:
Fetch the current CPU governor mode.
Toggle between performance and powersave modes.

## Prerequisites:

linux-tools: Required for the cpupower command. Install via:
`sudo pacman -S linux-tools`

## Usage: Run the following commands in your linux terminal
To fetch the current governor mode, run:
`/usr/local/bin/cpuScale`

To toggle the governor mode, run:
`cpueScale toggle`

## Waybar Integration:

To add this script to Waybar, update your Waybar configuration (config file) by adding the following module:

```
"custom/governor": {
    "format": "{}",
    "exec": "/usr/local/bin/cpuGovernor.sh",
    "on-click": "/usr/local/bin/cpuGovernor.sh toggle",
    "tooltip": "cpupower frequency-set -g $current_governor"
}
```

Once added, this will display the current governor mode on your Waybar. Clicking the display should toggle the governor mode - but as of yet I have not been able to find a way to get this working.

### Icons:

    ⚡P: Indicates performance mode.
    🍃E: Indicates powersave mode.
    ❓: Indicates an unknown mode.

## Note:
Ensure that the script /usr/local/bin/cpuScale has the necessary permissions to be executed. You can provide execute permissions using:

`chmod +x /usr/local/bin/cpuScale`


