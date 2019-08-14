from random import random, randint
from statistics import mean
from copy import deepcopy

# GRT -> >
# LST -> <
# EQL -> ==
# def GRT(x,y):
#     return x>y
# def LST(x,y):
#     return x<y
# def EQL(x,y):
#     return x==y

def AND(x,y):
    return x and y

def OR(x,y):
    return x or y

def NOT(x):
    return not x

# RELATION_FUNCTIONS =[GRT,LST,EQL]
BINARY_FUNCTIONS = [AND,OR]
UNARY_FUNCTIONS = [NOT]

TERMINALS = ['x','y',True,False]

def target_function(x,y):
    return ((not x) and y) or (x and not(y))

def generate_dataset():
    dataset = []
    collection = [(True,False),(False,True),(False,False),(True,True)]
    for i in collection:
        dataset.append(target_function(collection))
        
class GPTree:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    # def node_label(self):
    #     if (self.data in BINARY_FUNCTIONS):
            

