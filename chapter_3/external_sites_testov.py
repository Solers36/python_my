
"""Модифицируйте программу external_sites.py и задействуйте в ней
словарь со значениями по умолчанию. Это легко сделать, добавив
одну дополнительную инструкцию import и изменив всего две строки"""

import sys
from collections import defaultdict


sites = defaultdict(set)
for filename in sys.argv[1:]:
    with open(filename) as file:
        for line in file:
            i = 0
            while True:
                site = None
                i = line.find("http://", i)
                if i > -1:
                    i += len("http://")
                    for j in range(i, len(line)):
                        if not (line[j].isalnum() or line[j] in ".-"):
                            site = line[i:j].lower()
                            break
                    if site and "." in site:
                        sites[site].add(filename)
                    i = j
                else:
                    break

for site in sorted(sites):
    print("{0} is referred to in:".format(site))
    for filename in sorted(sites[site], key=str.lower):
        print("    {0}".format(filename))