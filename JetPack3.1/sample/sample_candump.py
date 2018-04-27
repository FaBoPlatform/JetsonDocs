# coding: utf-8
import sys
import subprocess
from subprocess import Popen

try:
    cmd = "candump can1"
    proc = Popen(cmd, shell=True, stdout=subprocess.PIPE)
    # candumpの終了を待たずに1行読み込む
    out = proc.stdout.readline()
    print(out)
except:
    import traceback
    traceback.print_exc()
finally:
    proc.terminate()
    sys.exit(0)

