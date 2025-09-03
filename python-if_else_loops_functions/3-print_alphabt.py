#!/usr/bin/python3
print(
    "{}".format(
        ''.join(
            chr(letter) for letter in range(97, 123)
            if letter not in (101, 113)
        )
    ),
    end=""
)
