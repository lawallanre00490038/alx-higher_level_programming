#!/usr/bin/python3
"""
Please test your script in the sandbox provided
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
