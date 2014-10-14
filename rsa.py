def genKey(a, b):
	try:
		p = genPrime(a, b)
		q = p
		while q == p:
			q = genPrime(a, b)
	except:
		raise ValueError

		N = p*q
		m = (p-1)*(q-1)

		e = random.randint(3, m-1)
		while gcd(e, m) != 1:
			e = random.randint(3, m-1)
		d = inverse(e, m)
	return (N, e, d)

def genPrime(min, max):
	return

def sieve(n):
"""
Generates list of all primes <= n
"""
	numList = [i for i in range(2, n+1)]
	for i in numList:
		f = range(i+i, n+1, i)
		for k in f:
			if k in numList:
				myList.remove(k)
	return numList

def isPrime(x):
	if x <= 1 or x % 2 == 0:
		return False
	else:
		for i in range(3, x**(1/2)+1):
			if x % i == 0:
				return False
	return True

def gcd(x, y):
	if y > x:
		return gcd(y, x)
	if y == 0:
		return x
	else:
		return gcd(x-y, y)

def egcd(x, y):
"""
Extended Euclid's Alogrithm
"""
	if (y > x):
		d, a, b = egcd(y, x)
		return (d, b, a)
	else:
		if y == 0:
			return (x, 1, 0)
		else:
			d, a, b = egcd(y, x%y)
			return (d, b, a - (x//y) *b)

def mod_exp(x, y, m):
"""
Finds (x^y) mod m using repeated squaring
"""
	if y == 0:
		return 1
	else:
		z = mod_exp(x, y // 2, m)
		if y % 2 == 0:
			return (z*z) % m
		else:
			return (x*z*z) % m

def inverse(x, m):
"""
Returns the multiplicative inverse of x mod m
"""
	inverse = egcd(x, m)[1]
	if inverse < 0:
		inverse += m
	return inverse