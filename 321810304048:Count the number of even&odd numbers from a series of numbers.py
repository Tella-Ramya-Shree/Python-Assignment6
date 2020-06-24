# Count the number of even&odd numbers from a series of numbers
series= [1,2,3,4,5,6,7,8,9,10,53,97,24]
even_count=0
odd_count = 0
for num in series: 
     if num % 2 == 0: 
       even_count += 1
     else: 
       odd_count += 1
print("Even numbers in the series:",even_count) 
print("Odd numbers in the series: ",odd_count)