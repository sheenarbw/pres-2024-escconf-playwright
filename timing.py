s = """
- me: 1:45
- demo: 2:30
- what's in the box: 5:00
- architecture: 2:40 
- why playwright: 2:45 
- demo: 12:30
"""

import re


total_seconds = 0
for line in s.split("\n"):
    m = re.search(r".*: (\d+):(\d+)", line)
    if m:
        minutes, seconds = m.groups()
        total_seconds += 60 * int(minutes)
        total_seconds += int(seconds)

final_minutes = total_seconds // 60
final_seconds = total_seconds % 60

print(f"TOTAL = {final_minutes}:{final_seconds}")
