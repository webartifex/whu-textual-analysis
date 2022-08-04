# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 21:40:57 2017

@author: Alexander Hillert, Goethe University Frankfurt
"""

directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Task 1: Open and print
# Open the Txt-file
print("\nTask 1 starts here!\n")
input_file=open(directory+'Fun_with_Python.txt','r')
input_text=input_file.read()
# Alternative with one command
input_text=open(directory+'Fun_with_Python.txt','r').read()

print(input_text)

# Task 2: Write text to output file
# Create file 'More_fun_with_Python.txt'
print("\nTask 2 starts here!\n")
output_file=open(directory+'More_fun_with_Python.txt','w')
output_file.write("Hallo\n")
output_file.write(input_text)
output_file.close()

# Task 3: loop
print("\nTask 3 starts here!\n")
# Alternative 1: While loop
i = 1
while i<=10:
    print('Iteration Number: '+str(i))
    i=i+1
    # Example of a nested loop
    j=1
    while j<3:
        print('Hallo')
        j=j+1

# Alternative 2: For loop
for i in range(0,10):
    print('Iteration Number: '+str(i))
# there is also a shorter notation: if there is no lower bound it is assumed to be zero
for i in range(10):
    print('Iteration Number: '+str(i))


# Task 4: Print text line by line
# Print text line by line
print("\nTask 4 starts here!\n")
line_of_text=input_text.split('\n')
i=0
while i<len(line_of_text):
    print("Line "+str(i+1)+": "+line_of_text[i])
    i=i+1

# First alternative using a for loop
for i in range(0,len(line_of_text)):
    print("Line "+str(i+1)+": "+line_of_text[i])
    
    
# Second alternative
# for ... in -> for each element of the list do ...
# line can be any name; it refers to the elements of the list
i=1
for line in line_of_text:
    print("Line "+str(i)+": "+line)
    i=i+1


# Task 5: count 'good'
# Count how often the word 'good' appears in the text
print("\nTask 5 starts here!\n")
number_good=input_text.count('good')
print(number_good)
# you can write the command in a shorter format
print(input_text.count('good'))

# Task 6a
# Print lines with the word 'good'
print("\nTask 6a starts here!\n")
for i in range(len(line_of_text)):
    if line_of_text[i].count('good')>=1:
        print(line_of_text[i])


# Task 7
# Print lines that start with the word 'This'
print("\nTask 7 starts here!\n")
print("\n'This' with a capital T.\n")
for i in range(len(line_of_text)):
    if line_of_text[i].startswith('This')>=1:
        print(line_of_text[i])
        
print("\n'this' with a lower case t.\n")
for i in range(len(line_of_text)):
    if line_of_text[i].startswith('this')>=1:
        print(line_of_text[i])

print("Yes, the command is case sensitive (2 vs. 0 matches)!")


# Task 8
# Replace the word 'good' by 'excellent'
print("\nTask 8 starts here!\n")
new_text=input_text.replace("good","excellent")
print(new_text)

# For illustation only
print("\nFor illustation only\n")
for i in range(len(line_of_text)):
    new_line_of_text=line_of_text[i].replace('good','excellent')
    # print the new line IF there are a change.
    if not new_line_of_text==line_of_text[i]:
        print(new_line_of_text)

input_file.close()
output_file.close()

print("DONE")