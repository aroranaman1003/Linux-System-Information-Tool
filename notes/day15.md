# Day 15

## Processes

A process is an instance of a running program.

Examples:
- Chrome
- VS Code
- Python

### Commands

ps -e
ps -aux

Used to view running processes.

---

## Daemons

Daemons are background services in Linux.

Examples:

- sshd
- ntpd
- systemd-journald

They provide services such as:

- Networking
- Time Synchronization
- SSH Access
- Logging

---

## systemd

systemd is the most common Linux init system.

Responsibilities:

- Starts services
- Mounts file systems
- Manages daemons

### Process Tree

pstree

---

## systemctl

Used to manage services.

### Service Status

sudo systemctl status sshd

### Start Service

sudo systemctl start sshd

### Stop Service

sudo systemctl stop sshd

### Restart Service

sudo systemctl restart sshd

### Reload Service

sudo systemctl reload sshd

### Reload Or Restart

sudo systemctl reload-or-restart sshd

---

## Enable And Disable Services

Enable:

sudo systemctl enable sshd

Disable:

sudo systemctl disable sshd

Check:

sudo systemctl is-active sshd

sudo systemctl is-enabled sshd

---

## Listing Units

sudo systemctl list-units

sudo systemctl list-units --all

sudo systemctl list-unit-files

---

## journalctl

Linux logging utility.

sudo journalctl -xe

---

## Masking Services

Mask:

sudo systemctl mask ntp

Unmask:

sudo systemctl unmask ntp

---

## Targets

Target = Desired system state.

Examples:

- multi-user.target
- rescue.target
- reboot.target

Commands:

sudo systemctl get-default

sudo systemctl status multi-user.target

sudo systemctl list-dependencies multi-user.target

---

## Reboot

sudo systemctl reboot

---

## Project Connection

Added:

- Process Count
- Process Search
- Top Processes

Learned:

- Daemons
- systemd
- systemctl
- journalctl
- Targets