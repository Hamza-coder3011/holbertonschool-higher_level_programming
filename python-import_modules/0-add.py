#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
	a = 1
	b = 2
	result = add(a, b)
	print("{a} + {b} = {result}".format(a=a, b=b, result=result))
