import threading
import time

def worker(name):
    for i in range(3):
        print(name, "working:", i+1)
        time.sleep(0.2)

def thread_demo():
    print("\n--- THREAD MANAGEMENT ---")
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker, args=(f"Thread-{i+1}",))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("All threads completed.")
