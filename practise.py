# Write a Python program that takes a list of numbers as input and 
# outputs the second largest number in the list using
# conditional statements and a for loop.

def second_largest(num):
      
    second = sorted(num)
    for n in second:
        if len(second)<1:
            return n
        else:
            new = max(second)
            return (second[-2])
          
       
num = [20,10,40,56,12,8,100]
print(second_largest(num))



# Write a Python program that takes a string as input and checks if it is a palindrome 
# (reads the same forwards and backwards), 
# ignoring spaces and punctuation.

def palindrome(name):
    if name== name[::-1]:
        return True
    else:
        return False
print(palindrome("dad"))

# Write a Python program that takes a list of numbers 
# as input and outputs the median of the numbers 

def median(numbers):
   sorted_list = sorted(numbers)
   mid = len(sorted_list) // 2
   if len(sorted_list) % 2 == 1:
        return sorted_list[mid]
   else:
        return (sorted_list[mid- 1] + sorted_list[mid]) / 2
   
numbers = [20, 30, 90, 20, 3, 44, 50, 12]
print(median(numbers))





# Write a Python program that takes a year as input and determines if it is a leap year.

def find_leap_year(year):
    if(year % 4==0):
        return f"{year} is a leapyear"
    else:
        return year
print(find_leap_year(year=2024))














