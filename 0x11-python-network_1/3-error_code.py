#!/usr/bin/python3
"""
This module contain a script tha
"""
import urllib.request
import urllib.error
import sys

url = sys.argv[1]
try:
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print(content.decode('utf-8'))
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
