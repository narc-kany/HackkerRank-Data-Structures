#!/bin/python3

import math
import os
import random
import re
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

#
# Complete the 'getNode' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER positionFromTail
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def getNode(llist, positionFromTail):
    # Write your code here
    # get a node form a specific position counting backwards
    # 1 is tail 
    # get kth node from the nail
    # we have head and position
    # intialize 2 pointer
    _1 = llist
    _2 = llist
    
    # traverse to the positon of the node
    # ie, 2 position 2 1 1 0 3 3 2 1 2
    # now traverse by index now _1 is of value 1
    for idx in range(positionFromTail):
        _1 = _1.next
        
    # traverse both node now 
    # traverse until end similaraly second node also deduces 
    while _1.next != None:
        _1 = _1.next
        _2 = _2.next
    
    return _2.data
    
    

if __name__ == '__main__':