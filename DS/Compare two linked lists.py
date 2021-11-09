#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    # compare 2 head nodes in the linked list
    # list maybe empty
    # check for size as well
    # return 1 when equal else 0
    # create temp to store
    _1 = llist1
    _2 = llist2
    
    # while _1 != None and while _2 != None both are same
    while _1 and _2:
        # check data validation (equal)
        if _1.data == _2.data:
            _1 = _1.next
            _2 = _2.next
        else:
            return 0
    # doing like this will eventually make the value null so check for that condition
    
    if _1 == None and _2 == None:
        return 1
    else:
        return 0
    
        
        

if __name__ == '__main__':