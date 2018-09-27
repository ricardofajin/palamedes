#/usr/bin/python3
import sys
import socket
from colorama import Fore, Back, Style 

def filetoVector(file):
    ipv = []
    escopo = open(file,'r')
    for ip in escopo.readlines():
        ipv.append(ip.replace('\n',''))
    return(ipv)    
        
def validateIp(addr):
    
    try:
        socket.inet_aton(addr)
        # legal
        print("IP "+ addr)
        return 1
    except socket.error:
        # Not legal
        print("erro - IP Invalido")
        return 0

def main():
    print("""
        ____        __                         __         
       / __ \____ _/ /___ _____ ___  ___  ____/ /__  _____
      / /_/ / __ `/ / __ `/ __ `__ \/ _ \/ __  / _ \/ ___/
     / ____/ /_/ / / /_/ / / / / / /  __/ /_/ /  __(__  ) 
    /_/    \__,_/_/\__,_/_/ /_/ /_/\___/\__,_/\___/____/  
                                                          
    "- A preguiça, o ócio e a recreação revigoravam as energias para a batalha."
                                                      """)
    print("Palamedes v0.1 - Teste segmentacao")
    #erro 1 - falta de argumento    
    if len(sys.argv) == 2:
        ipv = filetoVector(sys.argv[1])
        
        print(Fore.GREEN + "Escopo:" + Style.RESET_ALL)
        print(ipv)
        #validar o IP
        #validateIp(ipv)

        print(p)
        exit()
    else:
        print(Fore.RED + "\n[ERRO] - " + Style.RESET_ALL +"Insira um arquivo de texto")
        print("         Ex: python palamedes.py scope.txt")


if __name__ == '__main__':
  main()
  
  
#TODO: erro 2 - falta de CIDR(Classless Inter-Doamin Routing) /24 /23 ...
#      erro 3 - IPs Invalidos 
#      erro 4 - Falta de modulos(nmap) - https://www.youtube.com/watch?v=ufOrfPQOKvU
