a=("apple", "mango", "cherry", "kiwi","orange", "melon")

print("this is my tuple: "+str(a))


#length of tuple
print("\n length of my tuple:")
print(len(a))

#accessing item n the tuple

print(a[2:5])
print(a[:4])
print("\n")

#unpacking tuples
fruits=("apple", "mango", "cherry", "kiwi","orange", "melon")
(green, yellow, *red)=fruits
print(green)
print(yellow)
print(red)