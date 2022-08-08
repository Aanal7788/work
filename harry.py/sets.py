# a = {1, 3, 4, 5, 1}
# print(type(a))
# print(a)  #set is not include repetative items


#empty set
#important: this syntax will create an empty dictionary... not an empty set
# a={}
# print(type(a))


#an empty set can be create using the below syntax
b = set()
print(type(b))
b.add(4)  # adding values to an empty set
b.add(5)
b.add(5)  # adding a value repeatedly does not change a set
# b.add([4, 5, 6]) #we can not add list in set as list is not hashable..list content can be changedso it can not be added in set
# print(b)
b.add((4,5,6)) #we can add tuple in set
print(b)
# b.add({4:5})  # we can not add dict in set
# print(b)


# print(len(b))  #prints the length of set


# b.remove(5)#removes 5 from set
# b.remove(15)#throwes an error while trying to remove 15 which is not present in set
# print(b)

# print(b.pop())  #pop any rendom item from set and remove it from set
# print(b)

# b.clear()  #emties the set
# print(b)


# a={8,11}
# c=b.union(a)#returns a new set with all items from both sets
# print(c)

a={4,11}
c=b.intersection(a)  #returns a new set which contains items only in both sets
print(c)


