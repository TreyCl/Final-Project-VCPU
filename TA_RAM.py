#Initializes 2D 256*256 decimal array 
rows, cols = (256, 256) 
memory = [[0 for i in range(cols)] for j in range(rows)] 

#Imports ASM file data for virtual initilization
from TCL_ASM_Compiler import dataAddr, data, programData 

#Places ASM data in virtual boot and data sectors
for i in range(dataAddr[2]):
    memory[dataAddr[0]][i] = data[i]

for i in range(255):
    memory[2][i] = programData[i+1]
