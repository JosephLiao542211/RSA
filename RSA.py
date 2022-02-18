import os
import math
import Second
import random
import numpy as np
import matplotlib as mp

#Creating RSA Private and Public Key

lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
             67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
             157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
             251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349,
             353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
             457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
             571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
             673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
             797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
             911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

arr = np.genfromtxt('primes-to-100k.txt')
primes = np.array(np.split(arr, arr.size/4))


def encrypt(e,n):
    print("Encrypting Message")
    c = 65**3 % n
    print(c)


def genrateKey(keySize):
    p = int(input("Enter first prime: "))      #lowPrimes[22]
    q = int(input("Enter second prime: "))       #lowPrimes[23]
    n = p*q
    print("Finished Generating p,q,n",p, q, n)
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if Second.gcd(e, (p - 1) * (q - 1)) == 1:
            break
    print("Finihsed Generating e, relative prime number",e)
    d = Second.findModInverse(e,(p-1)*(q-1))

    publicKey=(n, e)

    privateKey=(n, d)

    print("Public Key: ", publicKey, "Private Key:", privateKey)
    encrypt(e, n)
    return publicKey, privateKey





genrateKey(10)

