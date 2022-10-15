#!/usr/bin/julia
# fib_test.jl - Fibonacci Numbers Test Program in Julia
#
# Expanding on the idea around Python's @cache decorator discussed
# in a video by mCoding at:
# https://www.youtube.com/watch?v=DnKxKFXB4NQ
#
# This is a simple recursive program to test the use of the
# @memoize macro in Julia. This memorizes/caches the results of
# the fib() function and saves having to recalculate any previously
# calculated values.
#
# The impact is noticeable with the program running in a few
# seconds with @memoize but slowing down significantly by the
# time it hits the 40s without the @memoize macro.


# If you have not previously imported Memoize, you ned to
# uncomment the following line for the first run:
# import Pkg; Pkg.add("Memoize")

using Memoize


@memoize function fib(n)
     if n <= 1
         return n
     else
         return fib(n-1) + fib(n-2)
     end
end

# NOTE: The fib(n) function can be greatly "shortened" (I would
# not use the word "simplified") to:
#
# fib(n) = n <= 1 ? n : fib(n-2) + fib(n-1)


for i in 0:75
    println(i, " ", fib(i))
end
