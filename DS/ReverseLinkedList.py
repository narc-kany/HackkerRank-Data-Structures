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
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse(llist):
    # Write your code here
    # Reverse a LinkedList
    # Reverse the pointer of n node to n-1 nodes 
    # check list empty
    # intilaize 3 pointer
    previous = None 
    current = llist
    nxt = llist.next
    
    while current != None:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
        # change the direction of the node (shifiting the nodes)
        
    llist = previous
    
    return(llist)
        
        

if __name__ == '__main__':