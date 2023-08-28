#!/usr/bin/env python3

from ping3 import ping
import time
import os
import argparse

# pingrr.py
# example usage: pingrr.py [--threshold <threshold_ms>] [--target <ping_target>] [-h,--help]
def options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--threshold",
        help="Threshold in milliseconds before a notification is sent. Default is 100ms.",
        type=int,
        default=100,
    )
    parser.add_argument(
        "--target",
        help="Ping target",
        type=str,
        default="google.com",
    )
    return parser.parse_args()

# function to send notification to macos notification center.
# required args: message
# optional args: title, subtitle
def send_notification(title=None, subtitle=None, message=None):
    if title is None:
        title = "Pingrr"
    if subtitle is None:
        print(f"Notification -- {title}: {message}")
        os.system(
            f"""   osascript -e 'display notification "{message}" with title "{title}"'    """
        )
    else:
        print(f"Notification -- {title}: {subtitle}: {message}")
        os.system(
            f"""   osascript -e 'display notification "{message}" with title "{title}" subtitle "{subtitle}"'    """
        )

# Ping google.com every second and print a message if the round trip time is greater than 0.01 seconds
def main(threshold_ms, ping_target):
    send_notification(
        "Pingrr",
        "Starting",
        f"Threshold: {threshold_ms}ms, Ping target: {ping_target}",
    )
    while True:
        # perform the ping
        round_trip_time = ping(ping_target)
        # Convert round trip time to milliseconds and round it down to the nearest integer
        round_trip_time_ms = int(round(round_trip_time * 1000))
        if round_trip_time is None:
            print("Ping failed.")
            # send notification to macos notification center with the round trip time
            send_notification(
                "Pingrr",
                "Ping Failed",
                f"No response from {ping_target}",
            )
            print("Waiting 10 seconds before pinging again...")
            time.sleep(10)  # Wait for 10 seconds before pinging again after sending notification
        elif round_trip_time_ms > threshold_ms:  # Convert 500ms to 0.5s for comparison
            print(f"Round Trip Time: {round_trip_time_ms}ms")
            # send notification to macos notification center with the round trip time
            send_notification(
                "Pingrr",
                "High Latency Detected",
                f"Round Trip Time: {round_trip_time_ms}ms",
            )
            print("Waiting 10 seconds before pinging again...")
            time.sleep(10)  # Wait for 10 seconds before pinging again after sending notification
        else:
            print(f"Round Trip Time: {round_trip_time_ms}ms")
            time.sleep(1)  # Wait for 10 seconds before pinging again after sending notification


opts = options()
main(opts.threshold, opts.target)