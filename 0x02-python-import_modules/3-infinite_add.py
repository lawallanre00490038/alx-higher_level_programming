#!/usr/bin/python3
import sys
def main():
	args = sum([int(arg) for arg in sys.argv[1:]])
	print (args)

if __name__ == "__main__":
	main()
