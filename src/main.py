import os
import getpass
import socket
import platform
import pwd
import subprocess


def get_basic_info():
    print("\nCurrent User:")
    print(getpass.getuser())

    print("\nHostname:")
    print(socket.gethostname())

    print("\nCurrent Working Directory:")
    print(os.getcwd())


def get_system_info():
    print("\nOperating System:")
    print(platform.system())

    print("\nKernel Version:")
    print(platform.release())


def get_user_id_info():
    user_info = pwd.getpwuid(os.getuid())

    print("\nUser ID Information:")
    print("Username:", user_info.pw_name)
    print("User ID:", os.getuid())
    print("Group ID:", os.getgid())


def get_environment_info():
    print("\nHome Directory:")
    print(os.environ.get("HOME"))

    print("\nCurrent Shell:")
    print(os.environ.get("SHELL"))

    print("\nPATH Variable:")
    print(os.environ.get("PATH"))


def get_process_info():
    print("\nRunning Processes:")

    result = subprocess.run(
        ["ps", "-e"],
        capture_output=True,
        text=True
    )

    print(result.stdout[:500])


def get_storage_info():
    print("\nStorage Information:")

    result = subprocess.run(
        ["diskutil", "list"],
        capture_output=True,
        text=True
    )

    print(result.stdout[:1500])


def get_network_info():
    print("\nNetwork Information:")

    result = subprocess.run(
        ["ifconfig"],
        capture_output=True,
        text=True
    )

    print(result.stdout[:1500])


def get_active_connections():
    print("\nActive Network Connections:")

    result = subprocess.run(
        ["netstat", "-an"],
        capture_output=True,
        text=True
    )

    print(result.stdout[:1500])


def get_logged_in_users():
    print("\nLogged In Users:")

    result = subprocess.run(
        ["who"],
        capture_output=True,
        text=True
    )

    print(result.stdout)


def main():
    print("=================================")
    print("Linux System Information Tool")
    print("Version 1.0")
    print("=================================")

    get_basic_info()
    get_system_info()
    get_user_id_info()
    get_environment_info()
    get_process_info()
    get_storage_info()
    get_network_info()
    get_active_connections()
    get_logged_in_users()


if __name__ == "__main__":
    main()