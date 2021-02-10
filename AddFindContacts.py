# HackerRank-19 by Alina Li Zhang
## HackerRank-19: Coding Interview Questions with Python Solutions and Explanations
### https://www.hackerrank.com/challenges/ctci-contacts/problem


#!/bin/python3

import math
import os
import random
import re
import sys

def ngram(contact):
    ngram_list = [contact[0:i] for i in range (1,len(contact)+1)]
    return ngram_list
    
def add_contact(contact):
    ngram_list = ngram(contact)
    for token in ngram_list:
        contact_dict[token] = contact_dict.get(token,0) + 1

def find_contact(contact):
    return contact_dict.get(contact, 0 )

if __name__ == '__main__':
    n = int(input())

    contact_dict = {}
    for n_itr in range(n):
        opContact = input().split()
        op = opContact[0]
        contact = opContact[1]
        
        if op=='add':
            add_contact(contact)
        elif op=='find':
            print(find_contact(contact))
