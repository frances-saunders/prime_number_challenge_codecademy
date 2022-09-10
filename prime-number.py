#This project fulfills the reqs for the code challenge of "Prime Number Finder" in Codecademy

def prime_finder(n):
  # Write your code here
  prime_numbers = [] #sets list for prime numbers prior to n and including n
  for x in range(2, n+1): # starting at 2 since it is the first prime number
    prime = True
    for y in range(2, x): #sets loop to check number from 2 through x
      if(x % y) == 0: #if remainder is 0, equals prime
        break 
    else:
      prime_numbers.append(x)
  return prime_numbers

#test value
print(prime_finder(11))
