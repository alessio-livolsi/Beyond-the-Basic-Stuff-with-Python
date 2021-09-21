# Code ran in shell
from pathlib import Path
path("spam") / "bacon" / "eggs"

# Code ran in shell
import subprocess, locale
procObj = subprocess.run(['ls', '-al'], stdout=subprocess.PIPE)
outputStr = procObj.stdout.decode(locale.getdefaultlocale()[1])
print(outputStr)

from pathlib import Path
import os
print(Path.cwd())