# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:07:10 2015


@author: Alexander Hillert, Goethe University Frankfurt
"""

# To determine file size we need the OS package
import os

# Please adjust the directory to your machine.
directory="C:/Lehre/Textual Analysis/Programming/Files/"

# Open the csv file containing the list of the 200 10-Ks
input_file=open(directory+'10-K_Sample_2011Q1_Input.csv','r',encoding="utf-8")
input_text=input_file.read()

# Create output file
output_file=open(directory+'10-K_Sample_2011Q1_File_Size.csv','w',encoding="utf-8")
output_file.write('CIK;Filename;File_size_gross;File_size_net\n')

# Split the input file in separate lines
input_text_line=input_text.split("\n")

# In general, there can be empty lines in the input file. The following command
# deletes these lines.
while input_text_line.count("")>0:
    input_text_line.remove("")
    
# Loop over all lines
for i in range(1,len(input_text_line)):
    print(str(i))
    # split the line into the two variables
    variables=input_text_line[i].split(";")
    # We need the CIK and the filename
    cik=variables[0]
    filename=variables[1]
    filename=filename.replace('.txt','')
    
    # File size of the complete submission file (gross file size)
    # You have to divide the result by 1024 to get the size in kilobyte
    # The file size will be affected by html code and exhibits.
    # APPLY THE COMMAND THAT IS SHOWN ON SLIDE 62.
    size_gross=XXX/1024
    
    # File size of the main text file (net file size)
    # You have to divide the result by 1024 to get the size in kilobyte
    size_net=XXX/1024 # SAME COMMAND AS FOR GROSS FILE SIZE BUT APPLIED TO THE _clean.txt
    
    output_file.write(cik+';'+filename+';'+str(size_gross)+';'+str(size_net)+'\n')
    
print("Finished")
output_file.close()
input_file.close()
