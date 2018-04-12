from Check_Collatz import *
from NumTheory import NumTheory

def check_paths_compare(a, b, k=3):
    if a in general_collatz_orbit(b, k):
        return True
    if b in general_collatz_orbit(a, k):
        return True
    return False

def check_all_divisors_paths(a,k=3):
    val = NumTheory(a)
    divisors = val.giveDivisors()
    div_dict = {}
    for div in divisors:
        if check_paths_compare(a, div, k):
            div_dict[div] = True
        else:
            div_dict[div] = False
    return div_dict

def check_prime_converge_one_iteration(K = 3, N = 200):
    N = 200
    K = 7
    Success_Set = []
    Fail_Set = []
    primeList = NumTheory.Prime_List(N)
    for prime in primeList:
        val = NumTheory(general_collatz_single_iteration(prime, k = K))
        valDivisors = val.giveDivisors()
        fail = False
        for div in valDivisors[:len(valDivisors) - 1]:
            if div > K:
                Fail_Set.append(prime)
                fail = True
                break
        if not fail:
            Success_Set.append(prime)
    return [Success_Set, Fail_Set]
