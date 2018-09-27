import socket

# encontrar melhor jeito de validar se uma string é um IP
def validate(addr):
    try:
        socket.inet_aton(addr)
        # legal
        print("IP " + addr)
        return 1
    except socket.error:
        # Not legal
        print("erro - IP Invalido")
        return 0