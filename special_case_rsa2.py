import math

#Function to compute e and d given phi(n)
def rsaKeys(phin, a):
	e, d = 0, 0
	for i in range(2,phin):
		if math.gcd(i, phin) == 1:
			e = e + 1
			if e == a:
				e = i
				break
	for i in range(2,phin):
		if (i*e)%phin == 1:
			d = i
			break
	return [e, d]

#Computes phi(n)
def phi(p, q):
	return (p-1)*(q-1)

p, q = 1031, 1039
n=p*q
phin = phi(p, q)
[e, d] = rsaKeys(phin, 6000)        #Try for 60, 600, 609, 6000
print('e:', e, '| d:', d, '| n:', n, '| Phi(n)', phin)

#Search for possible values of phi(n)
possiblePhi = []
for k in range(1, min(e, d)):
	if (   ( (e*d - 1)/k == (e*d - 1)//k ) and ( (e*d - 1)//k < n )   ):
		possiblePhi.append((e*d - 1)//k)
print('\nPossible values of Phi(n):', possiblePhi, '\n')

[e1, d1] = rsaKeys(phin, 191)

#finding the possible d1's wrt all the possible phi(n)'s
dPossible = set()
counter = 0
for phi in possiblePhi:
	for i in range(2, phi):
		if (i*e1)%phi == 1:
			counter = counter + 1
			dPossible.add(i)
print('Possible values of d1:', dPossible, '\n')
print('Actual value of d1:', d1, '\n')
print('#possiblePhi', len(possiblePhi), '| #counter', counter)



