#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    operators = {"+": add, "-": sub, "*": mul, "/": div}

    if op not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    result = operators[op](a, b)
    print(f"{a} {op} {b} = {result}")
