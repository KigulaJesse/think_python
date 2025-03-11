"""Converts GMT to Hours, minutes, seconds"""
import time

def convert_time():
    "time"
    # Get current time since the epoch
    current_time = time.time()

    # Calculate days since epoch
    days = int(current_time // 86400)  # 86400 seconds in a day
    seconds_remaining = int(current_time % 86400)
    hours = seconds_remaining // 3600
    seconds_remaining = seconds_remaining % 3600
    minutes = seconds_remaining // 60
    seconds = seconds_remaining % 60

    # Display results
    print("1")
    print(f"Current time: {hours:02d}:{minutes:02d}:{seconds:02d}")
    print(f"Days since epoch: {days}")

    # Convert to hours, minutes, and seconds
    local_time = time.localtime(current_time)
    hours = local_time.tm_hour
    minutes = local_time.tm_min
    seconds = local_time.tm_sec

    print("")
    print("2")
    # Display results
    print(f"Current time: {hours:02d}:{minutes:02d}:{seconds:02d}")
    print(f"Days since epoch: {days}")

# Run the function
convert_time()
