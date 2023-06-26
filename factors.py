import sys

def factorize(n):
    factors = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            factors.append((i, n // i))
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    input_file = sys.argv[1]
    try:
        with open(input_file, 'r') as file:
            numbers = file.read().splitlines()
            for number in numbers:
                factor_pairs = factorize(int(number))
                for factor_pair in factor_pairs:
                    print(f"{number}={factor_pair[0]}*{factor_pair[1]}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

if __name__ == '__main__':
    main()

