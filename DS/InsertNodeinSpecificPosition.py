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
# Complete the 'insertNodeAtPosition' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST llist
#  2. INTEGER data
#  3. INTEGER position
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def insertNodeAtPosition(llist, data, position):
    # Write your code here
    # insert a node at a specific position in the linkedlist(llist)
    # llist/head maybe empty then return as such
    # create a new node
    node = SinglyLinkedListNode(data)
    
    # check head node is not null if null head = node no changes
    if llist == None:
        llist = node
    else:
        temp = llist # temp pointer as header
        # skip nodes to reach position
        count = 1
        while temp != None and count < position:
            temp = temp.next
            count += 1
        
        # insert the new node
        node.next = temp.next # now node.next will point to temp node 
        temp.next = node # temp.next will point to the node 
    return llist
            
    
        


if __name__ == '__main__':