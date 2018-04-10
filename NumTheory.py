import sys
from time import clock
from numpy import pi, exp


class NumTheory(object):

    def __init__(self, number):
        self.number = number
        if number == 1:
            self.divisors = []
            return
        if number == 0:
            self.divisors = None
            return
        primeList = NumTheory.Prime_List(number//2)
        self.divisors = [1]
        for test in primeList:
            if NumTheory.divides(test, number):
                self.divisors.append(test)
            if test > number/2 + 1:
                break
        self.divisors.append(number)

    @classmethod
    def Prime_List(cls, length):
        primeSet = [2]
        i = 3
        while True:
            prime = True
            if len(primeSet) == length:
                return primeSet
            for primes in primeSet:
                if NumTheory.divides(i, primes):
                    prime = False
                    break
                if primes >= (i)**(1/2):
                    break
            if prime is True:
                primeSet.append(i)
            i += 2

    @classmethod
    def divides(cls, a, b):
        if a < b:
            (a, b) = (b, a)
        if a/b == a//b:
            return True
        return False

    @classmethod
    def gcd(cls, a, b):
        if a < b:
            (a, b) = (b, a)
        if b == 0:
            return a
        else:
            x = a//b
            (a, b) = (b, a - x*b)
            return NumTheory.gcd(a, b)

    def Euler_Phi_Function(self):
        number = self.number
        for div in self.divisors:
            if div == 1:
                continue
            number = int(number*(1 - 1/div))
        return number

    def giveDivisors(self):
        return self.divisors

    def giveNum(self):
        return self.number

    def Sigma(self):
        return sum(self.divisors)

    def Tau(self):
        return len(self.divisors)
