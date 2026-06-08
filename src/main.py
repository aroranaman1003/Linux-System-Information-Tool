import os
import getpass
import socket
import platform
import pwd

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