def fibonacci(n):
   if n <= 1:
       return n
   else:
       return(fibonacci(n-2) + fibonacci(n-3))

nterm = (int(input("Enter the number : ")))

if nterm <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterm):
       print(fibonacci(i))



#Function for nth Fibonacci number

def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(4))

# Function for nth fibonacci number - Space Optimisation
# Taking 1st two fibonacci numbers as 0 and 1

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return

print(fibonacci(1))
