import pprint

N = 100
 
a2d = [ list(range(i*N, i*N + N)) for i in range(N) ]
 
pprint.pprint(a2d, depth = 100)
 
 initialising a list
a = [0] * 10
pprint(a)

 
 import pprint
 stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
 stuff.insert(0, stuff[:])
 pp = pprint.PrettyPrinter(indent=4)
 pp.pprint(stuff)
 
 
 
 
 
 
 tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
 ('parrot', ('fresh fruit',))))))))
 pp = pprint.PrettyPrinter(depth=2)
 pp.pprint(tup)
