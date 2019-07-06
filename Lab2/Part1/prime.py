# def gen_primes(limit):
#     for number in range(limit):
#         if is_prime(number):
#             yield number


# class Primes:
#     def __init__(self):
#         self.start = 2

#     def __iter__(self):
#         self.current = self.start
#         return self

#     def __next__(self):
#         last_head = self.current
#         self.current = get_next_prime(last_head)
#         return last_head


# def get_next_prime(last_prime):
#     """ :return the smallest prime number greater than the parameter """
#     next_prime = last_prime + 1
#     while not is_prime(next_prime):
#         next_prime += 1
#     return next_prime


class Primes:
    def __init__(self):
        self.prime_list = [2]
        self.v = 3

    def gen_primes(self):
        yield 2
        while True:
            # check the numbers in prime list only
            for i in self.prime_list:
                if self.v % i == 0:
                    break
                elif i * i > self.v + 1:
                    yield self.v
                    self.prime_list.append(self.v)
                    break
            else:
                self.prime_list.append(self.v)
                yield self.v
            # check odd numbers only
            self.v += 2

      
def is_prime(n):
    if (n < 2):
        return False
    d = 2
    while d * d <= n:
        if (n % d) == 0:
            return False
        d = d + 1
    return True


def primes(a, b):
  for p in range(a, b + 1):
    if is_prime(p):
      yield p

    
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


def yield_map(f, L):
    """ Implement map(f, L) where f is a function
        and L is a list by using yield """
    for x in L:
        yield f(x)


class IterMap:
    """ Implement map(f, L) where f is a function
        and L is a list by creating an iterator object """

    def __init__(self, f, L):
        self.index = 0
        self.f = f
        self.L = L

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.L):
            self.c = self.L[self.index]
            self.index += 1
            return self.f(self.c)
        
        else:
            raise StopIteration

def square(x):
    return x * x


if __name__ == "__main__":

    primes = Primes().gen_primes()

    start, stop = 10, 2000
    n_primes = []

    for n in primes:
        if n > start and n < stop:
            n_primes.append(n)
        elif n > stop:
            break

    print("Using a yielding prime number generator...")
    print("The primes from {} to {} are: \t\t{}".format(start, stop, n_primes))

    print("Applying n_primes to list_map and got: \t\t{}".format(list_map(square, n_primes)))
    print("Applying n_primes to yield_map and got: \t{}".format(list(yield_map(square, n_primes))))
    print("Applying n_primes to IterMap and got: \t\t{}".format(list(IterMap(square, n_primes))))
