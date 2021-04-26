"""
shell.py

Author: Aamir Zainulabadeen

A simple program showcasing basic python syntax.
"""
import argparse

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def get_fib_memoized():
    d = {}
    def fib_memoized(n):
        if n in d:
            return d[n]
        else:
            d[n] = fib(n)
            return d[n]
    return fib_memoized

def computePrintFib(n, foo):
    print(f"The {n}th fibonacci number is {foo(n)}")

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("--n", type=int, help="Position in fibonacci sequence.")
   parser.add_argument("--nlist", type=str, help="A list of integers. Usage: --nlist=1,2,3,4,5,6")


   args = parser.parse_args()

   # --n=0 is valid
   if args.n is not None:
       n = args.n
       computePrintFib(n, fib)

   if args.nlist:
       fib_m = get_fib_memoized()
       nlist = [int(i) for i in args.nlist.split(",")]
       print("Parsed input is: ", nlist)
       for i in nlist:
           computePrintFib(i, fib_m)

if __name__=='__main__':
    main()
