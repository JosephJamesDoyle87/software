# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# pprint (a)
#     
# a2d = [a, a, a, a]
# pprint(a2d)
# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
#     
# #indexing 2d lists
# N =122
# a2d = [ list(range(i*N, i*N + N)) for i in range(N) ]
# print(a2d)
# 
# slicing 
# N = 999
# a = list(range(N))
# print(a[99:105])
    
#slicing 2
    
# print(a[2:5])
    
# # Iteration on lists - using index and element access
# a = list(range(N))
# for i in range(len(a)):
#     print(i, a[i])
    
# use readlines to read a line a time
# filename = "data/data.txt"
# with open(filename) as f:
#     for line in f.readlines():
#          process line        
#         values = line.strip().split()
#   
#  read the whole file into a buffer
# buffer = open(filename).read()
#   
# for line in buffer.split('\n'):
#      process line
#   
#     import urllib.request
# help(urllib.request.urlopen)
# Help on function urlopen in module urllib.request:
#   
# urlopen(url, data=None, timeout=<object object at 0x10185f2c0>, *, cafile=None, capath=None, cadefault=False, context=None)
#   
#  request
#   
# uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
# req = urllib.request.urlopen(uri)
#   
# buffer = req.read().decode('utf-8')
#   
# def read_uri(fname):
#     if fname.startswith('http'):
#          use urllib.request.urlopen(uri)
#     else:
#          use open(uri)
#     return ...
#   
# import argparse
#   
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='input help')
# args = parser.parse_args()
#   
# filename = args.input