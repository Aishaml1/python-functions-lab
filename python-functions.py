# Write a function named sum_to that accepts a single integer, n, and
# returns the sum of the integers from 1 to n.



def sum_to(n):
  sum = 0
  for i in range(n+1):
    sum+=i
  return sum

print(sum_to(6)) 
print(sum_to(10)) 
print(sum_to(11)) 
print(sum_to(12)) 

#Write a function named largest that takes a list of numbers as an argument and 
#returns the largest number in that list.
#max() function => returns largest number 
