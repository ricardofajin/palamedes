#/usr/bin/python3
# coding=utf-8

from Core import Scopes
from Utility import Parsers, Convertions, Banner


def main():
    Banner.banner()
    args = Parsers.getArgs()

    for f in args.scopeFiles:
        s = Scopes.Scope(Parsers.txtfiletoName(f), Convertions.filetoVector(f), args.interface, args.path)
        s.scan()


if __name__ == '__main__':
  main()
