#!/bin/python3
'''
def add(arg1,arg2,arg3):
	sum = arg1 + arg2 + arg3
	return sum

arg1=2
arg2=3
arg3=4
result = add(arg1,arg2,arg3)
print(result)

arg1 = "argument 1"
arg2 = "argument 2"
function(arg1)
function(arg2)
'''
#
#Keyowrd  arguments
#def function(arg1, arg2):
#    print(arg1, arg2)

#default positional argument

def function(arg1 = "argument 1" ,  arg2 = "argument 2", arg3 = "argumnet 3" ):
    print(arg1)
    print(arg2)
    print(arg3)
arg1 = "my argument 1"
arg2 = "my argument 2"
arg3 = "my argument 3"
#function(arg1,arg3, arg2)
#function()
function(arg2="Keyword argument")
#function(arg1,arg2)
#function("only argument ", "2nd argument")


