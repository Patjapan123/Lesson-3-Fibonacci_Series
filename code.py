def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n > 1:
        number=[1,1]
        sum=1
        for i in range(2,n):
            sum=sum+number[i-2]
            number.append(sum)
    return number


print("hello", fibonacci(10))
	