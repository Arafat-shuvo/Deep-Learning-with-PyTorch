
# ================================================================
# PYTHON BASICS FOR DEEP LEARNING
# Topic 01: Python Variables and Data Types
# Author: Md. Arafat Hossain
#
# Description:
# This file covers Python variables, data types, type checking,
# type conversion, variable assignment, naming rules, and
# practical programming examples.
#
# Learning Goal:
# Understand how Python stores, identifies, and processes data.
# These concepts are essential for NumPy, PyTorch, and Deep Learning.
# ================================================================


# ################################################################
# 1. VARIABLES IN PYTHON
# ################################################################

# What is a Variable?
#
# A variable is a named reference used to store and access data.
#
# Example:
# name = "Arafat"
#
# Here:
# name  -> Variable name
# =     -> Assignment operator
# "Arafat" -> Value stored in the variable
#
# Python automatically identifies the data type.
# We do not need to declare the variable type manually.

# Creating different variables

name = "Arafat"          # Stores a person's name (String)
age = 33                 # Stores age (Integer)
height = 5.8             # Stores height (Float)
is_student = True        # Stores student status (Boolean)

# Printing variable values
#
# The print() function displays information on the screen.
# We can print multiple variables using separate print statements.

print("\n1. VARIABLES IN PYTHON")
print("------------------------------")

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Expected Output:
#
# Name: Arafat
# Age: 33
# Height: 5.8
# Is Student: True


# ################################################################
# 2. PYTHON DATA TYPES
# ################################################################

# What is a Data Type?
#
# A data type defines the kind of value a variable can hold.
#
# Python has several built-in data types.
#
# Important Python Data Types:
#
# 1. int     -> Integer numbers (10, 20, 100)
# 2. float   -> Decimal numbers (10.5, 3.14)
# 3. str     -> Text data ("Python", "Deep Learning")
# 4. bool    -> Logical values (True, False)
# 5. complex -> Complex numbers (2 + 3j)
#
# Understanding data types is important because different
# operations are performed on different types of data.


# 2.1 Integer (int)
#
# Integer represents whole numbers.
# It does not contain decimal points.
#
# Examples: 10, 100, -50, 0

integer_number = 100

# 2.2 Float (float)
#
# Float represents numbers containing decimal points.
#
# Examples: 10.5, 3.14, 99.99

float_number = 10.5

# 2.3 String (str)
#
# String represents text or a sequence of characters.
# Strings are written inside single or double quotation marks.
#
# Examples: "Python", 'Machine Learning'

string_value = "Deep Learning"

# 2.4 Boolean (bool)
#
# Boolean represents only two logical values:
#
# True  -> Yes / Correct / Active
# False -> No / Incorrect / Inactive
#
# Important:
# T and F must be uppercase in True and False.

boolean_value = True

# 2.5 Complex (complex)
#
# Complex numbers contain a real part and an imaginary part.
#
# Example: 2 + 3j
#
# Here:
# 2 -> Real part
# 3j -> Imaginary part

complex_number = 2 + 3j


# Displaying all data type values

print("\n2. PYTHON DATA TYPES")
print("------------------------------")

print("Integer:", integer_number)
print("Float:", float_number)
print("String:", string_value)
print("Boolean:", boolean_value)
print("Complex:", complex_number)


# ################################################################
# 3. CHECKING DATA TYPES USING type()
# ################################################################

# What is type()?
#
# type() is a built-in Python function.
#
# It identifies the data type of a variable or value.
#
# Syntax:
# type(variable_name)
#
# Example:
# age = 25
# print(type(age))
#
# Output:
# <class 'int'>
#
# This means the variable age contains an integer value.


print("\n3. CHECKING DATA TYPES")
print("------------------------------")

# Checking the data type of each variable

print("Integer Type:", type(integer_number))
print("Float Type:", type(float_number))
print("String Type:", type(string_value))
print("Boolean Type:", type(boolean_value))
print("Complex Type:", type(complex_number))

# Expected Output:
#
# Integer Type: <class 'int'>
# Float Type: <class 'float'>
# String Type: <class 'str'>
# Boolean Type: <class 'bool'>
# Complex Type: <class 'complex'>


# ################################################################
# 4. TYPE CONVERSION
# ################################################################

# What is Type Conversion?
#
# Type conversion means changing a value from one data type
# into another data type.
#
# For example:
# Integer -> Float
# Float   -> Integer
# Integer -> String
# String  -> Integer
#
# Python provides several built-in conversion functions:
#
# int()   -> Converts compatible values into Integer
# float() -> Converts compatible values into Float
# str()   -> Converts values into String
# bool()  -> Converts values into Boolean
#
# Type conversion is frequently required when processing
# datasets and preparing numerical data for Machine Learning.


print("\n4. TYPE CONVERSION")
print("------------------------------")


# ------------------------------------------------
# 4.1 Integer to Float
# ------------------------------------------------

# Original variable contains an integer.

x = 10

# float() converts the integer into a floating-point number.

y = float(x)

print("\nInteger to Float:")
print("Original Value:", x)
print("Converted Value:", y)
print("Original Type:", type(x))
print("Converted Type:", type(y))

# Output:
# Original Value: 10
# Converted Value: 10.0
# Original Type: <class 'int'>
# Converted Type: <class 'float'>


# ------------------------------------------------
# 4.2 Float to Integer
# ------------------------------------------------

# Original value contains a decimal number.

a = 15.75

# int() removes the decimal part.
# It does not round the number to the nearest integer.
#
# Therefore:
# 15.75 becomes 15

b = int(a)

print("\nFloat to Integer:")
print("Original Value:", a)
print("Converted Value:", b)


# ------------------------------------------------
# 4.3 Integer to String
# ------------------------------------------------

# Original variable contains an integer.

number = 100

# str() converts the integer into text.
# After conversion, mathematical addition is no longer
# directly performed as numeric addition.

text = str(number)

print("\nInteger to String:")
print("Original Value:", number)
print("Converted Value:", text)
print("Converted Type:", type(text))


# ------------------------------------------------
# 4.4 String to Integer
# ------------------------------------------------

# A numeric string contains numbers written as text.

value = "500"

# int() converts the numeric string into an integer.
# Now we can perform mathematical calculations.

result = int(value)

print("\nString to Integer:")
print("Original Value:", value)
print("Converted Value:", result)
print("Calculation:", result + 100)

# Output:
# Calculation: 600


# ------------------------------------------------
# 4.5 String to Float
# ------------------------------------------------

# The value is stored as a string.

price = "99.99"

# float() converts the numeric string into a float.

converted_price = float(price)

print("\nString to Float:")
print("Original Value:", price)
print("Converted Value:", converted_price)
print("Data Type:", type(converted_price))


# ------------------------------------------------
# 4.6 Integer to Boolean
# ------------------------------------------------

# bool() converts values into True or False.
#
# Important Boolean Conversion Rules:
#
# bool(0)       -> False
# bool(1)       -> True
# bool(100)     -> True
# bool(-5)      -> True
# bool("")      -> False
# bool("Hello") -> True
#
# In general, zero and empty values are False.
# Most non-zero and non-empty values are True.

number = 1

converted_boolean = bool(number)

print("\nInteger to Boolean:")
print("Original Value:", number)
print("Converted Value:", converted_boolean)

print("bool(0):", bool(0))
print("bool(1):", bool(1))
print("bool(-5):", bool(-5))
print("bool(''):", bool(""))
print("bool('Python'):", bool("Python"))


# ################################################################
# 5. MULTIPLE VARIABLE ASSIGNMENT
# ################################################################

# Python allows us to assign multiple values to multiple
# variables in a single statement.
#
# This makes code shorter and easier to read.


print("\n5. MULTIPLE VARIABLE ASSIGNMENT")
print("------------------------------")


# ------------------------------------------------
# 5.1 Assigning Multiple Values
# ------------------------------------------------

# Three variables receive three different values.
#
# First value  -> student_name
# Second value -> student_age
# Third value  -> city

student_name, student_age, city = "Arafat", 33, "Dhaka"

print("Student Name:", student_name)
print("Student Age:", student_age)
print("City:", city)


# ------------------------------------------------
# 5.2 Assigning the Same Value
# ------------------------------------------------

# We can assign the same value to multiple variables.
#
# All three variables will contain the value 100.

a = b = c = 100

print("A:", a)
print("B:", b)
print("C:", c)


# ################################################################
# 6. VARIABLE NAMING RULES
# ################################################################

# Variable names should be meaningful and understandable.
#
# Python has some important naming rules:
#
# Rule 1:
# A variable name must start with a letter or underscore.
#
# Rule 2:
# A variable name cannot start with a number.
#
# Rule 3:
# Variable names can contain letters, numbers, and underscores.
#
# Rule 4:
# Spaces are not allowed in variable names.
#
# Rule 5:
# Python keywords cannot be used as variable names.
#
# Rule 6:
# Variable names are case-sensitive.
#
# Example:
# age and Age are two different variables.


print("\n6. VARIABLE NAMING RULES")
print("------------------------------")


# ------------------------------------------------
# 6.1 Valid Variable Names
# ------------------------------------------------

# These variable names follow Python naming rules.

first_name = "Arafat"
student_age = 25
total_marks = 450
_private_value = 100
student2 = "Rahim"

print("First Name:", first_name)
print("Student Age:", student_age)
print("Total Marks:", total_marks)
print("Private Value:", _private_value)
print("Student 2:", student2)


# ------------------------------------------------
# 6.2 Invalid Variable Names
# ------------------------------------------------

# The following names are invalid.
# They are written as comments because running them
# would produce a SyntaxError.
#
# 1name = "Arafat"
# Reason: Variable names cannot start with numbers.
#
# student-name = "Arafat"
# Reason: Hyphens are not allowed in variable names.
#
# student name = "Arafat"
# Reason: Spaces are not allowed.
#
# class = "Python"
# Reason: 'class' is a reserved Python keyword.


# ------------------------------------------------
# 6.3 Case-Sensitive Variables
# ------------------------------------------------

# Python is case-sensitive.
# Therefore, name, Name, and NAME are different variables.

name = "Arafat"
Name = "Rahim"
NAME = "Karim"

print("\nCase-Sensitive Variables:")
print("name:", name)
print("Name:", Name)
print("NAME:", NAME)


# ################################################################
# 7. PRACTICAL EXAMPLE: STUDENT INFORMATION SYSTEM
# ################################################################

# In this example, we will create a simple student profile.
#
# We will use different Python data types to store
# student information.
#
# This example demonstrates how variables are used
# in a real-world programming scenario.


print("\n7. STUDENT INFORMATION SYSTEM")
print("------------------------------")


# Student information

student_name = "Arafat"                 # String
student_id = 101                        # Integer
department = "Computer Science"         # String
cgpa = 3.56                             # Float
is_graduated = True                     # Boolean


# Displaying student information

print("Student Information")
print("------------------------------")

print("Name:", student_name)
print("Student ID:", student_id)
print("Department:", department)
print("CGPA:", cgpa)
print("Graduated:", is_graduated)


# Checking data types of student information

print("\nStudent Data Types")
print("------------------------------")

print("Name Type:", type(student_name))
print("ID Type:", type(student_id))
print("Department Type:", type(department))
print("CGPA Type:", type(cgpa))
print("Graduation Status Type:", type(is_graduated))


# ################################################################
# 8. PRACTICAL EXAMPLE: AVERAGE MARKS CALCULATOR
# ################################################################

# In this example, we will calculate the average marks
# of a student in three different subjects.
#
# Mathematical Formula:
#
# Average = Total Marks / Number of Subjects
#
# This example introduces basic numerical calculations.
# Similar calculations are used in data analysis and ML.


print("\n8. AVERAGE MARKS CALCULATOR")
print("------------------------------")


# Storing marks of three subjects

math = 85
physics = 90
chemistry = 80


# Adding all subject marks

total_marks = math + physics + chemistry

# Calculating average marks
#
# The division operator (/) returns a float value.

average_marks = total_marks / 3


# Displaying subject marks and results

print("Mathematics:", math)
print("Physics:", physics)
print("Chemistry:", chemistry)

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)


# ################################################################
# 9. BASIC PYTHON PROGRAMMING PRACTICE
# ################################################################

# This section contains small programming exercises.
#
# Try to understand each example and modify the values
# to observe how the output changes.


print("\n9. BASIC PYTHON PRACTICE")
print("------------------------------")


# ------------------------------------------------
# Exercise 1: Creating Different Variables
# ------------------------------------------------

# Create variables using different data types.

my_name = "Arafat"
my_age = 33
my_cgpa = 3.56
learning_python = True

print("\nExercise 1: Variable Creation")

print("Name:", my_name)
print("Age:", my_age)
print("CGPA:", my_cgpa)
print("Learning Python:", learning_python)


# ------------------------------------------------
# Exercise 2: Float to Integer Conversion
# ------------------------------------------------

# Convert a decimal number into an integer.

decimal_number = 25.75

# int() removes the decimal portion.

integer_result = int(decimal_number)

print("\nExercise 2: Float to Integer")

print("Original Number:", decimal_number)
print("Converted Number:", integer_result)


# ------------------------------------------------
# Exercise 3: String to Integer Conversion
# ------------------------------------------------

# Convert a numeric string into an integer.
# Then add another number to the converted value.

numeric_string = "250"

converted_number = int(numeric_string)

final_result = converted_number + 50

print("\nExercise 3: String to Integer")

print("Original String:", numeric_string)
print("Converted Number:", converted_number)
print("Final Result:", final_result)


# ------------------------------------------------
# Exercise 4: Average of Three Numbers
# ------------------------------------------------

# Store three numerical values.

num1 = 10
num2 = 20
num3 = 30

# Calculate the total of three numbers.

total = num1 + num2 + num3

# Calculate the average.

average = total / 3

print("\nExercise 4: Average Calculation")

print("Number 1:", num1)
print("Number 2:", num2)
print("Number 3:", num3)

print("Total:", total)
print("Average:", average)


# ################################################################
# 10. CONNECTION WITH DEEP LEARNING
# ################################################################

# Why are Python Variables and Data Types important in Deep Learning?
#
# Deep Learning models process numerical data.
# Python variables are used to store:
#
# 1. Input data
# 2. Model parameters
# 3. Learning rates
# 4. Batch sizes
# 5. Training epochs
# 6. Model predictions
# 7. Loss values
#
# Example:
#
# learning_rate -> Controls the model's learning step.
# epochs        -> Number of training iterations.
# batch_size    -> Number of samples processed together.
#
# These values are commonly used when training
# Neural Networks using PyTorch.


print("\n10. DEEP LEARNING EXAMPLE")
print("------------------------------")


# Model training configuration

learning_rate = 0.001
epochs = 100
batch_size = 32
number_of_classes = 10

# Displaying configuration values

print("Learning Rate:", learning_rate)
print("Epochs:", epochs)
print("Batch Size:", batch_size)
print("Number of Classes:", number_of_classes)

# Checking their data types

print("\nConfiguration Data Types")

print("Learning Rate Type:", type(learning_rate))
print("Epochs Type:", type(epochs))
print("Batch Size Type:", type(batch_size))
print("Classes Type:", type(number_of_classes))


# ################################################################
# END OF TOPIC 01
# PYTHON VARIABLES AND DATA TYPES
# ################################################################


# ================================================================
# SUMMARY:
#
# In this topic, we learned:
#
# 1. Variables in Python
# 2. Python Data Types
# 3. Checking Data Types using type()
# 4. Type Conversion
# 5. Multiple Variable Assignment
# 6. Variable Naming Rules
# 7. Student Information System
# 8. Average Marks Calculator
# 9. Basic Python Programming Practice
# 10. Connection with Deep Learning
#
# Next Topic:
# Lists, Tuples, Sets, and Dictionaries
# ================================================================
