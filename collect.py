import os
import loggus

for path, dirs, files in os.walk("./"):
    if path.startswith("./.") or path.endswith("./"):
        continue
    print(path, dirs, files)


