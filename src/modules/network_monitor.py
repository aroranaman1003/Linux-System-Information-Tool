import psutil, socket

def show_network():
    print("\n--- NETWORK MONITOR ---")
    for interface, addresses in psutil.net_if_addrs().items():
        print("\nInterface:", interface)
        for a in addresses:
            if a.family == socket.AF_INET:
                print("IPv4:", a.address)
    stats = psutil.net_io_counters()
    print("\nBytes Sent:", stats.bytes_sent)
    print("Bytes Received:", stats.bytes_recv)

def show_connections():
    print("\n--- NETWORK CONNECTIONS ---")
    try:
        for c in psutil.net_connections(kind='inet')[:20]:
            print("PID:", c.pid, "Local:", c.laddr,
                  "Remote:", c.raddr, "Status:", c.status)
    except psutil.AccessDenied:
        print("Permission denied. Run with appropriate privileges.")

