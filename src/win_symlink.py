import os
import sys
import pyinstaller

if __name__=="__main__":

    if len(sys.argv) != 2:
        exit()

    src_path = sys.argv[1]

    if not os.path.exists(src_path):
        exit()

    filename = os.path.basename(src_path)
    os.symlink(src_path, "./{}".format(filename))
