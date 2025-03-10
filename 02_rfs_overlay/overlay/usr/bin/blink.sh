#!/bin/sh

# Path to green LED's device under /sys/
LED_PATH="/sys/class/leds/ACT"

# Test for device existence
if [ ! -d "$LED_PATH" ]; then
    echo "Error: LED path not found ($LED_PATH). Exiting."
    exit 1
fi

# Disable default behavior
echo "none" > "$LED_PATH/trigger"

# Blink loop
while true; do
    echo 1 > "$LED_PATH/brightness"
    sleep 1
    echo 0 > "$LED_PATH/brightness"
    sleep 1
done
