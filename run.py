import script
import time
import sys
from multiprocessing import Process

processes = int(input("Enter amount of instances (recommended: 75-200): "))
json_payload = input("Enter the JSON payload (no outer quoutation marks): ")

print("\033[96m[*] Config Applied")
print("\033[96m[*] To stop, press enter")
time.sleep(1)
print("\033[95m[*] Starting in 5 seconds")
time.sleep(5)
threads = []
for x in range(processes):
    a = Process(target=script.main, args=(json_payload, x))
    a.start()
    threads.append(a)

stopData = input("#> \n")

print("\033[93m[*] Exiting...")
for x in threads:
    x.terminate()
print("\033[93m[*] Exit Code 0: Bye!")
sys.exit(0)
