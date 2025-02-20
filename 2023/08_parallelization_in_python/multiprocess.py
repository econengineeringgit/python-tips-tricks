import time
from multiprocessing import Pool

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

if __name__ == "__main__":
    inputs = [31, 32, 33, 34, 35]
    start = time.time()
    with Pool() as pool:
        results = pool.map(Fibonacci, inputs)
    print(f"Elapsed time: {time.time() - start}s.")
    print(results)
