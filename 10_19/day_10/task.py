#  day 10: Functions with Outputs

def format_name(f_name, l_name):
    formated_f__name = str(f_name).title()
    formated_l__name = str(l_name).title()
    return (f'{formated_f__name} {formated_l__name}')
    
    
formated_string = format_name('rafa', 'silva')
print(formated_string)


def function_1(text):
    return text + text


def function_2(text: str):
    return text.title()

output = function_2(function_1(input('Write the phrase: ')))
print(output)


"""
Leap Year
💪 This is a difficult challenge! 💪 

Write a program that returns True or False whether if a given year is a leap year.
A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice

This is how you work out whether if a particular year is a leap year. 

- on every year that is divisible by 4 with no remainder

- except every year that is evenly divisible by 100 with no remainder 

- unless the year is also divisible by 400 with no remainder   

If English is not your first language, or if the above logic is confusing, try using this flow chart.

e.g. The year 2000: 

2000 ÷ 4 = 500 (Leap)  
2000 ÷ 100 = 20 (Not Leap)  
2000 ÷ 400 = 5 (Leap!)  
So the year 2000 is a leap year. 

But the year 2100 is not a leap year because: 

2100 ÷ 4 = 525 (Leap)  
2100 ÷ 100 = 21 (Not Leap)  
2100 ÷ 400 = 5.25 (Not Leap)  

Warning

Your return should be a boolean and match the Example Output format exactly, including spelling and punctuation. 

"""
def is_leap_year(year):
    is_leap_year_bool = False
    if not year % 4 == 0:
        return is_leap_year_bool
    elif not year % 100 == 0:
        is_leap_year_bool = True
    elif not year % 400 == 0:
        return is_leap_year_bool
    else:
        is_leap_year_bool = True
        
    return is_leap_year_bool
    
print(is_leap_year(2400))
print(is_leap_year(1989))


def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))