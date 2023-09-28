#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Monday Lesson (variable assignment, loops, lists)

# ## Tasks Today:
# 
# 1) Int & Float assignments <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Assigning int <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Assigning float <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Performing Calculations on ints and floats <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Addition <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Subtraction <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Multiplication <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Floor Division <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Modulo <br>
#  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - Exponential <br>
# 2) String Input-Output <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) String Assignment <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) print() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) String Concatenation <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Type Conversion <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) input() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) format() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) Old Way (python 2) <br>
# 3) <b>In-Class Exercise #1</b> <br>
# 4) If Statements <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) 'is' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) 'not in' keyword <br>
# 5) <b>In-Class Exercise #2</b> <br>
# 6) Elif Statements <br>
# 7) Else Statements <br>
# 8) <b>In-Class Exercise #3</b> <br>
# 9) For Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Using 'in' keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Continue Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Break Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Pass Statement <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Double For Loops <br>
# 10) While Loops <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Looping 'While True' <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) While and For Loops Used Together <br>
# 11) Built-In Functions <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) range() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) len() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) help() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) isinstance() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) abs() <br>
# 12) Try and Except <br>
# 13) Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Declaring Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Indexing a List <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) .append() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) .insert() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) .pop() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) .remove() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; g) del() <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; h) Concatenating Two Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; i) Lists Within Lists <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; j) Looping Through Lists <br>

# ### Int & Float Assignments

# ##### Assigning int

# In[2]:


number = 6

print(number)


# ##### Assinging float

# In[5]:


numberFloat = 2.3
print(numberFloat)
print(numberFloat)
numberFloat = 7.2
print(numberFloat)


# #### Performing Calculations on ints and floats

# ##### Addition

# In[7]:


num1 = 2
num2 = 5.4

result = num1 + num2

print(result)

# result += 2
print(result + 2)


# ##### Subtraction

# In[10]:


result_diff = num2 - num1
print(result_diff)

result_diff -= 1
print(result_diff - 1)


# ##### Multiplication

# In[11]:


result_mul = num1 * num2
print(result_mul)

result_mul *= 2
print(result_mul)


# ##### Division

# In[14]:


result_div = num2/num1
print(result_div)

result_div /= 3
print(result_div)


# ##### Floor Division

# In[16]:


# rounds the dividend down

result_floor = num2 // num1
print(result_floor)

result_floor //= 2
print(result_floor)


# ##### Modulo

# In[18]:


# gives the remainder after dividend is calculated to the ones place

result_mod = num2 % num1
print(result_mod)

result_mod %= 2
print(result_mod)


# ##### Exponential

# In[19]:


square = 5 ** 2
print(square)

square **= 2
print(square)


# ### String Input-Output

# ##### String Assignment

# In[21]:


name = "Brandon"
print(name)


# ##### print() <br>
# <p>Don't forget about end=' '</p>

# In[24]:


print("This is my first name:", name)

print("Full Name:", name, end=" Apol")


# ##### String Concatenation

# In[28]:


first_name = "John"
last_name = "Smith"

full_name = first_name + " " + last_name
print(full_name)

full_name += ", Jr"
print(full_name)


# ##### Type Conversion

# In[29]:


number = "32"

change_type_num = int(number)
print(number)
print(change_type_num + 1)


# ##### input()

# In[33]:


# input will always returns a string

# name = input("What is your name? ")
# print("Nice to meet you, " + name)

age = int(input("What is your age?: "))
add_age = age + 5
print(add_age)


# ##### format()

# In[34]:


age = input("What is your age? ")

result_string = "You are {} {} and you are getting wiser!".format (age, name)
print(result_string)

result_again = f"{age} is age a great time in life!!!"
print(result_again)


# ##### Old Way (python 2)

# In[35]:


result_string2 = "You are %s and you look great for your age!" %age
print(result_string2)


# # In-Class Exercise 1 <br>
# <p>Create a format statement that asks for color, year, make, model and prints out the results</p>

# In[36]:


name = input("What is your name? ")
color = input("What color is your car? ")
year = input("What year is your car? ")
model = input("What make and model is your car? ")
print(name + ", your car is a " + color + ", " + year + " " + model + ".")


# ### If Statements

# In[40]:


# Available operators: Greater(>), Less(<),Equal(==)
# Greater or Equal(>=), Less or Equal (<=)

# Truth Tree:
# T && F = F
# T && T = T
# T || F = T
# F || T = T
# F || F = F

num1 = 5
num2 = 10
num3 = 1

# if num1 == num2:
#     print( 'Equal Values')
# else:
#     print('Not Equal')

if num2 >= num1:
    print("Num2 is greater")
elif num1 > num2:
    print("Num1 is greater")
else:
    print("Equal values")
    
if num2 < num1 or num3 > 0:
    print("This ran!")
else: 
    print("You are here")


# ##### 'is' keyword

# In[41]:


# The "is" keyword is for checking for the same object, but not the same value

num3 = 55

if num3 is 55:
    print("This is the exact number/object")


# ##### 'in' keyword

# In[42]:


# Check if a character is in a string

char_name = "Frodo Baggins"

if "Frodo" in char_name:
    print("The ring bearer")
    


# ##### 'not in' keyword'

# In[43]:


sega_char = "Sonic"

if 'a' not in sega_char:
    print('a is NOT here...')


# # In-Class Exercise 2 <br>
# <p>Ask user for input, check to see if the letter 'p' is in the input</p>

# In[37]:


p_here = input("What is your pet's name? ")
if 'p' in p_here:
    print("There's pee in here.")
else:
    print("No pee in here.")


# ## Using 'and'/'or' with If Statements

# In[3]:


num_11 = 15
num_12 = 3
num_13 = 10
num_14 = 3

# if with 'and' statement
if num_11 / 5 == num_12 and num_13 - 7 == num_14:
    print ("True and True")
    
# If with 'or' statement
if num_11 > num_12 or num_13 == num_14:
    print('True and False')


# ### Elif Statements

# In[7]:


first_name = input('What is your name? ')

if first_name == 'Smith':
    print('The name is Smith.')
elif first_name == 'Brandon':
    print('The name is Brandon')
elif first_name != 'Max':
    print('The name is NOT Max')
else:
    print('The name is Max')


# ### Else Statements

# In[ ]:


# see above


# ### For Loops

# In[8]:


# Syntax:
# for counter condition

name = 'Brandon Apol'

for letter in name:
    print(letter)


# ##### Using 'in' keyword

# In[ ]:


# see above


# ##### Continue Statement

# In[ ]:


# will continue to next iteration; don't do anything this time, just move on to the next number in the range(or whatever)


# In[10]:


for i in range(20):
    if i == 5:
        continue
    print(i)


# ##### Break Statement

# In[ ]:


# will break out of current loop


# In[11]:


for i in range(20):
    if i == 5:
        break
    print(i)


# ##### Pass Statement

# In[ ]:


# mostly used as a placeholder, and will continue on same iteration


# In[12]:


for i in name:
    pass


# ##### Double For Loops

# In[13]:


for i in range(5):
    for j in range(5):
        print('i = ', i, 'j = ', j)


# ### While Loops

# In[14]:


# continue happening as long as something is true
# syntax:
# while keyword, condition statement

num = 0

while num < 10:
    print(num)
    num += 1


# ##### Looping 'While True'

# In[16]:


game_over = True

while game_over:
    print('Infinite Loop')
    user_input = input('Would you like to stop? ')
    if user_input == 'Yes':
        game_over = False


# ##### While & For Loops Used Together

# In[17]:


num = 0

while num < 5:
    print('\n While loop iteration: ' + str(num))
    
    for i in range(2):
        print('For loop iteration: ', str(i))
    
    num += 1


# ### Built-In Functions

# ##### range()

# In[19]:


# range(Start, Stop, Step) (default=0, what is written in parenthesis, default=1)

for i in range(1, 20, 2):
    print(i)


# ##### len()

# In[22]:


name = input("Give me the name of your favorite book: ")

length = len(name)
print(length)


# ##### help()

# In[23]:


# Use this function to view more info about a python function
help(range)


# ##### isinstance()

# In[28]:


# Check a variable to find out what object family (or data type) it belongs to
# isinstance(var, type)

print(isinstance(4.5, int))

if isinstance(4.5, float):
    print("This number is a float type")
    
num = int(input("Pick a number "))
if isinstance (num, int):
    print(f"{num} is an int")
else:
    print(f"{num} is a float!")
    
#     This has problems. Doesn't account for floats.


# ##### abs()

# In[29]:


# /-5/ = 5

print(abs(-5))


# ### Try and Except

# In[31]:


# Use this to log out graceful and useful error messages
# Does not stop program! Neato!

try:
    input_num = int(input('Guess a number '))
    print('Your number is ' + str(input_num))
except:
    print("That didn't work: Change your input to a number!")


# ### Lists

# ##### Declaring Lists

# In[32]:


list_1 = []

names = ['Max', 'Cindy', 'Kathy', 'bob', 'Nate']
print(names)


# ##### Indexing a List

# In[36]:


# list_name [start: stop: step]

# single index
print(names[0])

# print starting at index 1 going to the end
print(names[1:])

# Print starting at the beginning of a list up until a number
print(names[:2])

# print starting at index 1 and going up by 2 in each iteration
print(names[1::2])

# print starting at the back and display in reverse order
print(names[::-1])


# ##### .append()

# In[40]:


names.append('Brandon')
print(names)


# ##### .insert()

# In[38]:


names.insert(3,'Devon')
print(names)


# ##### .pop()

# In[39]:


# Defaults to the last value if no parameter is given
# Pop returns the element that was removed in case you want to assign it to a variable

my_name = names.pop(2)
print(my_name)


# 
# ##### .remove()

# In[43]:


# Value to be removed rather than the index number
# names.remove('bob')
# print(names)

# remove multiple brandons from list
while 'Brandon' in names:
    names.remove('Brandon')
print(names)


# ##### del()

# In[44]:


# Goes by index, rather than value
# Be careful with del, it can cause indexing errors if not used carefully

del(names[1])
print(names)


# ##### Concatenating Two Lists

# In[47]:


# Will append two lists together, will NOT add the values!!

list_2 = [0, 1, 2]
list_3 = [3, 4, 5]

large_list = list_2 + list_3
print(large_list)


# ##### Lists Within Lists

# In[51]:


# Lists can hold ANY type of other element: Including other lists:
# They can go as deep as you want; this is called nested lists

names = ['Max', 'sam', 'Josh', ['Sally', ['Sue', 'Jim'], 'Tameka']]
print(names)
print(names[3])
print(names[3][1])


# ##### Looping Through Lists

# In[53]:


# Two ways to loop through a list! One is by index; the other is by using the 'in' keyword

# By index
for i in range(len(names)):
    print(names[i])
    
# Loop with 'in'
for i in names:
    print(i)


# ## Exercise #1 <br>
# <p>Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.</p>

# In[55]:


x = 0

while x ** 3 <= 1000:
    print(x ** 3)
    x += 1


# ## Exercise #2 <br>
# <p>Get first prime numbers up to 100</p>

# In[44]:


# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

for num in range (1, 101):
    # set flag
    prime = True
    # establish divisor at beginning of range
    for divisor in range (1, (num+1)):
        if num % divisor == 0:
            # because prime should only be evenly divisible by 1 & num
            if divisor != 1 and divisor != num:
                prime = False
    if prime == True:
        print (num)


# # Exercise 3 <br>
# <p>Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors</p>

# In[64]:


user_age = int(input("Please enter your age: "))

if user_age < 18:
    print("kids")
elif user_age <= 65:
    print("adults")
else:
    print("seniors")

