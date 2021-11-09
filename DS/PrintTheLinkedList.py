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

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    # print all elements in the linkedlist
    # if head is null dont do anything
    # create a temp pointer for head
    _ = head
    if _ == None:
        return
    
    # print element in linked list
    # curretn value is head.data next value will be head.next
    while _ != None:
        print(_.data)
        _ = _.next
        

if __name__ == '__main__':