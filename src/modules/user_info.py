import getpass, os, psutil

def show_users():
    print("\n--- USER INFORMATION ---")
    print("Current User:", getpass.getuser())
    print("Home:", os.path.expanduser("~"))
    print("UID:", os.getuid() if hasattr(os, "getuid") else "N/A")
    for user in psutil.users():
        print("Logged in:", user.name, user.terminal)

