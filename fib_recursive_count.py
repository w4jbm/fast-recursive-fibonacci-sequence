#!/usr/bin/python3
# fib_recursive_count.py - Fibonacci Numbers Test Program in Python
#
# From a video by mCoding at:
# https://www.youtube.com/watch?v=DnKxKFXB4NQ
#
# This is a simple recursive program that originally demonstrated
# the @cache decorator in Python.
#
# This version has a simple modification to count the number of
# times the fib() fuction is called for each different value when
# the @cache decorator is turned off.

### For this test, we don't need this...
#from functools import cache

# We are going to calculate 0:15 (16 total) values...
list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

### For this test, we turn off the cache decorator
#@cache
def fib(n):
     list[n] += 1 # How many times does this get called
     if n <= 1:
          return n
     return fib(n - 1) + fib(n - 2)


def main():
    for i in range(16):
        print(i, fib(i))
    print('\nNumber of time fib(n) is called:')
    print(list)


if __name__ == '__main__':
    main()
