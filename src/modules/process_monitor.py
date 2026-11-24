import psutil

def show_processes():
    print("\n--- PROCESS MONITOR ---")
    processes = []
    for p in psutil.process_iter(['pid','name','status','memory_percent']):
        try:
            processes.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    print("Total processes:", len(processes))
    for p in processes[:20]:
        print(p)

def search_process():
    name = input("Process name: ").lower()
    for p in psutil.process_iter(['pid','name','status']):
        try:
            if name in (p.info['name'] or '').lower():
                print(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

