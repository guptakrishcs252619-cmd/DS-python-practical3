# Write a python code to create Numpy Array. 
import numpy
print("krish gupta 085")
arr = numpy.array([1, 2, 3, 4, 5])

print(arr)

#Write a python code to demonstrate basic operations on single array.
from array import *
print("krish gupta 085")
a = array('i', [10, 20, 30])

print(a)      
print(a[0])   

a.append(40)  
a.remove(20)  

print(a)

 #Write a python code to create array with 10 elements and slice
from array import *

arr = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:", arr)

print("Sliced Elements (1st to 5th):"), arr[0:5]
print("krish gupta 085")


#Write a python code to sort an array alphabetically
from array import *

arr = array('i', [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:", arr)

print("Sliced Elements (1st to 5th):", arr[0:5])
print("krish gupta 085")


 #Write a python code to create a filter array that will return maximum values from an array.
from array import *

arr = array('i', [15, 45, 22, 89, 67, 12, 90, 34, 56, 78])

max_value = max(arr)

filter_array = [x for x in arr if x == max_value]

print("Original Array:", arr)
print("Maximum Value:", max_value)
print("Filter Array:", filter_array)
print("krish gupta 085")
