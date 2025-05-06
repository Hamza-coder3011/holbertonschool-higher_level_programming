#!/usr/bin/python3
for alphas in range(97, 123):
    if chr(alphas) not in ('e', 'q'):
        print("{}".format(chr(alphas)), end="")
