#!/usr/bin/env python3

from person import Person

import random
import math
import matplotlib.pyplot as plt
from time import perf_counter as pc
from time import sleep as pause
import concurrent.futures as future
import numpy as np
from numba import njit

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
	
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return fib_numba(n-1) + fib_numba(n-2)

def graph(q,w):
	x = range(q,w)
	y_cpp = []
	y_numba = []
	y_py = []

	for i in x:
		print(i)
		t1 = pc()
		f = Person(i)
		f.fib()
		t2 = pc()
		fib_numba(i)
		t3 = pc()
		fib_py(i)
		t4 = pc()

		y_cpp.append(t2-t1)
		y_numba.append(t3-t2)
		y_py.append(t4-t3)

	plt.plot(x, y_cpp, "r", label = "C++")
	plt.plot(x, y_numba, "g", label = "Numba")
	plt.plot(x, y_py, "b", label = "py")

	plt.yscale('log')
	plt.xlabel('n')
	plt.ylabel('Time (s)')
	plt.title('r = C++, g = Numba, B = Py')
	plt.savefig(f'{q} to {w} logFib_TimeComparsion.png')

def time47():
	x = 47
	t1 = pc()
	f = Person(x)
	print(f'C++: {f.fib()}')
	t2 = pc()
	print(f'numba: {fib_numba(x)}')
	t3 = pc()
	print(f'C++: {round(t2-t1,4)}')
	print(f'Numba:{round(t3-t2,4)}')

def main():
	graph(20,31)
	time47()
	graph(30,46)

if __name__ == '__main__':
	main()
