mydict = {
    "fast": "in a quick manner",
    "Harry": "A coder",
    "marks": [1, 2, 5],
    "anotherdict" : {"Harry":"player"},
    1:2
}
# print(mydict.keys()) # prints the keys of the dict
# print(mydict.values()) # prints the values of the dict
# print(mydict.items())  # # prints the keys and values of the dict
# print(mydict)
updatedict = {
    "pooja":"sister",
    "dharti":"sister",
      "Harry": "dancer" #replace the value of key already present in dict
}
mydict.update(updatedict) #update the dict by adding key:value pair from updatedict
print(mydict)

#the difference between .get and [] syntax in dict:

print(mydict.get("harry2")) #returns none as Harry2 is not present in the dict
print(mydict["Harry2"]) #throws an error as Harry2 is not present in the dict
print(mydict.get("Harry")) #prints value associated with key "harry"
print(mydict["Harry"]) #prints value associated with key "harry"