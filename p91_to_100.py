# Q.91
# l = [1,2,4]

# for i in range(len(l)):       # This is how we can iterate over a list with a loop.
#     print(l[i])

# Q.92
# The break statement comletely stops the execution of loop and the control comes out of the 
# loop body and continue executing the rest of the program.

# Q.93
# sum = 0
# while True:
#     num = input("Enter a number: ")    # Thisis how we can write a infinite loop which will keep running
#     if num.isdigit():                  # until user enter "quit".
#         num = int(num)
#         sum += num
#         print("Sum is:", sum)
#     elif num.capitalize() == 'Quit':
#         break
#     else:
#         print("Enter valid input.")

# print(" We are free.")

# Q.94
# The purpose of continue statement is to skin an iteration while looping through an iterable object.

# Q.95
# d = {'a':1, 'b':2}   # This is how we can loop through a dictionary and print its keys.
# for key in d:
#     print(key)

# Q.96
# for i in range(11):   # Counting from 0-10 with for loop.
#     print(i)

# Q.97
# for i in range(5):  # This loop will print numbers from 0 to 4.
#     print(i)

# Q.98
# l = [3, 1, 4, 1, 5]
# small = l[0]
# for i in range(len(l)-1):   # This is how we can find the smallest number in a list with a for loop.
#     if l[i] > l[i+1]:
#         small = l[i+1]
# print(small)

# Q.99
# l = [3, 1, 4, 1, 5]
# print("Index  -  Element")
# for idx, ele in enumerate(l):        # Using enumerate() function we can iterare the index and elements of a list.
#     print(idx, '     -     ', ele)

# Q.100
# for i in range(1,6):     # else clause is executed when the for loop has exhausted.
#     print(i)
# else:
#     print("Loop Exhausted.")