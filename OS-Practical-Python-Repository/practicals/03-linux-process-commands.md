# Practical 03 — Linux Process, Communication and Protection Commands

[Back to Index](../README.md)

## Practical Question

**Execute various LINUX commands:**

1. Process Control: `fork`, `getpid`, `ps`, `kill`, `sleep`
2. Communication: Input-output redirection, Pipe
3. Protection Management: `chmod`, `chown`, `chgrp`

## Aim

To study Linux commands and shell features used for process control, communication and file protection.

## Requirements

Linux terminal. Some operations, especially ownership changes, may require administrator privileges.

## 1. Process Control

| Command / call | Purpose | Example |
|---|---|---|
| `fork()` | System call that creates a child process | Demonstrated through Python in Practical 04 |
| `getpid()` | System call that returns the current process ID | `os.getpid()` in Python |
| `ps` | Displays process information | `ps` |
| `kill` | Sends a signal to a process | `kill PID` |
| `sleep` | Pauses execution for a specified time | `sleep 5` |

Useful commands:

```bash
ps
ps -ef
ps aux
sleep 5
```

To stop a process, first find its PID:

```bash
ps -ef
kill PID
```

Replace `PID` with the actual process ID. `kill PID` normally sends `SIGTERM`, requesting that the process terminate. Use `kill -9 PID` only when necessary because it sends `SIGKILL` and does not allow normal cleanup.

**Note:** `fork()` and `getpid()` are system calls/functions, not ordinary shell commands on most Linux distributions. Their use is demonstrated in the Python program for Practical 04.

## 2. Communication — Redirection and Pipes

### Input redirection

```bash
wc -l < file.txt
```

The shell supplies `file.txt` as standard input to `wc`.

### Output redirection

```bash
ls > output.txt
```

Saves command output in `output.txt`, replacing its previous contents.

### Append redirection

```bash
date >> output.txt
```

Appends the date output to the end of the file.

### Error redirection

```bash
ls missing_file 2> error.txt
```

Saves standard error in `error.txt`.

### Pipe

```bash
ps aux | grep python
```

The pipe `|` sends the standard output of the command on its left to the standard input of the command on its right.

Another example:

```bash
cat file.txt | wc -l
```

## 3. Protection Management

| Command | Purpose | Example |
|---|---|---|
| `chmod` | Changes file permissions | `chmod 644 file.txt` |
| `chown` | Changes file owner | `sudo chown user file.txt` |
| `chgrp` | Changes file group | `sudo chgrp groupname file.txt` |

### Permission example

```bash
chmod 755 script.sh
```

Permission values:

- `r` = read = 4
- `w` = write = 2
- `x` = execute = 1

For `755`:
- Owner: `7` = read + write + execute
- Group: `5` = read + execute
- Others: `5` = read + execute

Symbolic example:

```bash
chmod u+x script.sh
```

Adds execute permission for the file owner.

Ownership examples (replace placeholders with real account/group names):

```bash
sudo chown username file.txt
sudo chgrp groupname file.txt
```

## Result

Linux process-control commands, input/output redirection, pipes and protection-management commands were studied and executed.

## Important Details

- Use a real PID when running `kill`; never copy an example PID blindly.
- `chown` and `chgrp` may require `sudo`.
- Do not change ownership or permissions of system files for practice.
- Redirection operators are shell features; they are not separate Linux programs.
