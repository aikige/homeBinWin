#!/usr/bin/env python
import time
import os
import sys

os.system('cls' if os.name == 'nt' else 'clear')
try:
    while True:
        # Clear the terminal screen
        #os.system('cls' if os.name == 'nt' else 'clear')
        
        # Get current time
        current_time = time.strftime('%Y-%m-%d %H:%M:%S %a')
        
        # Print current time
        sys.stdout.write(f"\rCurrent Time: {current_time}")
        sys.stdout.flush()
        
        # Wait for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
