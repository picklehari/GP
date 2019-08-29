from random import random, randint
from statistics import mean
from copy import deepcopy
from operator import xor
# GRT -> >
# LST -> <
# EQL -> ==
# def GRT(x,y):
#     return x>y
# def LST(x,y):
#     return x<y
# def EQL(x,y):
#     return x==y
POPSIZE = 100
MIN_TREE_SIZE = 2
MAX_TREE_SIZE = 6

def AND(x,y):
    return x and y

def OR(x,y):
    return x or y

def NOR(x,y):
    return not (x or y)

# RELATION_FUNCTIONS =[GRT,LST,EQL]
BINARY_FUNCTIONS = [AND,OR,NOR]
#UNARY_FUNCTIONS = [NOT]

TERMINALS = ['x','y',True,False]

def target_function(x,y):
    return xor(x,y)

def generate_dataset():
    dataset = []
    collection = [(True,False),(False,True),(False,False),(True,True)]
    for i in collection:
        dataset.append(i,target_function(i))
    return dataset
        
class GPTree:
    def __init__(self,data=None,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

    def node_label(self):
        if (self.data in BINARY_FUNCTIONS):
            return self.__name__
        else:
            return str(self.data)

    def print_tree(self ,prefix = " "):
        print(self.node_label())
        if self.left:
            self.left.print_tree()
        if self.right.print_tree():
            self.right.print_tree()

    
    def compute_tree(self,x,y):  
        if self.data in BINARY_FUNCTIONS:
            return self.data(compute_tree(self.left),compute_tree(self.right))
        elif self.data == x:
            return 'x'
        elif self.data == y:
            return 'y'
        else:
            return self.data

    def random_tree(self,grow,max_depth,depth = 0):
        if depth < MIN_DEPTH:
            




            
    
        
            

