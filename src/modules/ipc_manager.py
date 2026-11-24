from multiprocessing import Pipe

def pipe_demo():
    print("\n--- IPC USING PIPE ---")
    parent, child = Pipe()
    message = "Hello from Process 1"
    parent.send(message)
    print("Process 1 sent:", message)
    received = child.recv()
    print("Process 2 received:", received)
    parent.close()
    child.close()


def ipc_menu():
    print("1. Pipe Communication")
    c = input("Choice: ")
    if c == "1": pipe_demo()
    else: print("Invalid choice")
