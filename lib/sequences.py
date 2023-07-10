#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length <= 0:
        return fib_list
    else:
        fib_list.append(0)
        if length == 1:
            return fib_list
        else:
            fib_list.append(1)
            i = 2
            while i < length:
                fib_list.append(fib_list[i - 1] + fib_list[i - 2])
                i += 1
        return fib_list
