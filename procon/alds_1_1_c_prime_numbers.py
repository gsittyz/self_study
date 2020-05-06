import math


def is_prime(n):
    if n == 2:
        return 1
    if n == 1 or n % 2 == 0:
        return 0

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return 0
    return 1


def main():
    num_el = int(input())
    nums = [int(input()) for i in range(num_el)]
    are_primes = [is_prime(num) for num in nums]
    print(sum(are_primes))


if __name__ == "__main__":
    main()
