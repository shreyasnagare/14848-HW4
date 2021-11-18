import sys

locations = {
    "yearMonthDay": (15, 23),
    "temperature": (87, 92),
    "quality": (92, 93),
}


def valid_record(yearMonthDay: str, temperature: str, quality: str):
    return (int(temperature) != 9999) and (int(quality) in [0, 1, 4, 5, 9])


for line in sys.stdin:
    line = line.strip()
    record = {k: line[slice(*v)] for k, v in locations.items()}
    if valid_record(**record):
        print("{yearMonthDay}\t{temperature}".format(**record))