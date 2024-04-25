# Q.61
# tup = (5,)         # We can create a tuple with a single element like this. 
# print(type(tup))

# Q.62
# Lists: Lists are mutable, which means their elements can be added removed or updated after creation.
# Tuples: Tuples are immutable meaning you cannot the data once stored inside a tuple.

# Q.63
# tup = (0,1,2,3,4,5)
# print(tup[1])         # We can simply use index to access the elements of a tuple.

# Q.64
# tup = (2,5,7)
# tup[2] = 9     # No, because tuples are immutable.
# print(tup)

# Q.65
# t1 = (1,2,4)
# t2 = (5,6,7)         
# print(t1 + t2)      # It extended the tuples.

# Q.66
# tup = ('a', 'b', 'c')
# v1, v2, v3 = tup     # We can do this to unpack the elements of the tuple into different varibales.
# print(v1, v2, v3)

# Q.67
# If we try to modify one of the elements of a tuple, we get error saying, "Assignment is not allowed in tuples." 

# Q.68
# l = [1,2,3,4,4]
# t = tuple(l)              # We can use the tuple() method to create the tuple of a list.
# print(type(l), type(t))

# Q.69
# print((1,2)*3)     # It added the elements in the tuple 2 more times, increasing the size tuple 3 times.

# Q.70
# tup = (0,1,2,3,3,3,6)
# print(len(tup))         # Using the len() function we can find length of the tuple.