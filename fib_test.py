#!/usr/bin/python3
# fib_test.py - Fibonacci Numbers Test Program in Python
#
# From a video by mCoding at:
# https://www.youtube.com/watch?v=DnKxKFXB4NQ
#
# This is a simple recursive program to test the use of the
# @cache decorator in Python. This caches the results of the
# fib() function and saves having to recalculate any previously
# calculated values.
#
# The impact is noticeable with the program running in a few
# seconds with @cache but slowing down significantly by the
# time it hits the mid-30s without the @cache.

from functools import cache

@cache
def fib(n):
     if n <= 1:
          return n
     return fib(n - 1) + fib(n - 2)


def main():
    for i in range(76):
        print(i, fib(i))


if __name__ == '__main__':
    main()
