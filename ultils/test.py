import numpy as np
import time 
from numba import vectorize, cuda, jit

# @vectorize(['float32(float32, float32)'], target = 'gpu')
# def add(a, b):
#     return a + b


# def main():
#     n = 32000000
#     a = np.ones(n, dtype=np.float32)
#     b = np.ones(n, dtype=np.float32)
    
#     start = time.time()
#     c = add(a, b)
#     vector_add_time = time.time() - start
#     print('c[:5] = ', str(c[:5]))
#     print('c[-5:] = ', str(c[-5:]))
#     print(vector_add_time)
    
# if __name__ == '__main__':
#     main()
    