#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#define DISTANCE_PATH "/sys/bus/iio/devices/iio:device0/in_distance_raw"
#define LED_BRIGHTNESS_PATH "/sys/class/leds/ACT/brightness"
#define LED_TRIGGER_PATH "/sys/class/leds/ACT/trigger"
#define BLINK_THRESHOLD 100
#define BLINK_DELAY 100000  // 0.1 seconds in microseconds

// Function to read an integer value from a sysfs file
int read_sysfs_value(const char *path) {
    int value = -1;
    FILE *file = fopen(path, "r");
    if (file) {
        if (fscanf(file, "%d", &value) != 1) {
            perror("Failed to read value");
        }
        fclose(file);
    } else {
        perror("Failed to open file");
    }
    return value;
}

// Function to write a value to a sysfs file
void write_sysfs_value(const char *path, const char *value) {
    int fd = open(path, O_WRONLY);
    if (fd >= 0) {
        write(fd, value, strlen(value));
        close(fd);
    } else {
        perror("Failed to open file for writing");
    }
}

int main() {
    // Disable LED trigger to allow manual control
    write_sysfs_value(LED_TRIGGER_PATH, "none");

    while (1) {
        int distance = read_sysfs_value(DISTANCE_PATH);
        if (distance < 0) {
            fprintf(stderr, "Error reading distance sensor\n");
            break;
        }

        if (distance < BLINK_THRESHOLD) {
            // Blink the LED
            write_sysfs_value(LED_BRIGHTNESS_PATH, "1");
            usleep(BLINK_DELAY);
            write_sysfs_value(LED_BRIGHTNESS_PATH, "0");
            usleep(BLINK_DELAY);
        } else {
            // LED is off if condition isn't met; sleep to avoid lockup
            write_sysfs_value(LED_BRIGHTNESS_PATH, "0");
            usleep(500000);  
        }
    }

    return 0;
}

