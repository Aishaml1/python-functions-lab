# Write a function named sum_to that accepts a single integer, n, and
# returns the sum of the integers from 1 to n.



def sum_to(n):
  sum = 0
  for i in range(1, n + 1):
    sum+=i
  return sum

print(sum_to(6)) 
print(sum_to(10)) 


#Write a function named largest that takes a list of numbers as an argument and 
#returns the largest number in that list.
#max() function => returns largest number 
def largest(li):
    max = li[0]
    for x in li:
        if x > max:
            max = x
    return max
print(largest([1, 2, 3, 4, 0])) # returns 4
print (largest([10, 4, 2, 231, 91, 54]))  # returns 231