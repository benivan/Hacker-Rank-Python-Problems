from itertools import product
list1=[int(x) for x in input().split()]
list2=[int(y) for y in input().split()]
list3=[]
list3.append(list1)
list3.append(list2)

all_product(list(product(*list3)))
for i in all_products:
  print(i,end" ")
