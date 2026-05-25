#import system monitoring library 
import psutil
#import built-in time library
import time

print("Starting Live Monitoring System... Press Ctrl+C to stop.")
print("========================================================")

#LOOP: tells Pythn to repeat the code inside forever
while True:
#Check current CPU utilization percentage
#'interval=1' means it samples CPU usage over 1 second
    cpu_usage = psutil.cpu_percent(interval=1)

# Check Virtual Memory (RAM) statistics
    ram_info = psutil.virtual_memory()
#Get RAM usage%
    ram_usage = ram_info.percent

#Print live dashboard to screen
    print("=== LIVE SYSTEM METRICS ===")
    print(f"Current CPU Usage: {cpu_usage}%")
    print(f"Current RAM Usage: {ram_usage}%")
    print("========================")

#DevOps Alert Threshold Logic
#If either CPU or RAM crosses 80%, sound the alarm!
    if cpu_usage > 80 or ram_usage > 80:
        print("WARNING!!! : High resource utilization detected on host machine!")
    else:
        print(" System Health: Normal")

    #Pause execution for 4 seconds before running again
    time.sleep(4)