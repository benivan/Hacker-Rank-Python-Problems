'''
Task

You are given a string .
Your task is to print all possible permutations of size  of the string in lexicographic sorted order.




>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>> 
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>> 
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
abc=[str(x)for x in input().split()]
permuted_value=list(permutations(abc[0].upper(),int(abc[1])))
for i in sorted(permuted_value):
    print("".join(i))
