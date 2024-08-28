from array import *

vars = [[0, 0], [0, 1], [1, 0], [1, 1]]

# AND
# return duo[0] & duo[1] 
def _and(duo):
    if(duo[0] == duo[1]):
        print(duo[0])
    else:
        print(0)
# OR
# return duo[0] | duo[1]
def _or(duo):
    if(duo[0] == 1 or duo[1] == 1):
        print(1)
    else:
        print(0)

# NOT
# return ~val%2
def _not(val):
    if(val == 0):
        print(1)
    else:
        print(0)

# NAND
# return _not(_and(duo))
def _nand(duo):
    if(duo[0] == duo[1]):
        if(duo[0] == 0):
            print(1)
        else:
            print(0)
    else:
        print(1)

# NOR
# return _not(_or(duo))
def _nor(duo):
    if(duo[0] == 1 or duo[1] == 1):
        print(0)
    else:
        print(1)

# XOR
# return duo[0] ^ duo[1]
def _xor(duo):
    if(duo[0] == duo[1]):
        print(0)
    else: 
        print(1)

# XNOR
# return _not(_xor(duo))
def _xnor(duo):
    if(duo[0] == duo[1]):
        print(1)
    else:
        print(0)

# Execute functions
# TODO: Write code to store values from operations
# TODO: Write code to recieve values as parameters
# TODO: Write code to execute certain operations as parameters
for i in vars:
    print(i)
    print("And")
    _and(i)
    print("Or")
    _or(i)
    print("Not")
    _not(i[0])
    _not(i[1])
    print("Nand")
    _nand(i)
    print("Nor")
    _nor(i)
    print("Xor")
    _xor(i)
    print("Xnor")
    _xnor(i)


