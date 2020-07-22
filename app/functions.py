import os
import shutil

def directory(path):
    tree = []
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            fn = os.path.join(path, name)
            if os.path.isdir(fn):
                tree.append(name)
    return tree

def filefinder(path):
    tree = []
    try: lst = os.listdir(path)
    except OSError:
        pass #ignore errors
    else:
        for name in lst:
            if os.path.isfile(os.path.join(path, name)):
                tree.append(name)
    return tree


def filemover(inputFile, destDirectory):
    #Moving forward code
    path = os.path.join(os.getcwd())
    shutil.move(inputFile, destDirectory)
    print('Zoom!!')