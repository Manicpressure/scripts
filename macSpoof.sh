#!/bin/bash

# Find your mac address and enter the first half in block1 and second half in block2
block1="12:34:56"
block2="78:91:01"
random1=$(printf "%02x" $(( $RANDOM % 256 )))
random2=$(printf "%02x" $(( $RANDOM % 256 )))
random3=$(printf "%02x" $(( $RANDOM % 256 )))

# Find your network device and enter it below
NIC="wlan0"

if [[ $1 == --* ]]; then
	echo "flag"
else
	NIC=$1
	echo "$NIC=$1"
	shift
fi

case $1 in
	--change)
		ip link set dev $NIC down
		echo "interface down"
		spoof="$block1:$random1:$random2:$random3"
		echo "spoofing to address $spoof"
		ip link set dev $NIC address $spoof
		ip link set dev $NIC up
		echo "MAC addy spoofed"
		;;
	--reset)
		ip link set dev $NIC down
		echo "interface down"
		ip link set dev $NIC address "$block1:$block2"
		ip link set dev $NIC up
		echo "Resetting MAC to $block1:$block2"
		;;
esac

