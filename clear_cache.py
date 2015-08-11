#!/usr/bin/env python

import requests

THRESHOLD = 95

r = requests.get('http://localhost:9200/_nodes/stats')
mem_used = []
for node in r.json()['nodes']:
    heap_used = r.json()['nodes'][node]['jvm']['mem']['heap_used_in_bytes']
    heap_max = r.json()['nodes'][node]['jvm']['mem']['heap_max_in_bytes']
    mem_used.append(round(((float(heap_used) / float(heap_max)) * 100), 2))

num_over_limit = len([x for x in mem_used if x > THRESHOLD])

if num_over_limit:
    r = requests.post('http://localhost:9200/_cache/clear')
    print r.text
