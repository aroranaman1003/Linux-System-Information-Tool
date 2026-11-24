import platform, socket, getpass, os

def show_system_info():
    print("\n--- SYSTEM INFORMATION ---")
    print("User:", getpass.getuser())
    print("Hostname:", socket.gethostname())
    print("OS:", platform.system())
    print("Kernel:", platform.release())
    print("Architecture:", platform.machine())
    print("Python:", platform.python_version())
    print("Working Directory:", os.getcwd())
