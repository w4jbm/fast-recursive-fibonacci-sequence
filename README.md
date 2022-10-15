# Fast Recursive Fibonacci Sequence Generator

These two programs look at ways to significantly improve performance of a recursive Fibonacci number generator in Python and Julia.

This is a rather contrived example and there are better ways to caclulate the first 76 numbers of the Fibonacci Sequence. But it is useful to demonstrate the impact caching or memorizing previous results can have on performance of functions.

In Python, the @cache decorator is used to store previously calculated values of the recursive Fibonacci function call. In Julia, the @memoize macho is used to do this.
