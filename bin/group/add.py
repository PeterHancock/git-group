#! /usr/bin/python

import os
import shutil
import sys

import core
import link

def main():
    try:
        if len(sys.argv) < 1:
            raise RuntimeError("No repo supplied")
        dir = sys.argv[1]
        if os.path.basename(dir) != dir:
            raise RuntimeError(dir + " is an invalid repo")
        dir = os.path.join(os.getcwd(), dir)
        if os.path.exists(dir):
            raise RuntimeError(dir + " already exists!")
    except Exception, err:
        sys.stderr.write("ERROR: %s\n" % str(err))
        return 1 
    try:
        os.mkdir(dir)
        os.chdir(dir)
        core.sh("git init")
        link.link(os.path.join(dir, ".git"))
        return 0               
    except Exception, err:
        sys.stderr.write("ERROR: %s\n" % str(err))
        shutil.rmtree(dir)
        return 1 

if __name__ == "__main__":
    sys.exit(main())

