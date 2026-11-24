import psutil

def health_check():
    print("\n--- SYSTEM HEALTH CHECK ---")
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    print("CPU:", cpu, "%")
    print("RAM:", ram, "%")
    print("Disk:", disk, "%")
    if cpu > 80: print("WARNING: High CPU usage")
    if ram > 85: print("WARNING: High RAM usage")
    if disk > 90: print("WARNING: Low disk space")
    if cpu <= 80 and ram <= 85 and disk <= 90:
        print("System operating normally")
