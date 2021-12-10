import math
import random

#Extended Euclidean  Algorithm
def extendedEuclideanAlgo(a, b):
	if a < b or (a==0 and b==0):
		return[-1, -1, -1]
	elif a%b==0:
		return [b, 0, 1]
	elif b==0:
		return [a, 1, 0]
	else:
		[g, x1, y1] = extendedEuclideanAlgo(b, a%b)
		return [g, y1, x1 - (y1*(a//b))]
		
#Function to compute e and d given phi(n)
def rsaKeys(phin, a, spCond=1):
	e, d = 0, 0
	for i in range(2,phin):
		if math.gcd(i, phin) == 1 and math.gcd(i, spCond) == 1:
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

keys1 = rsaKeys(phin, 20)			#keys of employee 1 (e1 and d1)
keys2 = rsaKeys(phin, 18, keys1[0])    		#keys of employee 2 (e2 and d2)

[e1, d1], [e2, d2] = keys1, keys2

print('n:', n, '| Phi(n)', phin, '\n')
print('e1 =', e1, '| d1 =', d1)
print('e2 =', e2, '| d2 =', d2, '\n')
print('e1*d1 mod phi(n) =', (e1*d1)%phin)
print('e2*d2 mod phi(n) =', (e2*d2)%phin, '\n')
print('gcd(e1, e2) =', math.gcd(e1, e2), '\n')

coefficients = extendedEuclideanAlgo(max(e1, e2), min(e1, e2))			#coefficients of e1 and e2 in e1*x + e2*y = 1

#Just setting values of x and y
x = (max(e1, e2) == e1)*coefficients[1] + (max(e1, e2) == e2)*coefficients[2]
y = (max(e1, e2) == e1)*coefficients[2] + (max(e1, e2) == e2)*coefficients[1]

print('In the equation e1*x + e2*y = 1:')
print('x =', x)
print('y =', y)

#Check
print('Checking e1*x + e2*y =', max(e1, e2)*coefficients[1] + min(e1, e2)*coefficients[2], '\n')

#Random message generated
message = random.randint(2, n)
print('message =', message)

E, F = pow(message, e1, n), pow(message, e2, n)
print('E =', E, '| F =', F)

messageFound = (pow(E, x, n)*pow(F, y, n))%n
print('messageFound =', messageFound)






