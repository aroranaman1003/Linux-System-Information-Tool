def bankers_algorithm():
    print("\n--- BANKER'S DEADLOCK AVOIDANCE ---")
    n = int(input("Number of processes: "))
    m = int(input("Number of resource types: "))

    allocation = []
    maximum = []

    print("Enter allocation matrix:")
    for i in range(n):
        allocation.append(list(map(int, input(f"P{i}: ").split())))

    print("Enter maximum demand matrix:")
    for i in range(n):
        maximum.append(list(map(int, input(f"P{i}: ").split())))

    available = list(map(int, input("Available resources: ").split()))

    if (len(available) != m or any(len(x) != m for x in allocation)
            or any(len(x) != m for x in maximum)):
        print("Invalid matrix dimensions")
        return

    need = [[maximum[i][j] - allocation[i][j] for j in range(m)]
            for i in range(n)]

    if any(x < 0 for row in need for x in row):
        print("Invalid input: allocation exceeds maximum")
        return

    work = available[:]
    finish = [False] * n
    sequence = []

    while len(sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                work = [work[j] + allocation[i][j] for j in range(m)]
                finish[i] = True
                sequence.append(i)
                found = True
        if not found:
            break

    if all(finish):
        print("System is in SAFE state.")
        print("Safe sequence:", " -> ".join("P"+str(i) for i in sequence))
    else:
        print("System is in UNSAFE state.")
        print("No safe sequence found.")


def deadlock_menu():
    print("1. Banker's Safety Algorithm")
    c = input("Choice: ")
    if c == "1":
        bankers_algorithm()
    else:
        print("Invalid choice")
