def genKey(a, b, k=7):
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