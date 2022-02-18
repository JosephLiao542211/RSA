import numpy as np

def p_and_q_1(n):
    data = []
    for possiblePrime in range(2, n):
        # print('DEBUG: possiblePrime={}'.format(possiblePrime))
        isPrime = True
        for num in range (2, possiblePrime):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            # print('INFO: Prime found {}'.format(possiblePrime))
            data.append(possiblePrime)
    return tuple(data)


def p_and_q_2(n):
    data = []
    i=1
    print_num=1
    for possiblePrime in range(2, n):
        # print('DEBUG: possiblePrime={}'.format(possiblePrime))
        isPrime = True
        for num in range (2, int(possiblePrime ** 0.5)+1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            i = i + 1
            if i == print_num*10000:
                print_num = print_num +1
                print('INFO: Prime found {}'.format(possiblePrime))
            data.append(possiblePrime)
    return tuple(data)


def primesfrom2to(n):
    print('INFO: get primes between 2 and {}'.format(n))
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    result = [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
    print('INFO: Primes {}'.format(result))
    return result


def euler(p, q):
    result = (p - 1) * (q - 1)
    print('DEBUG: {}'.format(result))
    return result


def private_index(e, euler_v):
    for i in range(2, euler_v):
        if i * e % euler_v == 1:
            return i


def decipher(d, n, c):

    return c ** d % n


def main():

    e = int(input("input e: "))
    n = int(input("input n: "))
    c = int(input("input c: "))
    #9 digits max

    print('INFO: e={}, n={}, c={}'.format(e,n,c))
    p_and_q_v = p_and_q_2(n)

    euler_v = euler(p_and_q_v[0], p_and_q_v[1])

    d = private_index(e, euler_v)
    plain = decipher(d, n, c)
    print("plain: ", plain)


if __name__ == "__main__":
    main()