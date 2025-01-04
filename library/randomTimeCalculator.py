import random
from datetime import datetime, timedelta
import pytz

def generate_random_time_ist():
    # Define the start and end time as datetime objects (8 AM and 8 PM IST)
    start_time = datetime.strptime("08:00:00", "%H:%M:%S")
    end_time = datetime.strptime("20:00:00", "%H:%M:%S")

    # Calculate the difference (timedelta) between the two times
    delta = end_time - start_time
    
    # Generate a random number of seconds within the time range
    random_seconds = random.randint(0, int(delta.total_seconds()))
    
    # Add the random seconds to the start_time to get the random time
    random_time = start_time + timedelta(seconds=random_seconds)

    # Convert to IST (Indian Standard Time)
    ist = pytz.timezone('Asia/Kolkata')
    random_time_ist = ist.localize(random_time)

    # Convert to GMT (Greenwich Mean Time)
    gmt = pytz.timezone('GMT')
    random_time_gmt = random_time_ist.astimezone(gmt)

    # Format the time in 12-hour format with AM/PM
    formatted_time_ist = random_time_ist.strftime("%I:%M:%S %p")
    formatted_time_gmt = random_time_gmt.strftime("%I:%M:%S %p")

    return formatted_time_ist, formatted_time_gmt

# Generate and print the random times
formatted_time_ist, formatted_time_gmt = generate_random_time_ist()
print(f"Random time in IST: {formatted_time_ist}")
print(f"Random time in GMT: {formatted_time_gmt}")
