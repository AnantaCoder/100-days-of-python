'''Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

You are going to create a list called result which contains the numbers that are common in both files. '''

with open(r'Days\Intermediate\day-26 List comprehension & NATO\file1.txt') as x:
    contentsx = x.read().split()
    numbers_x = [int(i) for i in contentsx]
with open(r'Days\Intermediate\day-26 List comprehension & NATO\file2.txt') as y:
    contentsy = y.read().split()
    numbers_y = [int(i) for i in contentsy]

result = [x for x in numbers_x if x in numbers_y ]
print(result)


''' Alternate
with open("file1.txt") as file1:
  list1 = file1.readlines()
    
with open("file2.txt") as file2:
  list2 = file2.readlines()
    
result = [int(num) for num in list1 if num in list2]
 
print(result)
'''