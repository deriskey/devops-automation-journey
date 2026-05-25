import os
import platform #detects underlying OS

#create a list of IP addresses to monitor.
#(We will use Google DNS, Cloudflare DNS, and a fake local IP for testing)
devices_to_ping = [
    "8.8.8.8",
    "1.1.1.1",
    "192.168.254.254"
]

print("==STARTING DOSM NETWORK REACHABILITY SCAN ===")
print("=============================================")

#Determine corect flag based on OS
current_os = platform.system().lower()
if current_os == "windows":
    ping_flag = "-n 1"
else:
    ping_flag = "-c 1" #Linux/Alpine
#loop throught each target IP address in our tracking list
for ip in devices_to_ping:

    #Build native ping commanf string for Windows systems
    #'-n 1' tells Windows to send exactly 1 ping packet instead of 4 (save time)
    #3'>null' hides messy raw command line output from clutteting your screen
    ping_command = f"ping {ping_flag} {ip} > /dev/null 2>&1" if current_os != "windows" else f"ping{ping_flag} {ip} > nul"

    #Execute comman on system
    #os.system returns 0 if command succeeds (ping replies!)
    response = os.system(ping_command)

    #Conditional response logic to evaluate the network status
    if response == 0:
        print(f"Host {ip} is UP and reachable.")
    else:
        print(f" ALERT: Host {ip} is DOWN or unreacheable")

print("=======================================")
print("Scan routine complete")