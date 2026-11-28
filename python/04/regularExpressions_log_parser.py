"""A practical regex example: parse structured application logs.

The pattern uses named groups so each important part of a log line can be read
by a meaningful name rather than by a numeric position.
"""

import re
from collections import Counter


# Example expected line:
# 2026-11-28 09:15:10 | ERROR | user=habib | Login failed
LOG_PATTERN = re.compile(
    r"^(?P<date>\d{4}-\d{2}-\d{2}) "
    r"(?P<time>\d{2}:\d{2}:\d{2})\s+\|\s+"
    r"(?P<level>INFO|WARNING|ERROR)\s+\|\s+"
    r"user=(?P<user>[A-Za-z][A-Za-z0-9_]{2,15})\s+\|\s+"
    r"(?P<message>.+)$"
)

logs = [
    "2026-11-28 09:15:10 | ERROR | user=habib | Login failed",
    "2026-11-28 09:16:03 | INFO | user=sara_1 | Login successful",
    "2026-11-28 09:17:22 | WARNING | user=admin | Password expires soon",
    "This line does not have the expected format",
]

levels = Counter()

for line in logs:
    match = LOG_PATTERN.fullmatch(line)

    if match is None:
        print(f"Invalid log line: {line!r}")
        continue

    record = match.groupdict()
    levels[record["level"]] += 1

    print(
        f"[{record['level']}] {record['date']} {record['time']} - "
        f"{record['user']}: {record['message']}"
    )

print("\nLog summary")
for level in ("INFO", "WARNING", "ERROR"):
    print(f"{level}: {levels[level]}")
