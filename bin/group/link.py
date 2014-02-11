#! /usr/bin/python

import os
import sys
import shutil

import core

def link(dir):
    os.chdir(dir)
    for i in "branches config hooks info objects refs packed-refs svn".split():
        core.sh("rm -rf " + i)
        core.sh("ln -sf ../../.gitgroup/.git/" + i + " " + i) 

def main():
    try:
        if len(sys.argv) < 1:
            raise RuntimeError("No repo supplied")
        dir = sys.argv[1]
        if os.path.basename(dir) != dir:
            raise RuntimeError(dir + " is an invalid repo")
        dir = os.path.join(os.getcwd(), dir, ".git")
        if os.path.exists(dir) is False:
            raise RuntimeError(dir + " does not exist!")
        link(dir)
        return 0
    except Exception, err:
        sys.stderr.write("ERROR: %s\n" % str(err))
        return 1

if __name__ == "__main__":
    sys.exit(main())

