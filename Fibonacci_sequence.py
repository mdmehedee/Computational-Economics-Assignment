#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 0
Submitted By: Md Mehedee Zaman Khan
Matrikel-Nr.: 665630
Email: mehedee.zaman95@gmail.com
"""

#Initialise 2 variables
first_num= 0
second_num = 1
sequence = []  #Create an empty list
sequence.extend([first_num,second_num]) #Adding the initial Fibonacci numbers into the list.

def Fibonacci_sequence(n):
  #Using global keyword to access variable first_num and second_num
  global first_num,second_num

  while(len(sequence)<n): 
    #The Sum of the first 2 sequences is added to the sequence list again
    new_num = first_num + second_num
    sequence.append(new_num)
    #Updating the first and second variables for finding the next number.
    first_num = second_num
    second_num = new_num
    
  return sequence  
        
print(f'F5 Fibonacci sequence is : {Fibonacci_sequence(5)}')
print(f'F6 Fibonacci sequence is : {Fibonacci_sequence(6)}')
print(f'F7 Fibonacci sequence is : {Fibonacci_sequence(7)}')
print(f'F25 Fibonacci sequence is : {Fibonacci_sequence(25)}')
print(f'F40 Fibonacci sequence is : {Fibonacci_sequence(40)}')