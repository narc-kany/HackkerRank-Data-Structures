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
# Complete the 'removeDuplicates' function below.
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

def removeDuplicates(llist):
    # Write your code here
    # Sorted link list 
    # data is in ascending order 
    # delete duplicate values 
    # temp pointer
    _ = llist
    
    # loop through end of the list
    while _.next != None :
        # check if the values are a duplicate
        if _.data == _.next.data :
            # if its a duplicate delete it
            _.next = _.next.next
        else :
            _ = _.next
        
    return llist

if __name__ == '__main__':