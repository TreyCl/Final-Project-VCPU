import re

#Opens custom ASM files
#programFile = open('Boot_Sector_HW', 'r').read()
programFile = open('Boot_Sector_Arith', 'r').read()
st = programFile

#Removes comments from instruction set
st = re.sub('#.*#', '', st)

#Clips data section from ASM file
dataSection = st[st.find(".data")+5:st.find(".global")]

#Finds data bytes
x = st.find("db")
y = st[x:len(st)].find(";")

#Initializes data memory address, string, and finalized data array
dataAddr = [0, 0, 0]
dataStr = [""] * 259
data = [0] * 256

#For loops through data section for numeric values to add to data string
valueIndex = 0
for i in range(len(dataSection)):
    if dataSection[i].isnumeric():
        dataStr[valueIndex] = dataStr[valueIndex] + dataSection[i]
    
    elif not dataSection[i].isnumeric() and dataStr[valueIndex] != "":
            valueIndex += 1
        
    
#Seperates address data from data string
dataAddr[0:3] = dataStr[0:3]
for i in range(len(dataAddr)):
    dataAddr[i] = int(dataAddr[i])
    

dataAddr[2] +=1

#Places and converts data string into integer data array
for i in range(valueIndex-2):
    data[i] = int(dataStr[i+2])

#Clips program section from ASM file
programSection = st[st.find(".global")+7:len(st)]

#Assembles functions into cooresponding decimal optcodes 
program = programSection.replace("mov", "1").replace("add", "2").replace("sub", "3").replace("mul", "4").replace("div", "5").replace("_start:", "0"). replace("int", "0")

#Initializes for loops for numerical values to place in string array
progStr = [""] * 256

valueIndex = 0
for i in range(len(program)):
    if program[i].isnumeric():
        progStr[valueIndex] = progStr[valueIndex] + program[i]
    
    elif not program[i].isnumeric() and progStr[valueIndex] != "":
            valueIndex += 1
            
#Casts and places program string array into integer array 
progAddr = [0] * 256        
for i in range(valueIndex):
    progAddr[i] = int(progStr[i])
    
programData = progAddr