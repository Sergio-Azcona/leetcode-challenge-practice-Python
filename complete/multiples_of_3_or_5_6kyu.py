# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
# 6 kyu - Multiples of 3 or 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
# Additionally, if the number is negative, return 0 (for languages that do have them).
# Note: If the number is a multiple of both 3 and 5, only count it once.

def solution(number):
  collection = [] #collect all relevant #s
  
#exclude numbers less than 4
  if number >= 4:
  # iterate through numbers, starting from 1 to number
    for num in range(1, number):
      #each number that is divisible by 3 or 5
      if num % 3 == 0 or num % 5 == 0:
      # added to collection
        collection.append(num)
        
  #return the sum of all digits in collection
  return sum(collection)  
    # pass
  



s1 = solution(4) # 3
s2 = solution(6) #8 
s3 = solution(16) #60
s4 = solution(3) # 0
s5 = solution(-15) #0
s6 = solution(0) #0

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)