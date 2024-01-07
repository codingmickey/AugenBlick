
# import the text file
import os
import sys
import re
import math

# read the file
def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read()
    return data

input = read_file('input5.txt')

# split the input into a list of strings
input = input.split(',')

def hash(str):
    ans = 0
    
    for character in str:        
        ascii_character = ord(character)
        ans += ascii_character
        ans *= 17
        ans = ans % 256
        # print(ans)
    
    return ans

final_ans = 0
# how to traverse the input list
for chunk in input:
    final_ans += hash(chunk)
    # print(chunk, hash(chunk))

print("The final answer is: " + str(final_ans))