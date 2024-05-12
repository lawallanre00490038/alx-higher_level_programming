#!/usr/bin/python3
""" Test function find_peak """
# import find_peak function from the file 6-peak.py in the parent directory. two dots before the slash means parent directory
from os import sys
sys.path.append('..')
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 3, 1]))
