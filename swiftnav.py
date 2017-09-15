import sys
import collections
import math

#To make future primality checks faster, prime numbers that are calculated are stored in a class dictionary
class fibonacci:
	prime_dict = collections.defaultdict(bool)
	
	#using this function because xrange will throw an OverflowError for large numbers
	def mrange(self, start, stop, step):
	    while start < stop:
	        yield start
	        start += step

	def get_fibonacci_nums(self, n):
		a = 1
		b = 1
		if n<=0: return
		elif n==1: print a
		elif n==2: print a, b
		else:
			print a
			print b 
			c = a+b
			for i in range(2,n):
				if c==2: print "BuzzFizz" #2 is prime
				elif c%2==0: print c #If fibonacci number is even, then we know its not prime
				elif c%15==0: print "FizzBuzz"
				elif c%3==0: print "Buzz"
				elif c%5==0: print "Fizz"
				elif self.isPrime(c): print "BuzzFizz"
				else: print c
				a = b
				b = c
				c = a+b

	#Only check odds from 7 to the square root of n. Even's, multiples of 3, 5, and 15 are accounted for in fibonacci_ method
	def isPrime(self, n):
		if n in fibonacci.prime_dict: return fibonacci.prime_dict[n]
		else:
			for i in self.mrange(7, int(math.sqrt(n)) + 1, 2):
				if n%i==0: 
					fibonacci.prime_dict[n] = False
					return False 
			fibonacci.prime_dict[n] = True
			return True


user_n = sys.argv[1]
fib = fibonacci()
fib.get_fibonacci_nums(int(user_n))
