from numba import jit, cuda
import numpy as np
from timeit import default_timer as timer

def normal_func(a):
    for i in range(10_000_000):
        a[i] += 1

@jit(target_backend='cuda')
def gpu_func(a):
    for i in range(10_000_000):
        a[i] += 1

if __name__ == '__main__':
    n = 10_000_000
    a = np.ones(n,dtype=np.float64)

    start = timer()
    normal_func(a)
    print(f"funkcja na CPU: {timer()-start}")

    start = timer()
    gpu_func(a)
    print(f"funkcja na GPU: {timer() - start}")
