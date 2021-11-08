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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    # print the entire linkedlist if it has value
    # else dont do anything 
    # output is newline 
    # dont change the headpoiter in the linkedlist
    # head pointer maybe empty(list is empty) then assign a new head
    # insert node at the end of each element in the list
    # create a new node for this new data 
    node  = SinglyLinkedListNode(data) # SinglyLinkedListNode is a the class to create a node
    
    # Head pointer is null
    if head == None:
        head = node
    
    else:
        # Insert node at the tail
        temp = head
        # traverse to the end of the list
        while temp.next != None:
        # loop will execute until the end of the list
            temp = temp.next
        temp.next = node # assign end to tail
    return head

if __name__ == '__main__':