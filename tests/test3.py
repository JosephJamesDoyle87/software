from pprint import pprint

stuff = ["a",'b','c']

pprint (stuff)

from builtins import str
def grid(str):
    "This prints a passed string into the function"
    print (str)
    return;

print('\n')
grid("This is a grid")
print('\n')
grid("This is another grid")
print('\n')
grid("and this is another grid")

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
pprint (a)
    
a2d = [a, a, a, a]
pprint(a2d)

print ('\n')

answer1= ('off')

columns = 999
rows = 999

b = [[0 for x in range(columns)] for y in range(rows)]


pprint(b)

    
