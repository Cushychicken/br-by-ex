#!/bin/sh
### BEGIN INIT INFO
# Provides:          distance_led
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Controls LED based on distance sensor
# Description:       Starts a Python script to monitor distance and control LED via sysfs
### END INIT INFO

DAEMON=/usr/bin/python3
SCRIPT_PATH=/home/closeblink/closeblink.py
PIDFILE=/var/run/closeblink.pid

start() {
    echo "Starting distance LED service..."
    start-stop-daemon --start --background --make-pidfile --pidfile $PIDFILE --exec $DAEMON -- $SCRIPT_PATH
}

stop() {
    echo "Stopping distance LED service..."
    start-stop-daemon --stop --pidfile $PIDFILE
    rm -f $PIDFILE
}

restart() {
    stop
    sleep 1
    start
}

case "$1" in
    start) start ;;
    stop) stop ;;
    restart) restart ;;
    *) echo "Usage: $0 {start|stop|restart}"; exit 1 ;;
esac

exit 0

