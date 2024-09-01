# Subscripting
print('Hello'[0])

# Negative start in the end of string
print('Hello'[-1])

# Type string don't calculate
print('12' + "15")

# Integer = Whole Number
print(12 + 15)

# Large Integers - To humans visualize better, use _
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# Len don't work to Integer type, only String types

# To discover the type of variable
print(type("Hello"))
print(type(6))
print(type(6.5))
print(type(True))

# Convert types
print(type(int("123")))
# float()
# bool()
# str()


# Calculator basic operations
multiplication_result = 2 * 8
division_result = 10 / 2
addition_result =  8 + 10
subtraction_result = 10 - 5

# Mathematic rules, multiplication and division first
print(3 * 3 + 3 / 3 - 3)


# Simplified Exercise 16
bmi = 84 / 1.65 ** 2
print(bmi)

# Rounded the number
print(round(bmi, 2)) 

# Manipulate value on number
score = 0
score += 1
score *= 4
score -= 2

# Concatenate strings with numbers
print(f"Your score is = {score}")