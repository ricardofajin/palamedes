#/usr/bin/python3
# coding=utf-8

from Core import Scan, Threads
from Utility import Parsers, Convertions, Banner


def main():
    Banner.banner()

    scope = []

    # TODO: matriz[scopes][vlans]
    args = Parsers.getArgs()
    for f in args.files:
        scope.append(Convertions.filetoVector(f))

    for t in scope:
        Threads.multi(scope[t])


if __name__ == '__main__':
  main()

  
  
#TODO: erro 2 - falta de CIDR(Classless Inter-Doamin Routing) /24 /23 ...
#      erro 3 - IPs Invalidos 
#      erro 4 - Falta de modulos(nmap) - https://www.youtube.com/watch?v=ufOrfPQOKvU
