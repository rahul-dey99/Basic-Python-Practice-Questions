# Q.81
# s = set()           # by using the set keyword we can make an empty set.
# print(type(s))

# Q.82
# print(len(set([1, 2, 3, 2, 1])))     # Output is 3 because set doesn't allow duplicate elements.

# Q.83
# s = {1,2,3}
# s.add(4)        # We can use add() function to add elements in a set.
# print(s)

# Q.84
# s1 = {1,2,3}
# s2 = {3,4,5}
# var = s1.intersection(s2)      # intersection() function returns the intersection of 2 sets.
# print(var, type(var))

# Q.85
# s = {1,2,3}
# s.remove(1)      # remove() function takes a argument and remove it from the set. 
# print(s)

# Q.86
# The main difference between a set and a list is that list allows duplicate elements in it 
# while, set does not store duplicate elements.

# Q.87
# s1 = {1,2,4,7,8,5}
# s2 = {2,3,4,5}
# intersec = s1.intersection(s2)     # This is how I find elements that are in either of two sets but not in both.
# for i in intersec:
#     s1.remove(i)
#     s2.remove(i)
# uni = s1.union(s2)
# print(uni)

# Q.88
# s1 = {2,4,7}
# s2 = {1,2,4,7,8,5}
# is_sub_set = s1.issubset(s2)      # Using the issubset() method we can find if s1 is subset of s2.
# is_sub_set = s1 <= s2             # Using the <= subset operator.
# print(is_sub_set)

# Q.89
# print({1,2,3}.union({3,4,5}))     # It resulted in a union set of the 2 given sets.

# Q.90
# set1 = {1,2,4,5,6}
# set1.clear()                      # clear() method can delete all the elements from a set. 
# print(set1)