#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], "r") as f:
    for line in f.readlines():
        line.strip()
        line.replace(jane, jdoe)

subprocess.run(["cd ~/data", "mv *{}* *{}*".format("jane", "jdoe")]) 
