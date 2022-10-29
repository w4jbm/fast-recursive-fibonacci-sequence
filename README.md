# Fast Recursive Fibonacci Sequence Generator

These two programs look at ways to significantly improve performance of a recursive Fibonacci number generator in Python and Julia.

This is a rather contrived example and there are better ways to caclulate the first 76 numbers of the Fibonacci Sequence. But it is useful to demonstrate the impact caching or memorizing previous results can have on performance of functions.

In Python, the @cache decorator is used to store previously calculated values of the recursive Fibonacci function call. In Julia, the @memoize macho is used to do this.

## Some further observations...

Why is the recursive Fibonacci (fib(x) = fib(x-1) + fib(x-2)) so slow? Well, I kind of knew why and realistically it is not the way you would go about solving for the sequence. (Rather it started as a way to demonstrate the impact of caching previously calculated function values.)

But, interestingly, the answer to why it's slow is very similar to the Fibonacci sequence itself.

To keep things simple, I calculated the first 15 values in the Fibonacci sequence.

Thinking about it first, if we are going to calculate fib(15) we would call fib(15). That call would, in turn, trigger calls to fib(14) and fib(13). Also, that call to fib(14) would cause calls to fib(13) and fib(12) while the call to fib(13) would cause calls to fib(12) and fib(11).

I inserted a counter that tracks how many times the fib() function was called for each value and ran it for calculating the first 15 numbers of the sequence. This is tracked in a list and printed when things finish up.

![Screen Shot 1](https://github.com/w4jbm/fast-recursive-fibonacci-sequence/blob/df0dd2603539e63eedf37c6240797d1ab7ef22f2/images/Screenshot_2022-10-29_10-46-33.png)

You can see that fib(15) was only called 1 time, fib(14) was called 2 times, fib(13) was called 4 times, fib(12) was called 7 times, fib(11) was called 12 times, and so on.

But wait! That is really close to a Fibonacci sequence itself. We have (from top to bottom of the fib() calls) 1, 2, 4, 7, 12, 20, 33, etc..

If we look at the Fibonacci sequence starting at the third value, we have 2, 3, 5, 8, 13, 21, 34, etc.. That part of the sequence is just 1 off from the counters for the number of times fib(x) was called.

This does break down when we get to fib(0) in the program because f(1) simply returns a value of 1 instead of trying to call fib(0) and fib(-1).

After this, I did another test run with the @cache decorator reinserted and it does exactly what you'd expect--the function is just called once for each value and then the results are cached so there are no recalculations.

![Screen Shot 2](https://github.com/w4jbm/fast-recursive-fibonacci-sequence/blob/df0dd2603539e63eedf37c6240797d1ab7ef22f2/images/Screenshot_2022-10-29_10-56-38.png)
