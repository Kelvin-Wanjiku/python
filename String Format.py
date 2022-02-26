quantity=3
item_no=456
price= 300
my_order="I want {} pieces of item {} for kshs{} "

print(my_order.format(quantity,item_no,price))


#using index numbers to ensure arguments are well placed in the right order
my_order="I want to pay kshs{2} for {0} pieces of item {1}"
print(my_order.format(quantity, item_no, price))