import os

def path(f):
    cwd = os.getcwd()
    p = "file://{}/{}".format(cwd,f)
    print('****** ' + p)
    return p
