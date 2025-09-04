s= {2,4,4,6,7,8,9,10,10,11,12,13,14,15}
print(s, type(s))
s.add(56) # add an element
s.add(78)
print(s)

print(len(s)) # length of the set

s.remove(10)
s.remove(56)
print(s)

s.discard(715) # discard does not raise an error if the element is not found
s.discard(15)
print(s)

s.pop()  # removes a random element
print(s)

s.union({34,55,66,77}) # returns a new set with elements from both sets
s.intersection({2,4,6,8,10}) # returns a new set with elements common to both sets
print(s)

s.clear()  # removes all elements   
print(s)