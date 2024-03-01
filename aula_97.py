# l1 = [1,2,2,2,3,3,3,1,1,1]
# s1 = set(l1)
s1 = set()
s1.add(5)
s1.add(('ola'))
s1.update(('u', 1,2,4))
# l2 = list(s1)
# s1.clear()
s1.discard('u')
# print(s1)
s1 ={1,2,3}
s2 = {2,3,4}

s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s1 ^ s2



print(s3)