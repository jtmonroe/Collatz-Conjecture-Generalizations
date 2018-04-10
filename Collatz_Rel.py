from Check_Collatz import *
from NumTheory import NumTheory

def check_paths_compare(a, b, k=3):
    if a in general_collatz_orbit(b, k):
        return True
    if b in general_collatz_orbit(a, k):
        return True
    return False

def stopping_times_compare(a,k=3):
    val = NumTheory(a)


def main():
    print(general_collatz_orbit(3))
    print(general_collatz_orbit(15))
    print(check_paths_compare(3, 15))

main()