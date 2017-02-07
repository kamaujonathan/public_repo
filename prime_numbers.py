n=8
def check_prime_numbers(n): #function to check for prime numbers between 0 and n
        
        for x in range(0,n+1): #the time complexity here can be denoted by 0(n)
                if x > 0: 
                        for i in range(2,x):
                                if (x % i) == 0:
                                        break
                                else:
                                        print(x)
                                        break
        

print check_prime_numbers(n)
