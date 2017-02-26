# import pprint
# 
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# print (a)

# a2d = [a, a, a, a]
# print(a2d)
# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]

#indexing 2d lists
N =122
a2d = [ list(range(i*N, i*N + N)) for i in range(N) ]
print(a2d)