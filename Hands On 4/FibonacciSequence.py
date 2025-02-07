# Fibonacci Sequence

import timeit

def fib(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fib(n - 1) + fib(n - 2)

def fibImproved(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = a + b
        a = b
        b = temp
    
    return b

n = int(input("Enter the number: "))
print("\n1. Fibonnaci Number By Given Algorithm")
start = timeit.default_timer()
print(f"Fibonnaci Number at index {n} is : {fib(n)} and taken time is {(timeit.default_timer() - start) * 1000000:.2f} microseconds\n")
print("\n1. Fibonnaci Number By Improved Algorithm 1")
start = timeit.default_timer()
print(f"Fibonnaci Number at index {n} is : {fibImproved(n)} and taken time is {(timeit.default_timer() - start) * 1000000:.2f} microseconds\n")