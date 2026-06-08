import os
import getpass
import socket
import platform
import pwd
import subprocess

print("=================================")
print("Linux System Information Tool")
print("Version 0.3")
print("=================================")

print("\nCurrent User:")
print(getpass.getuser())

print("\nHostname:")
print(socket.gethostname())

print("\nCurrent Working Directory:")
print(os.getcwd())

print("\nOperating System:")
print(platform.system())

print("\nKernel Version:")
print(platform.release())
print("\nUser ID Information:")

user_info = pwd.getpwuid(os.getuid())

print("Username:", user_info.pw_name)
print("User ID:", os.getuid())
print("Group ID:", os.getgid())

print("\nHome Directory:")
print(os.environ.get("HOME"))

print("\nCurrent Shell:")
print(os.environ.get("SHELL"))

print("\nPATH Variable:")
print(os.environ.get("PATH"))

print("\nRunning Processes:")

result = subprocess.run(
    ["ps", "-e"],
    capture_output=True,
    text=True
)

print(result.stdout[:500])