#!/usr/bin/env python

# Finding a Motif in DNA
# Problem
# Given two strings s and t, t is a substring of s if t is contained as a contiguous 
# collection of symbols in s (as a result, t must be no longer than s).
# The position of a symbol in a string is the total number of symbols found to its left, 
# including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" 
# are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].
# A substring of s can be represented as s[j:k], where j and k represent the starting and 
# ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
# The location of a substring s[j:k] is its beginning position j; note that t will have 
# multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

# Given: Two DNA strings s and t (each of length at most 1 kbp).
# Return: All locations of t as a substring of s.

# Sample Dataset
# GATATATGCATATACTT
# ATAT
# Sample Output
# 2 4 10
##########################
# Solution from Hazard
##########################
# Solution 1
s='GATATATGCATATACTT'
t='ATAT'
p=[]
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        p.append(i+1)
        print(i+1, end=" ")
        
# Solution 2
ith open('rosalind_subs.txt', 'r') as f:
    s=f.readline().strip()
    t=f.readline().strip()

i = 0
while True:
    i = s.find(t, i) +1 # Notice 1 step one loop. Some matches will be ignored if >1 (eg. len(t)) steps one loop.  
    if i==0:
        break
    print(i, end=" ")
#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 



