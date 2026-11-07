"""Create a Bash file with 10 useful commands for WSL or Ubuntu."""

from pathlib import Path

script = """#!/usr/bin/env bash
# 10 useful commands for WSL / Ubuntu.
# Run individually in your terminal, or run this file with: bash ubuntu_wsl_basic_commands.sh

# 1. Show your current directory.
pwd

# 2. List files, including hidden files.
ls -la

# 3. Show your Linux username.
whoami

# 4. Show the current date and time.
date

# 5. Show Linux system information.
uname -a

# 6. Show available disk space in readable units.
df -h

# 7. Show memory usage in readable units.
free -h

# 8. List running processes.
ps aux

# 9. Find Python files in the current directory and its subdirectories.
find . -type f -name '*.py'

# 10. Show the size of the current directory.
du -sh .
"""

output = Path(__file__).with_name("ubuntu_wsl_basic_commands.sh")
output.write_text(script, encoding="utf-8", newline="\n")
print(f"Created {output}")
