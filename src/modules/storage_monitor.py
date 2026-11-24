import psutil

def show_storage():
    print("\n--- STORAGE MONITOR ---")
    for p in psutil.disk_partitions():
        try:
            d = psutil.disk_usage(p.mountpoint)
            print(p.mountpoint, "| Total:", round(d.total/1024**3,2),
                  "GB | Used:", d.percent, "%")
        except (PermissionError, OSError):
            pass

