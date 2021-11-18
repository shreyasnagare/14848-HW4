import math
import sys

current_yearMonthDay = None
max_temperature = -math.inf

for line in sys.stdin:
    line = line.strip()
    yearMonthDay, temperature = line.split(sep="\t", maxsplit=1)

    try:
        temperature = int(temperature)
    except ValueError:
        continue

    if yearMonthDay == current_yearMonthDay:
        max_temperature = max(temperature, max_temperature)
    else:
        if current_yearMonthDay:
            print(f"{current_yearMonthDay}\t{max_temperature}")
        current_yearMonthDay = yearMonthDay
        max_temperature = temperature

if current_yearMonthDay:
    print(f"{current_yearMonthDay}\t{max_temperature}")
