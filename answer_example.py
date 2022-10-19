def fibonacci(n): #a function that gives the fibonacci series and n determines how many number of the series it will give
	if n < 0: # n is less than 0 cant happen
		raise ValueError("Negative length list is invalid") #error 
	if n == 0:# n is equal to 0 = no list
		return [] # empty list
	if n == 1: #n is equal to 1 
		return [1] # give the first term of the fibonnaci series
	list = [1,1] # the first two term of fibonaci series 
	for i in range(2,n): # i starting at 2 to n i help add to the list with the equation below
		list.append(list[i-1] + list[i-2]) #add to list (the prior term adding to the current term) Example i=2 add term1+term0 i=3 add term2+term1
	return list #return the new list