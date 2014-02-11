import subprocess

def sh(cmd):
    proc = subprocess.Popen(cmd, shell = True)
    if proc.wait() != 0:
        raise RuntimeError(cmd)
