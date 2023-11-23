import random
# Random Numbers for Addition
addend1 = random.randint(1, 99)
addend2 = random.randint(1, 99)

# Display of Questions
print("What is", addend1, "+", addend2, "?")
sum = int(input(">> "))
print(addend1, "+", addend2, "=", sum)

# Conditional Statement
if sum == addend1 + addend2:
    print("Your answer is correct!")
else:
    print("Your answer is wrong!")
    print("The correct answer is", addend1 + addend2)
print()


# Random Numbers for Subtraction
minuend = random.randint(1, 99)
subtrahend = random.randint(1, 99)

# Display of Questions
print("What is", minuend, "-", subtrahend, "?")
difference = int(input(">> "))
print(minuend, "-", subtrahend, "=", difference)

# Conditional Statement
if difference == minuend - subtrahend:
    print("Your answer is correct!")
else:
    print("Your answer is wrong!")
    print("The correct answer is", minuend - subtrahend)
print()


# Random Numbers for Multiplication
factor1 = random.randint(1, 99)
factor2 = random.randint(1, 99)

# Display of Questions
print("What is", factor1, "x", factor2, "?")
product = int(input(">> "))
print(factor1, "x", factor2, "=", product)

# Conditional Statement
if product == factor1 * factor2:
    print("Your answer is correct!")
else:
    print("Your answer is wrong!")
    print("The correct answer is", factor1 * factor2)
print()


# Random Numbers for Division
dividend = random.randint(1, 99)
divisor = random.randint(1, 99)

# Display of Questions
print("What is", dividend, "/", divisor, "?")
quotient = int(input(">> "))
print(dividend, "/", divisor, "=", quotient)

# Conditional Statement
if quotient == dividend / divisor:
    print("Your answer is correct!")
else:
    print("Your answer is wrong!")
    print("The correct answer is", dividend / divisor)
print()
