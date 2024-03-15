#!/usr/bin/python3
""" Module 0-prime_game """


def SieveOfEratosthenes(n):
    """ Implements the sieve of Eratosthenes """
    primes = set()
    prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            primes.add(p)
    return primes


def roundPlay(n, primes):
    """ Implements the play for each round and returns round winner """
    maria_round_wins = 0
    ben_round_wins = 0

    if n < 2:
        ben_round_wins += 1
    else:
        remaining_numbers = set(range(2, n + 1))

        while remaining_numbers:
            # Maria's turn
            for prime in remaining_numbers:
                if prime in primes:
                    break
            # print('Maria pick = {}'.format(prime))
            # print('remaining_numbers before discard: {}'.format(
            #     remaining_numbers))
            for multiple in range(prime, n + 1, prime):
                remaining_numbers.discard(multiple)
            # print('remaining_numbers before discard: {}'.format(
            #     remaining_numbers))
            if not remaining_numbers:
                maria_round_wins += 1
                break

            # Ben's turn
            for prime in remaining_numbers:
                if prime in primes:
                    break
            # print('Ben pick = {}'.format(prime))
            # print('remaining_numbers before discard: {}'.format(
            #     remaining_numbers))
            for multiple in range(prime, n + 1, prime):
                remaining_numbers.discard(multiple)
            # print('remaining_numbers before discard: {}'.format(
            #     remaining_numbers))
            if not remaining_numbers:
                ben_round_wins += 1
                break

    # print("Maria wins: {}".format(maria_round_wins))
    # print("Ben wins: {}".format(ben_round_wins))
    # print('\n')

    if maria_round_wins > ben_round_wins:
        return "Maria"
    elif ben_round_wins > maria_round_wins:
        return "Ben"
    else:
        return None


def isWinner(x, nums):
    """ Main driver to solve the prime game. Returns the final winner """
    if not nums:  # If nums list is empty
        return None

    if all(num == 0 for num in nums):  # If all elements in nums are 0
        return "Maria"

    maria_wins = 0
    ben_wins = 0
    primes = SieveOfEratosthenes(max(nums))

    for i in range(x):
        if i < len(nums):
            # print('round: {}'.format(i))
            result = roundPlay(nums[i], primes)
            if result == 'Maria':
                maria_wins += 1
            elif result == 'Ben':
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
