from pprint import pprint
   
#    
# w, h = 100, 499;
# w1,h1 = 500,999;
# Matrix = [['on' for x in range(w1)] for y in range(h1)] 
#   
# Matrix = [['off' for x in range(w)] for y in range(h)] 
#   
# from test.badsyntax_future3 import result
#    
# print (Matrix[105][400])
#    
w, h = 999,999;
    
Matrix = [[0 for x in range(w)] for y in range(h)] 
    
Matrix[0][0] = "on"
print (Matrix[0][0]) # prints 
     
Matrix[0][2] = ("off")
     
print (Matrix[0][2]) # prints 
i=0
for i in range(w,h):
    print (i)

# def test(x):
#     for 
#     
# print (test(4))

