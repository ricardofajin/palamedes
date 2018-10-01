import nmap
import threading
from colorama import Fore, Style
from Utility import Loading

def tcp(ip,interface,folder='results'):
    print('[' + Fore.GREEN + 'TCP - SCANNING' + Style.RESET_ALL + '] - ' + ip)

    def aux_Scan_Tcp():
        try:
            nm = nmap.PortScanner()
            param = '-sV --open -sC -T3 -e ' + interface + ' -o ' + folder + '/' + ip.replace('/', '-') + '_TCP.txt'
            nm.scan(ip, '445', param)
        except Exception as e:
            e = str(e)
            e = e.replace("'", "")
            e = e.replace("\\nQUITTING!\\n", "")
            print("\n[" + Fore.RED + "ERROR" + Style.RESET_ALL + "]" " - " + e)
            exit()



    the_process = threading.Thread(name='Scan TCP - Palapica 8==D', target=aux_Scan_Tcp)
    the_process.start()

    while the_process.isAlive():
        Loading.animated()
        if the_process.isAlive() != True:
            print(' - FINISH\n')

def udp(ip,interface,folder='results'):
    print('[' + Fore.BLUE + 'UDP - SCANNING' + Style.RESET_ALL + '] - ' + ip)

    def aux_Scan_Udp():
        nm = nmap.PortScanner()
        try:
            param = '-sV -sC -sU -T3 --open -e ' + interface + ' -oN ' + folder + '/' + ip.replace('/', '-') + '_UDP.txt'
            nm.scan(ip, '445', param)

        except nmap.nmap.PortScannerError as e:
            e = str(e)
            e = e.replace("'", "")
            e = e.replace("\\nQUITTING!\\n", "")
            print("\n[" + Fore.RED + "ERROR" + Style.RESET_ALL + "]" " - " + e)
            exit()


    the_process = threading.Thread(name='Scan UDP - Palapica 8==D', target=aux_Scan_Udp)
    the_process.start()

    while the_process.isAlive():
        Loading.animated()
        if the_process.isAlive() != True:
            print(' - FINISH\n')

