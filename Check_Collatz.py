from sympy import isprime, primepi, prevprime, nextprime

def check_collatz(term, k = 3):
    """Simple function to check if a number
    falls under the collatz conjecture."""
    current = term
    repeat_check = {current}
    while True:
        #print(current)
        if current % 2 == 0:
            current = current//2
        else:
            current = k*current + 1
        if current in repeat_check:
            return False
        repeat_check.add(current)
        if current == 1:
            return True
        if current > 10**1000:
            return

def check_general_collatz(term, k = 3):
    """Generaliztion proposed by 
    Zhang Zhongfu and Yang Shiming
    and found in
    http://web.mit.edu/rsi/www/pdfs/papers/2004/2004-lesjohn.pdf"""
    current = term
    repeat_check = {current}
    divisor_success = False
    while True:
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
        if current > 10**1000:
            return


if __name__ == "__main__":
    for i in range(1, 1001):
        if check_general_collatz(i, 7):
            print(i, "SUCCESS")
        else:
            pass
            #print(i, "FAILED")

    print(check_general_collatz(78, 7))
