from argparse import ArgumentParser

def getArgs():
    parser = ArgumentParser("palamedes.py")
    parser.add_argument("files", nargs='+')
    return parser.parse_args()
