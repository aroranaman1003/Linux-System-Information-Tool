import threading

def mutex_demo():
    counter = [0]
    lock = threading.Lock()

    def worker():
        for _ in range(10000):
            with lock:
                counter[0] += 1

    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads: t.start()
    for t in threads: t.join()

    print("Mutex Synchronization")
    print("Expected: 40000")
    print("Actual:", counter[0])


def semaphore_demo():
    semaphore = threading.Semaphore(2)

    def worker(i):
        with semaphore:
            print("Thread", i, "entered critical section")
            import time
            time.sleep(1)
            print("Thread", i, "exited critical section")

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(1, 6)]
    for t in threads: t.start()
    for t in threads: t.join()


def peterson_demo():
    flag = [False, False]
    turn = [0]
    counter = [0]

    def worker(i):
        other = 1 - i
        for _ in range(1000):
            flag[i] = True
            turn[0] = other
            while flag[other] and turn[0] == other:
                pass
            counter[0] += 1
            flag[i] = False

    threads = [threading.Thread(target=worker, args=(i,)) for i in range(2)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("Peterson's Solution (demonstration)")
    print("Counter:", counter[0])


def synchronization_menu():
    print("\n1. Mutex")
    print("2. Semaphore")
    print("3. Peterson's Solution")
    c = input("Choice: ")
    if c == "1": mutex_demo()
    elif c == "2": semaphore_demo()
    elif c == "3": peterson_demo()
    else: print("Invalid choice")
