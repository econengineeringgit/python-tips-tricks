## @njit()

* same as @jit(nopython= True)
* **C-compiles** the come
  * on the first run
  * greater speed-up achieved on second run
* can be **multi-threaded**
  * highly recommended to use with nogil= True
* can use GPU cores (CUDA only for now)

## @cache()

* from functools import cache
* stores return value of funcions
  * returns those is function is called with the same inputs
* many other similar tools exist in `functools` modul

## Threading

* from concurrent.futures import ThreadPoolExecutor

## Branchless programming

* can speed up C-compiled code
* code-specific investigation needed
