from flask import Flask, jsonify, render_template
import time

DISTANCE_PATH = "/sys/bus/iio/devices/iio:device0/in_distance_raw"
LED_BRIGHTNESS_PATH = "/sys/class/leds/ACT/brightness"
LED_TRIGGER_PATH = "/sys/class/leds/ACT/trigger"
BLINK_THRESHOLD = 100
BLINK_DELAY = 0.05  # 0.05 seconds

app = Flask(__name__)


def read_sysfs_value(path):
    try:
        with open(path) as file:
            return int(file.read().strip())
    except (OSError, ValueError) as e:
        print(f"Error reading {path}: {e}")
        return -1


def write_sysfs_value(path, value):
    try:
        with open(path, "w") as file:
            file.write(value)
    except OSError as e:
        print(f"Error writing to {path}: {e}")


def blink_led():
    write_sysfs_value(LED_BRIGHTNESS_PATH, "1")
    time.sleep(BLINK_DELAY)
    write_sysfs_value(LED_BRIGHTNESS_PATH, "0")
    time.sleep(BLINK_DELAY)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/distance")
def get_distance():
    distance = read_sysfs_value(DISTANCE_PATH)
    return jsonify({"distance": distance})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
