def paging_demo():
    print("\n--- PAGING AND ADDRESS TRANSLATION ---")
    page_size = int(input("Page size: "))
    if page_size <= 0:
        print("Page size must be positive")
        return
    address = int(input("Logical address: "))
    if address < 0:
        print("Address must be non-negative")
        return

    page = address // page_size
    offset = address % page_size
    print("Page Number:", page)
    print("Offset:", offset)

    frame = int(input("Enter frame number for this page: "))
    if frame < 0:
        print("Invalid frame")
        return
    print("Physical Address:", frame * page_size + offset)


def page_replacement():
    print("\n--- PAGE REPLACEMENT ---")
    pages = list(map(int, input("Page reference string: ").split()))
    capacity = int(input("Number of frames: "))
    if capacity <= 0:
        print("Frame capacity must be positive")
        return

    frames = []
    faults = 0
    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) == capacity:
                frames.pop(0)
            frames.append(page)
        print(page, "=>", frames)

    print("FIFO Page Faults:", faults)


def memory_menu():
    print("\n1. Paging and Address Translation")
    print("2. FIFO Page Replacement")
    c = input("Choice: ")
    if c == "1": paging_demo()
    elif c == "2": page_replacement()
    else: print("Invalid choice")
