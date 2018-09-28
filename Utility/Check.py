from os.path import isdir, isfile, exists


def file(file):
    if isfile(file):
        return exists(file)
    else:
        return False


def dir(dir):
    if isdir(dir):
        return exists(dir)
    else:
        return False