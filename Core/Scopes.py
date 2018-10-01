from Core import Scan
from Utility import Check, Make

class Scope:

    def __init__(self, scopeName, vlans, interface, path):
        self.scopeName = scopeName
        self.vlans = vlans
        self.interface = interface
        self.path = path

    def scan(self):
        if Check.dir(str(self.path)):
            pass
        else:
            Make.dir(str(self.path))

        for ip in self.vlans:
            Scan.tcp(ip, self.interface, self.path)
            Scan.udp(ip, self.interface, self.path)
