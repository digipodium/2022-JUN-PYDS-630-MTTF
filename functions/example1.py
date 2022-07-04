
# creation
def si_calc():
    p = float(input("Enter the principle: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time: "))
    si = p * (r * t) / 100
    print(f'Simple Interest is {si}')

def ci_calc():
    p = float(input("Enter the principle: "))
    r = float(input("Enter the rate of interest: "))
    t = float(input("Enter the time: "))
    ci = p * (1 + r / 100) ** t
    print(f'Compound Interest is {ci}')

# calling functions
# si_calc()
# ci_calc()