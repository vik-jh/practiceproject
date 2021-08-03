# Part-1: Find the factorial of a given number
def factorial(n):
    if n == 0:
        return 1
    if n < 0:
        return 
    
    return n * factorial(n-1)

def factorialTrailingZeros(n):

    #fact = factorial(n)
    #8print(fact)

    count = 0

    i = 5

    while(n//i != 0):
        count = count + int(n/i)
        i = i*5
    return count
    
   # while (fact%10 == 0):
    #    count = count + 1
     #   fact = fact/10
    return count




n = int(input("Enter the number to find its factorial: \n"))

ans = factorial(n)
print(ans)
print(factorialTrailingZeros(n))

# Part-2: Find the number of trailing zeros in that factorial





