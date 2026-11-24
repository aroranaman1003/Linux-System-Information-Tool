from modules.system_info import show_system_info
from modules.user_info import show_users
from modules.process_monitor import show_processes, search_process
from modules.resource_monitor import show_resources
from modules.storage_monitor import show_storage
from modules.network_monitor import show_network, show_connections
from modules.health_monitor import health_check
from modules.cpu_scheduler import cpu_scheduler, advanced_scheduling
from modules.thread_manager import thread_demo
from modules.synchronization import synchronization_menu
from modules.deadlock_manager import deadlock_menu
from modules.memory_manager import memory_menu
from modules.ipc_manager import ipc_menu


def main():
    while True:
        print("""
================================================
       INTEGRATED OPERATING SYSTEM TOOLKIT
                    VERSION 4.0
================================================

 LIVE SYSTEM MONITORING
 1. System Information
 2. User Information
 3. Process Monitoring
 4. Search Process
 5. CPU and RAM Monitoring
 6. Storage Monitoring
 7. Network Monitoring
 8. Active Network Connections
 9. System Health Check

 OS ALGORITHM SIMULATOR
10. CPU Scheduling Algorithms
11. Advanced Scheduling (MLQ / MLFQ)
12. Thread Management
13. Process Synchronization
14. Deadlock Management
15. Memory Management and Paging
16. Inter-Process Communication

 0. Exit
================================================
""")
        choice = input("Enter your choice: ")

        actions = {
            "1": show_system_info,
            "2": show_users,
            "3": show_processes,
            "4": search_process,
            "5": show_resources,
            "6": show_storage,
            "7": show_network,
            "8": show_connections,
            "9": health_check,
            "10": cpu_scheduler,
            "11": advanced_scheduling,
            "12": thread_demo,
            "13": synchronization_menu,
            "14": deadlock_menu,
            "15": memory_menu,
            "16": ipc_menu
        }

        if choice == "0":
            print("Thank you for using Integrated OS Toolkit!")
            break

        action = actions.get(choice)
        if action:
            try:
                action()
            except (ValueError, IndexError) as error:
                print("Invalid input:", error)
            except Exception as error:
                print("Operation failed:", error)
        else:
            print("Invalid choice!")

        input("\nPress Enter to return to main menu...")


if __name__ == "__main__":
    main()
