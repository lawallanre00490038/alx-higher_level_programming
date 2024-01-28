#!/usr/bin/python3
def no_c(my_string):
	newString = ""
	for s in newString:
		if s in ["c", "C"]:
			continue
		newString.append(s)
	return ("{:s}".format(newString))
