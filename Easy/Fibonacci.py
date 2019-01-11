# Naive way which is purely recursive blows up exponentially.
# Dynamic programming way remembers values of fib(N) we've already computed in the hash table.

class Solution:
    def __init__(self):
        self.valHash = {0 : 0, 1: 1}

    def fib(self, N):
        if N in self.valHash:
            return self.valHash[N]

        val = self.fib(N-1)+self.fib(N-2)
        self.valHash[N] = val
        return val

class SolutionNaive:
    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1)+self.fib(N-2)