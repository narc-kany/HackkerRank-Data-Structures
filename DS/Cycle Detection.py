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

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
# check if the value is null
# cyclic is when the nth node points to the n-x node 
# slow pointer : 1, 2, 3
# fast pointer : 1, 3, 3(2 points to 3 and 3 points back to 2 which again points to 3)
# initiate temp values each pointign each method
    slow = fast = head
    
    # working 
    while fast != None and fast.next != None:
        # check for not null
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

if __name__ == '__main__':