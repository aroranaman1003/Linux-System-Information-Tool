def calculate(processes, algorithm, quantum=2):
    # Each process: [PID, Arrival Time, Burst Time, Priority]
    n = len(processes)
    remaining = {p[0]: p[2] for p in processes}
    arrival = {p[0]: p[1] for p in processes}
    burst = {p[0]: p[2] for p in processes}
    priority = {p[0]: p[3] for p in processes}
    completion = {}
    gantt = []
    time = 0

    if algorithm == "FCFS":
        order = sorted(processes, key=lambda p: p[1])
        for p in order:
            pid, at, bt, pr = p
            time = max(time, at)
            start = time
            time += bt
            completion[pid] = time
            gantt.append((pid, start, time))

    elif algorithm in ("SJF", "PRIORITY"):
        done = set()
        while len(done) < n:
            ready = [p for p in processes
                     if p[1] <= time and p[0] not in done]
            if not ready:
                time += 1
                continue
            if algorithm == "SJF":
                p = min(ready, key=lambda x: x[2])
            else:
                p = min(ready, key=lambda x: x[3])
            pid, at, bt, pr = p
            start = time
            time += bt
            completion[pid] = time
            done.add(pid)
            gantt.append((pid, start, time))

    elif algorithm == "SRTF":
        while len(completion) < n:
            ready = [p for p in processes
                     if p[1] <= time and remaining[p[0]] > 0]
            if not ready:
                time += 1
                continue
            p = min(ready, key=lambda x: remaining[x[0]])
            pid = p[0]
            if not gantt or gantt[-1][0] != pid:
                gantt.append([pid, time, time + 1])
            else:
                gantt[-1][2] += 1
            remaining[pid] -= 1
            time += 1
            if remaining[pid] == 0:
                completion[pid] = time

    elif algorithm == "RR":
        queue = []
        added = set()
        while len(completion) < n:
            for p in sorted(processes, key=lambda x: x[1]):
                if p[1] <= time and p[0] not in added:
                    queue.append(p[0])
                    added.add(p[0])
            if not queue:
                time += 1
                continue
            pid = queue.pop(0)
            start = time
            run = min(quantum, remaining[pid])
            time += run
            remaining[pid] -= run
            gantt.append((pid, start, time))
            if remaining[pid] == 0:
                completion[pid] = time
            else:
                for p in sorted(processes, key=lambda x: x[1]):
                    if p[1] <= time and p[0] not in added:
                        queue.append(p[0])
                        added.add(p[0])
                queue.append(pid)

    print("\n--- GANTT CHART ---")
    for pid, start, end in gantt:
        print(f"| P{pid} ({start}-{end}) ", end="")
    print("|")

    total_wt = total_tat = 0
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        pid, at, bt, pr = p
        tat = completion[pid] - at
        wt = tat - bt
        total_tat += tat
        total_wt += wt
        print(f"P{pid}\t{at}\t{bt}\t{completion[pid]}\t{tat}\t{wt}")

    print("Average Waiting Time:", round(total_wt/n, 2))
    print("Average Turnaround Time:", round(total_tat/n, 2))


def cpu_scheduler():
    print("\n--- CPU SCHEDULING SIMULATOR ---")
    print("1. FCFS")
    print("2. SJF (Non-preemptive)")
    print("3. SRTF")
    print("4. Priority (Non-preemptive, lower number = higher priority)")
    print("5. Round Robin")
    choice = input("Choose algorithm: ")
    algorithms = {"1":"FCFS", "2":"SJF", "3":"SRTF",
                  "4":"PRIORITY", "5":"RR"}
    if choice not in algorithms:
        print("Invalid choice")
        return

    n = int(input("Number of processes: "))
    processes = []
    for i in range(n):
        print(f"\nProcess P{i+1}")
        at = int(input("Arrival time: "))
        bt = int(input("Burst time: "))
        pr = int(input("Priority (enter 0 if unused): "))
        if bt <= 0 or at < 0:
            print("Invalid process values")
            return
        processes.append([i+1, at, bt, pr])

    q = 2
    if choice == "5":
        q = int(input("Time quantum: "))
        if q <= 0:
            print("Quantum must be positive")
            return

    calculate(processes, algorithms[choice], q)


def advanced_scheduling():
    print("\n--- MULTILEVEL QUEUE / FEEDBACK QUEUE ---")
    print("MLQ and MLFQ are planned for the next implementation.")
