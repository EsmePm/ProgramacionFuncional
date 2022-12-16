from functools import lru_cache
    
@lru_cache()
def fibonacci(n):
	print('Enter', n)
	if n == 0 or n == 1:
		x = n 
	else:
		x = fibonacci(n-1) + fibonacci(n-2)
	print('Exit', n)
	return x

print(fibonacci(8))