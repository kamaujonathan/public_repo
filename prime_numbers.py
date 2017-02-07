n=8
def check_prime_numbers(n):
        
        for x in range(0,n+1):
                if x > 0:
                        for i in range(2,x):
                                if (x % i) == 0:
                                        break
                                else:
                                        print(x)
                                        break
        

print check_prime_numbers(n)
