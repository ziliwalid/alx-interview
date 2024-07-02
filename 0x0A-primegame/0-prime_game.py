#!/usr/bin/python3
"""
Module: Game of choosing Prime numbers
"""


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): num of rounds of game
        nums (int):  limit of range for each round
    Return:
        Name of winner (Maria or Ben)
    """
    if x == 0 or not nums:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    # Sieve of Eratosthenes to find all primes up to max_num
    for start in range(2, int(max_num ** 0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, max_num + 1, start):
                sieve[multiple] = False

    # List of primes up to max_num
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]

    def get_winner(n):
        available = set(range(1, n + 1))
        player = 0  # 0 for Maria, 1 for Ben
        
        while True:
            move_made = False
            for prime in primes:
                if prime in available:
                    move_made = True
                    multiples = {i for i in range(prime, n + 1, prime)}
                    available -= multiples
                    break
            if not move_made:
                return 1 - player  # if no move is made, the current player loses
            player = 1 - player

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = get_winner(n)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
