def gen_primes(limit):
    for number in range(limit):
        if is_prime(number):
            yield number


class Primes:
    def __init__(self):
        self.start = 2

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        last_head = self.current
        self.current = get_next_prime(last_head)
        return last_head


def get_next_prime(last_prime):
    """ :return the smallest prime number greater than the parameter """
    next_prime = last_prime + 1
    while not is_prime(next_prime):
        next_prime += 1
    return next_prime


def is_prime(n):
    if (n < 2):
        return False
    d = 2
    while d * d <= n:
        if (n % d) == 0:
            return False
        d = d + 1
    return True


def sum_primes(a, b):
    accum = 0
    for x in range(a, b + 1):
        if is_prime(x):
            accum += x
    return accum


def list_map(f, L):
    """ Implement map(f, L) where f is a function
        and L is a list by constructing a list """
    return [f(x) for x in L]


def square(x):
    return x * x


if __name__ == "__main__":
    primes = iter(Primes())
    print("Using an iterator...")
    for i in range(5):
        print("The next prime number is: {}.".format(next(primes)))

    upper_limit = 13
    yielding_generator = gen_primes(upper_limit)
    print("Using a yielding prime number generator...")
    print("The primes smaller than {} are: \t\t{}".format(upper_limit, list(yielding_generator)))

    primes = iter(Primes())
    n_primes = []
    for _ in range(5):
        next_prime = next(primes)
        n_primes.append(next_prime)

    assert(isinstance(n_primes, list))

    print("Applying n_primes to list_map and got: \t{}".format(list_map(square, n_primes)))
