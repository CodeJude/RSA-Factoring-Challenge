import sys
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def factorize(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if is_prime(i) and is_prime(n // i):
                factors.append((i, n // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: rsa <file>")
        return

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            number = int(file.read())
            factor_pairs = factorize(number)
            for factor_pair in factor_pairs:
                print(f"{number}={factor_pair[0]}*{factor_pair[1]}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == '__main__':
    main()

