from Linkedlist import Linklist

def __str__(self):
    out_str = '['
    
    _cur = self._start
    
    while _cur is not None:
        out_str += str(_cur.data)+','
        _cur = _cur.next
    return out_str.strip(',') + ']'



Linklist.__str__ = __str__


def print_square(node_x):
    print (node_x.data, "x", node_x.data, '=')
    print (node_x.data * node_x.data)



def call_func(self, fn):
    _cur = self._start
    while _cur is not None:
        fn(_cur)
        _cur = _cur.next
    

Linklist.call_func = call_func



my_list = Linklist()
my_list.insert(25)
my_list.insert(35)
my_list.insert(4)

print(my_list)
my_list.call_func(print_square)