#!/usr/bin/env python

import sys
import requests

# with open('sites', 'r') as f:
#     sites = [line.strip() for line in f.readlines()]

sites = []
for line in sys.stdin:
    sites.append(line.strip())

# print(sites)

result = []
for site in sites:
    r = requests.head(site)
    if r.status_code != 200:
        result.append(f'❌  - {site} - {r.status_code}')

with open('result', 'w') as f:
    f.writelines(result)

# sys.stdout.write("\n".join(result))