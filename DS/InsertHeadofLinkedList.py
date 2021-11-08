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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):
    # Write your code here
    # add head of a link list
    # if it has element assign a new node 
    # if empty return as such
    node = SinglyLinkedListNode(data) # create a new node
    
    # llist is head pointer
    # no need to check for end of the list here so code ends here as it directly added to the head
    if llist != None:
        node.next = llist
    
    return node

        
    
    

    

if __name__ == '__main__':