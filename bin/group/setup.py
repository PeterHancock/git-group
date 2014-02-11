#! /usr/bin/python

import os
import shlex
import sys
import shutil

import core

def main():
    groupDir = os.path.join(os.getcwd(), ".gitgroup")
    try:
        os.mkdir(groupDir)
    except Exception, err:
        sys.stderr.write("ERROR: %s\n" % str(err))
        return 1
    try:
        os.chdir(groupDir)
        core.sh("git init")
        if len(sys.argv) < 1:
            raise RuntimeError("No repo supplied")
        repoUrl = sys.argv[1]
        core.sh("git remote add origin " + repoUrl)
        core.sh("git fetch origin")
        print "Created git group"
        return 0
    except Exception, err:
        sys.stderr.write("ERROR: %s\n" % str(err))
        shutil.rmtree(groupDir)
        return 1

if __name__ == "__main__":
    sys.exit(main())
