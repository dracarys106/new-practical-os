# Practical 02 — Linux Information, File and Directory Commands

[Back to Index](../README.md)

## Practical Question

**Execute various LINUX commands:**

1. Information Maintenance: `wc`, `clear`, `cal`, `who`, `date`, `pwd`
2. File Management: `cat`, `cp`, `rm`, `mv`, `cmp`, `comm`, `diff`, `find`, `grep`, `awk`
3. Directory Management: `cd`, `mkdir`, `rmdir`, `ls`

## Aim

To execute and understand basic Linux commands used for system information, file management and directory management.

## Requirements

Linux terminal (Ubuntu or another Linux distribution).

## 1. Information Maintenance Commands

| Command | Purpose | Example |
|---|---|---|
| `wc` | Counts lines, words and bytes | `wc notes.txt` |
| `clear` | Clears terminal display | `clear` |
| `cal` | Displays a calendar (may require the `ncal` package) | `cal` |
| `who` | Displays users currently logged in | `who` |
| `date` | Displays current date and time | `date` |
| `pwd` | Displays present working directory | `pwd` |

Useful variations:

```bash
wc -l notes.txt       # Count lines
wc -w notes.txt       # Count words
wc -c notes.txt       # Count bytes
date "+%d-%m-%Y"
```

## 2. File Management Commands

Create sample files first:

```bash
printf "Operating System\nLinux commands\n" > file1.txt
printf "Operating System\nPython programming\n" > file2.txt
```

| Command | Purpose | Example |
|---|---|---|
| `cat` | Displays or joins file contents | `cat file1.txt` |
| `cp` | Copies files | `cp file1.txt copy.txt` |
| `rm` | Removes a file | `rm copy.txt` |
| `mv` | Moves or renames a file | `mv file2.txt renamed.txt` |
| `cmp` | Compares two files byte by byte | `cmp file1.txt file2.txt` |
| `comm` | Compares two sorted files line by line | `comm sorted1.txt sorted2.txt` |
| `diff` | Displays line-by-line differences | `diff file1.txt file2.txt` |
| `find` | Searches for files/directories | `find . -name "*.txt"` |
| `grep` | Searches text matching a pattern | `grep "Linux" file1.txt` |
| `awk` | Processes text by fields/patterns | `awk '{print $1}' file1.txt` |

More examples:

```bash
cat file1.txt
cat file1.txt file2.txt
cp file1.txt backup.txt
mv backup.txt backup_old.txt
cmp file1.txt file2.txt
sort file1.txt > sorted1.txt
sort file2.txt > sorted2.txt
comm sorted1.txt sorted2.txt
diff file1.txt file2.txt
find . -type f -name "*.txt"
grep -n "Linux" file1.txt
awk '{print NR, $0}' file1.txt
```

**Note:** `comm` expects sorted input files. The `awk` example prints the line number and full line.

## 3. Directory Management Commands

| Command | Purpose | Example |
|---|---|---|
| `cd` | Changes current directory | `cd Documents` |
| `mkdir` | Creates a directory | `mkdir OS_Practical` |
| `rmdir` | Removes an empty directory | `rmdir OS_Practical` |
| `ls` | Lists directory contents | `ls -l` |

More examples:

```bash
pwd
mkdir OS_Practical
cd OS_Practical
touch sample.txt
ls -la
cd ..
rmdir OS_Practical   # Works only when the directory is empty
```

## Result

The Linux information maintenance, file management and directory management commands were executed and studied.

## Important Details

- Linux commands are case-sensitive.
- `rm` permanently removes files in normal terminal use; check the filename before executing it.
- `rmdir` removes only empty directories.
- `comm` requires sorted input.
- `>` redirects output to a file and overwrites that file; `>>` appends output.
- Some minimal Linux installations may not include `cal` by default.
