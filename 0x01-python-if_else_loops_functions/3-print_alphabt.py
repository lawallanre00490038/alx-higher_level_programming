#!/usr/bin/python3
for character in range(97, 123):
	if chr(character) in "qe":
		continue
	print("{}".format(chr(character)), end='')
