RELATION_FUNCTIONS =[GRT,LST,EQL]
BINARY_FUNCTIONS = [AND,OR]
UNARY_FUNCTIONS = [NOT]

TERMINALS = ['x','y',True,False]

class Tree:
    def __init__(self, data = None, left_child = None,right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def node_label(self):
        if(self.data)

