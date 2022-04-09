#!/usr/bin/env python3
import subprocess
import sys

# >>> import sys
# >>> sys.executable
# '/Users/arkchauhan/opt/anaconda3/envs/4c16/bin/python3'

exe_path = sys.executable
# x = subprocess.run([exe_path, "-c", "ls -la"])
x = subprocess.run(["ls", "-la"])
print(x.args, x.returncode)  # x = CompletedProcess(args=['ls', '-la'], returncode=0)

x = subprocess.run(["ls", "-la"], capture_output=True)
print(x)

