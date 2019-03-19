#!/usr/bin/python3
import sys
from shlex import split


for line in sys.stdin:
   if line == "---\n":
      break
   print(line)
