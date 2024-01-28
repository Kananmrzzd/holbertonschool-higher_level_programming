#!/usr/bin/python3

"""Print the result of the addition of all arguments."""
import sys

total = 0
for i in range(1, len(sys.argv)):
    total += int(sys.argv[i])
print("{}".format(total))
