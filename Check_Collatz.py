from sympy import isprime, primepi, prevprime, nextprime
from math import inf


def check_general_collatz(term, k = 3, upper_bound = 10**10000):
    """Generaliztion proposed by 
    Zhang Zhongfu and Yang Shiming
    and found in
    http://web.mit.edu/rsi/www/pdfs/papers/2004/2004-lesjohn.pdf"""
    current = term
    repeat_check = {current}
    while True:
        divisor_success = False
        p = k
        while True:
            try:
                p = prevprime(p)
            except:
                break
            if current % p == 0:
                divisor_success = True
                current = current//p
        if not divisor_success:
            current = k*current + 1
        if current in repeat_check:
            return False
        repeat_check.add(current)
        if current == 1:
            return True
        if current > upper_bound:
            return None

def general_collatz_single_iteration(term, k = 3):
    current = term
    divisor_success = False
    p = k
    while True:
        try:
            p = prevprime(p)
        except:
            break
        if current % p == 0:
            divisor_success = True
            current = current//p
    if not divisor_success:
        current = k*current + 1
    return current


def general_collatz_orbit(term, k = 3, upper_bound = 10**10000):
    """Generaliztion proposed by 
    Zhang Zhongfu and Yang Shiming
    and found in
    http://web.mit.edu/rsi/www/pdfs/papers/2004/2004-lesjohn.pdf
    Returns a list of numbers in the collatz
    tree from term -> 1, the cycle, or the terms less than the upper bound
    Simple check for each through last term
    if convergent: last term = 1
    if cycle: last term = first term
    if violate upper bound: last term is inf"""
    current = term
    orbit = [current]
    while True:
        divisor_success = False
        p = k
        while True:
            try:
                p = prevprime(p)
            except:
                break
            if current % p == 0:
                divisor_success = True
                current = current//p
        if not divisor_success:
            current = k*current + 1
        if current in orbit:
            orbit.append(current)
            return orbit
        orbit.append(current)
        if current == 1:
            return orbit
        if current > upper_bound:
            orbit.append(inf)
            return orbit


def total_stopping_time(term, k = 3, upper_bound = 10**10000):
    orbit = general_collatz_orbit(term, k, upper_bound)
    if orbit[len(orbit) - 1] != inf and orbit[len(orbit) - 1] != orbit[0]:
        return len(orbit)
    return inf


def check_range(start, end, k = 3):
    collatz_dict = {}
    for i in range(start, end + 1):
        collatz_dict[i] = check_general_collatz(i, k)
    return collatz_dict
