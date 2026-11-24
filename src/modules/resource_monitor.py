import psutil

def show_resources():
    print("\n--- RESOURCE MONITOR ---")
    print("CPU:", psutil.cpu_percent(interval=1), "%")
    print("CPU Cores:", psutil.cpu_count())
    m = psutil.virtual_memory()
    print("Total RAM:", round(m.total/1024**3, 2), "GB")
    print("Used RAM:", round(m.used/1024**3, 2), "GB")
    print("RAM Usage:", m.percent, "%")
    s = psutil.swap_memory()
    print("Swap Used:", round(s.used/1024**3, 2), "GB")
    print("Swap Usage:", s.percent, "%")

