import code

if code.fibonacci(1) == [1]:
	print("Test Case 1 Passed!")
else:
	print("Test Case 1 Failed! 1 expected [1], got", code.fibonacci(1))

if code.fibonacci(8) == [1,1,2,3,5,8,13,21]:
	print("Test Case 2 Passed!")
else:
	print("Test Case 2 Failed! 8 expected [1,1,2,3,5,8,13,21] got", code.fibonacci([1]))