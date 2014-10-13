def generateKey(a, b, k=7):

	try:

		p = gen_prime(a, b)
		q = p
		while q == p:
			q = gen_prime(a, b)
	except:
		raise ValueError

		N = p*q
		m = (p-1)*(q-1)

		e = random.randint(3, m-1)
		while gcd(e, m) != 1:
			e = random.randint(3, m-1)
		d = inverse(e, m)

	return (N, e, d)