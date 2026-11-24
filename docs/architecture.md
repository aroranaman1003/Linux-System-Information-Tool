cat > docs/architecture.md <<'EOF'
# Integrated Operating Systems Management & Simulation Toolkit

## 1. Project Overview
A Python-based application designed to demonstrate Operating System concepts through real-time system monitoring and algorithm simulations.

## 2. Project Objectives
- Monitor system resources.
- Manage and inspect processes.
- Simulate CPU scheduling algorithms.
- Demonstrate thread management and synchronization.
- Implement deadlock avoidance.
- Simulate memory management and paging.
- Demonstrate inter-process communication.

## 3. Technology Stack
- Python 3
- Linux / Ubuntu
- psutil
- Python threading
- Multiprocessing
- Operating System system utilities

## 4. System Modules

### Live System Monitoring
- System Information
- User Information
- Process Monitoring
- CPU and RAM Monitoring
- Disk Monitoring
- Network Monitoring
- System Health Check

### CPU Scheduling
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Shortest Remaining Time First (SRTF)
- Priority Scheduling
- Round Robin (RR)
- Multilevel Queue (MLQ)
- Multilevel Feedback Queue (MLFQ)

### Thread Management
- Thread Creation
- Multithreading
- Thread Execution

### Process Synchronization
- Mutex Locks
- Semaphores
- Peterson's Solution

### Deadlock Management
- Banker's Algorithm
- Safe State Detection

### Memory Management
- Paging
- Address Translation
- FIFO Page Replacement
- LRU Page Replacement

### Inter-Process Communication
- Pipes
- Shared Memory

## 5. Architecture

User
  |
  v
Main Menu (main.py)
  |
  +-- System Monitoring
  |
  +-- Process Management
  |
  +-- CPU Scheduling
  |
  +-- Thread Management
  |
  +-- Synchronization
  |
  +-- Deadlock Management
  |
  +-- Memory Management
  |
  +-- IPC

## 6. Expected Output
The application will provide system information, resource statistics, scheduling results, algorithm simulations, and monitoring reports.

## 7. Development Status
Version 4.0 - Under Development
EOF