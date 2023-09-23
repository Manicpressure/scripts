#!/bin/bash

# Destination directory for snapshots, root subvolume, home subvolume
snapDir="/.snapshots"
rootSV="root_$(date +%Y-%m-%d_%H:%M:%S)"
homeSV="home_$(date +%Y-%m-%d_%H:%M:%S)"

# Create snapshot
sudo btrfs subvolume snapshot / $snapDir/$rootSV
sudo btrfs subvolume snapshot /home $snapDir/$homeSV

echo "Snapshots taken successfully"
