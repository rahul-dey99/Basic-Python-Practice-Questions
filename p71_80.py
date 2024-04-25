# Q.71
# dict = {}             # This is how we can create a empty dictionary in python.
# print(type(dict))

# Q.72
# d = {'key':"value"}
# print(d['key'])           # Ouptup: value

# Q.73
# d = {'key':"value"}
# d['key2'] = 'value2'       # This is how we can add key value pair in dictionary.
# print(d) 

# Q.74
# dict = {'a':1, 'b':2, 'c':3}
# print(dict.keys())               # The keys() function returns a list of all the keys in the dictionary.

# Q.75
# dict = {'a':1, 'b':2, 'c':3}
# dict.pop('a')                    # We can use the pop() method or del keyword to remove a key-value pair from a dictionary.
# print(dict)

# Q.76
# dict = {'a':1, 'b':2, 'c':3}               # This is a small program to access the value without knowing if key exists in 
# if 'b' in dict:                            # dictionary or not, without getting any exception.
#     print(dict['b'])
# else:
#     print("key is not present in dictionary.")

# Q.77
# print(len({1: 'one', 2: 'two', 3: 'three'}))    # Output: 3

# Q.78
# di = {1: 'one', 2: 'two', 3: 'three'}
# di[1] = 'hundred'                        # This is how we can update the value of the key in a dictionary.
# print(di)

# Q.79
# di = {1: 'one', 2: 'two', 3: 'three'}
# print(di.values())                       # The values() method can be used to get all the values of a dictionary. 

# Q.80
# di = {1: 'one', 2: 'two', 3: 'three'}
# print(di[5])                                # Throws a Keyerror when key is not present in the dictionary.