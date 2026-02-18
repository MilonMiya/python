#Indexing
str = "Milon Miya"
print (str[0], str[1], str[2], str[3], str[4])

#Slicing
str = "Milon Miya"
print (str[0:12])
print ( str[2:8])
#negative index
str = "Apple"
print (str[-5:-2])
print (str[-3:-1])
print (str [-5:-4])

str = "I am studying python from ApnaCollege"
print (str.endswith("ege")) #True
print (str.endswith("from")) #False

#string.capitalize()
str = "hello world"
print(str.capitalize())

#str.replace()
str = "I love Java"
print(str.replace("Java", "Python"))

str = "banana"
print(str.replace("a", "o"))

str = "banana"
print(str.replace("a", "o", 2))

