import math
import sys

continued_fractions = []

class AttackHandler:
    def __init__(self, e, N):
        self.e = e
        self.n = N

    def finish_recursion(self, x, y):
        return x / y

    def compute_continued_fractions(self, x, y):
        count = x / y
        remainder = x % y
        continued_fractions.append(count)
        if remainder == 1:
            continued_fractions.append(self.finish_recursion(y,remainder))

        else:
            self.compute_continued_fractions(y, remainder)

    def compute_convergents(self, cont_frac):
        res_num = list([cont_frac[0], cont_frac[1]*cont_frac[0]+1])
        res_denom = list([1, cont_frac[1]])

        for i in range(2, len(cont_frac)):
            res_num.append(cont_frac[i]*res_num[i-1]+res_num[i-2])
            res_denom.append(cont_frac[i]*res_denom[i-1]+res_denom[i-2])

        for i in range(0, len(res_num)):
            num = res_num[i]
            denom = res_denom[i]
            print(f"Convergent found: {num}/{denom}")

        return res_num, res_denom

    def compute_euler_totient(self, e, numerators, denominators):
        totient_vals = []
        for i in range(0, len(numerators)):
            if numerators[i] == 0:
                continue

            phi = (int(e)*denominators[i]-1)/numerators[i]
            print(f"Recovered possible phi value: {phi}")
            totient_vals.append(phi)

        return totient_vals

    def find_roots(self, totients, N):
        for i in range(0, len(totients)):
            a = 1
            b = ((int(N)-totients[i])+1)
            c = int(N)
            dis = b*b-4*a*c
            sqrt_val = math.sqrt(abs(dis))

            if dis > 0:
                p = int((b+sqrt_val)/(2*a))
                q = int((b-sqrt_val)/(2*a))
                print(f"Recovered values {p}, {q} for p and q")

if __name__ == '__main__':
    sys.stackrecursionsize = 1000
    e = input("Enter value for e: ")
    N = input("Enter value for N: ")
    wiener = AttackHandler(int(e), int(N))
    wiener.compute_continued_fractions(wiener.e, wiener.n)

    for x in range(0, len(continued_fractions)):
        continued_fractions[x] = math.floor(continued_fractions[x])
    
    print("Computed continued fraction: ", continued_fractions)
    res_num, res_denom = wiener.compute_convergents(continued_fractions)
    totient_vals = wiener.compute_euler_totient(e, res_num, res_denom)
    wiener.find_roots(totient_vals, N)