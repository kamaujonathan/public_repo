def fizz_buzz(r):
    if (r % 5 == 0 and r % 3 == 0):
        return 'FizzBuzz'
    elif (r % 3 == 0 and r % 5 != 0):
        return 'Fizz'
    elif(r % 5 == 0 and r % 3 != 0):
        return 'Buzz'
    else:
        return r
