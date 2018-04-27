# coding: utf-8
import sys
import subprocess
from subprocess import Popen

try:
    cmd = "cansend can0 123#abcdabcd"
    proc = Popen(cmd, shell=True)
    proc.wait()
except:
    import traceback
    traceback.print_exc()
finally:
    proc.terminate()
    sys.exit(0)

