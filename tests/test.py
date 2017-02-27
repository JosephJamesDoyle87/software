# w ,h = 999,999;
# 
# Matrix = [[0 for x in range(w)] for y in range (h)]
# 
# 
# def turnon:
#     for x in range[0,0] to [999]:
#     
#  turn on 0,0 through 999,999
#  switch 0,0 through 999,0
#  turn off 499,499 through 500,500
#  where the first line specifies the size of the grid 0 < L < 109 and the next lines
#  contain the command. The only possible commands are ”turn on”, ”turn off” and
#  ”switch”.


#To initialize a two-dimensional array in Python:

rows = [10]
columns = [10]

a = [[x for x in range(columns)] for y in range(rows)]


x=4
y=3

print (a)