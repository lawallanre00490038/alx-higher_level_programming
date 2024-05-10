#!/usr/bin/python3
"""
You must use the with statement
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
