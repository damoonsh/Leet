# Disk Usage

import os

def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print(f'{total}, {path}')

    return total

print(f'total: {disk_usage("../../")}')