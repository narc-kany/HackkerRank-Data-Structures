#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'sortedInsert' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST llist
#  2. INTEGER data
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def sortedInsert(head, data):
    # Write your code here
    # create a new node
    # sort the order in acending
    # ie list is 1 -> 3 -> 4 ->10 insert 5 it will be 1234510
    node = DoublyLinkedListNode(data)
    
    # list is empty
    if head == None:
        head = node
    
    # insert before head when its smaller than head value
    elif data < head.data:
        node.next = head
        head.prev = node
        head = node
        
    # insert at specific position or at the end
    else:
        _ = head
        # traverse ot the specific position and matain sort order
        while _.next != None and _.data < data:
            _ = _.next
        
        # insert at the end
        if _.next == None and _.data < data:
            _.next = node
            node.prev = _
            
        # insert at a specific position
        else:
            previous = _.prev
            # change the previous node
            previous.next = node
            node.prev = previous
            # make chnages to the current node
            node.next = _
            _.prev = node
    return head

        

if __name__ == '__main__':