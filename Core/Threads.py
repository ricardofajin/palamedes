from multiprocessing import Process

def multi(vfunctions):
    n = len(vfunctions)
    for t in range(n):
        Process(target=vfunctions[n]).start()