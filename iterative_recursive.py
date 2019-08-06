# the three approaches (recursive vs. iterative) to writing the same function
# Trying out the three different implementations of the is_segment function in the lecture at:
# https://www.cs.cmu.edu/~fp/courses/15122-f15/lectures/10-linkedlist.pdf
# A wonderful lecture from CMU 
class Node:
    def __init__(self, data):
        self.data = data

class LList:
    def __init__(self, nxt, head, tail):
        self.nxt = None
        self.head = head
        self.tail = tail
    #1. recursive
    def is_segment_recur(self, l_list_s, l_list_e):
    # input: linked list # not utterly clear whether the input is the linked list or a node because I do not know this language.
    # what makes more sense? I think a node makes more
    # what the function does: points to the next node until the last
    # output: boolean
        if l_list_s == None:
            return False
        if l_list_s == l_list_e:
            return True
        return self.is_segment_recur(l_list_s.nxt, l_list_e)
    # 2. the iterative while loop version! Wait, does it make sense to do a for loop since we do not have the length
    def is_seg_while(self, l_list_s, l_list_e):
        l = l_list_s       
        while l != None:
            if l == l_list_e:
                return True
            l = l.nxt
        return False

        







if __name__ == "__main__":
    #creating four nodes
    Node1 = Node(1)
    Node2 = Node(2)
    Node3 = Node(3)
    Node4 = Node(4)
    #initializing the linked list with its head and tail
    llist = LList(None, Node1, Node4)
    Node1.nxt = Node2
    Node2.nxt = Node3
    Node3.nxt = Node4
    #Try out the recursive version :)
    print(llist.is_segment_recur(llist.head, llist.tail))
    print(llist.is_seg_while(llist.head, llist.tail))