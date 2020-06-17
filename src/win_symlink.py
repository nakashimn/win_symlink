import os
import sys

if __name__=="__main__":

    if len(sys.argv) != 2:
        exit()

    src_path = sys.argv[1]

    if not os.path.exists(src_path):
        exit()

    dirpath = os.path.dirname(src_path)
    filename = os.path.basename(src_path)
    os.symlink(src_path, "{}/{}_symlink".format(dirpath, filename))
