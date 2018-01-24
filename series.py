def fibonnacci(n):
	""" recursive solution to fibonnacci"""
	if n == 0:
		return 0
	if n == 1:
		return 1
	
	return fibonnacci(n-2) + fibonnacci(n-1)

def lucas(n):
	""" 2 if n == 0
		1 if n == 1
		L n-1 + L n-2 if n > 1
	"""
	if n == 0:
		return 2
	if n == 1:
		return 1
	
	return lucas(n - 1) + lucas(n - 2)
	
def sum_series(n, x=0, y=0):
	if x ==2 and y == 1:
		return lucas(n)
	else:
		return fibonnacci(n)
	
	

if __name__ == "__main__":
	print (fibonnacci(3))
	print (lucas(2))


	
