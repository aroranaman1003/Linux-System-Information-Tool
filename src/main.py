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

def get_user_accounts():
    print("\nUser Accounts:")

    result = subprocess.run(
        ["cat", "/etc/passwd"],
        capture_output=True,
        text=True
    )

    print(result.stdout[:1000])

def get_group_info():
    print("\nGroup Information:")

    result = subprocess.run(
        ["cat", "/etc/group"],
        capture_output=True,
        text=True
    )

    print(result.stdout[:1000])

def get_current_user_details():
    print("\nCurrent User Details:")

    result = subprocess.run(
        ["id"],
        capture_output=True,
        text=True
    )

    print(result.stdout)

def get_sudo_information():
    print("\nSudo Configuration:")

    result = subprocess.run(
        ["cat", "/etc/sudoers"],
        capture_output=True,
        text=True
    )

    print(result.stdout[:1000])

def get_home_directory_files():
    print("\nHome Directory Analysis:")

    result = subprocess.run(
        ["ls", "-al", os.path.expanduser("~")],
        capture_output=True,
        text=True
    )

    print(result.stdout[:1500])

import shutil

def check_package_managers():
    managers = ["apt", "dpkg", "snap", "pip3", "brew"]

    print("\nPackage Managers:")

    for manager in managers:
        if shutil.which(manager):
            print(f"✓ {manager}")
        else:
            print(f"✗ {manager}")


def get_process_count():
    print("\nProcess Statistics:")

    result = subprocess.run(
        ["ps", "-e"],
        capture_output=True,
        text=True
    )

    processes = result.stdout.strip().split("\n")

    print("Total Processes:", len(processes) - 1)

def search_process(process_name):
    print(f"\nSearching for process: {process_name}")

    result = subprocess.run(
        ["ps", "-e"],
        capture_output=True,
        text=True
    )

    matches = []

    for line in result.stdout.splitlines():
        if process_name.lower() in line.lower():
            matches.append(line)

    if matches:
        print("Found Processes:")
        for process in matches[:10]:
            print(process)
    else:
        print("No matching process found.")


def get_top_processes():
    print("\nTop Processes:")

    result = subprocess.run(
        ["ps", "-e"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.splitlines()

    for line in lines[:10]:
        print(line)



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
    get_user_accounts()
    get_group_info()
    get_current_user_details()
    get_sudo_information()
    get_home_directory_files()
    check_package_managers()
    get_process_count()
    processsearch=input("\nEnter the process name you want to search: ")
    search_process(processsearch)
    get_top_processes()

if __name__ == "__main__":
    main()