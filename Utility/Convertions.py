def filetoVector(file):
    ipv = []
    escopo = open(file,'r')
    for ip in escopo.readlines():
        ipv.append(ip.replace('\n',''))
    escopo.close()
    return(ipv)