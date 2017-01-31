import math

prime_list = [2, 3, 5, 7]


def nextNumber(number=prime_list[-1]):
    return max(prime_list[-1], number) + 2


def nPrime(N):
    global prime_list
    if len(prime_list) >= N:
        # already calculated earlier
        yield prime_list[N - 1]
    number = nextNumber()
    counter = len(prime_list)
    while counter < N:
        for prime in prime_list:
            if prime > math.sqrt(number):
                # No need to check next, no factor available
                prime_list.append(number)
                counter += 1
                yield number
                break
            elif number % prime == 0:
                # Not a prime, factors available
                break
            else:
                # Continue to check the divisiblity with next big prime no from
                # already available list
                continue
        # look for next number
        number = nextNumber(number)


def primeTillN(N):
    global prime_list
    for prime in prime_list:
        if prime > N:
            break
        # already calculated earlier
        yield prime
    number = nextNumber()
    while number < N:
        for prime in prime_list:
            if prime > math.sqrt(number):
                # No need to check next, no factor available
                prime_list.append(number)
                yield number
                break
            elif number % prime == 0:
                # Not a prime, factors available
                break
            else:
                # Continue to check the divisiblity with next big prime no from
                # already available list
                continue
        # look for next number
        number = nextNumber(number)

if __name__ == '__main__':
    import sys
    try:
        N = int(sys.argv[1])
    except IndexError:
        N = input("Enter value of N : ")
    count = 0
    for i in primeTillN(N):
        # print i
        count += 1
    print "Count : %d\nBiggest Prime : %d" % (count, prime_list[-1])
