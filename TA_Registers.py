#imports memory from RAM file
from TA_RAM import memory

#Boot sector
regF = memory[1][5] = 2

#System interrupt to make execution calls
def interrupt():
    
    def write():
        match regB:
            case 1:
                output = ''
                for i in range(regE): output += chr(memory[regC][regD+1 + i])
                print(output)
        
        
    match regA:
        case 0:
            exit("Exited")

        case 1:
            write()

          
#Register A operations and AU functions cooresponding to decimal optcodes
def operation():
    def mov(i):
        if memory[regF][i+3] == 0:
            memory[memory[regF][i+1]][memory[regF][i+2]] = memory[regF][i+4]
        
        else:
            memory[memory[regF][i+1]][memory[regF][i+2]] = memory[memory[regF][i+3]][memory[regF][i+4]]
            
    def add(i):
        memory[memory[regF][i+1]][memory[regF][i+2]] = memory[regF][i+3] + memory[regF][i+4]
        
    def sub(i):
        memory[memory[regF][i+1]][memory[regF][i+2]] = memory[regF][i+3] - memory[regF][i+4]
        
    def mul(i):
        memory[memory[regF][i+1]][memory[regF][i+2]] = memory[regF][i+3] * memory[regF][i+4]
        
    def div(i):
        memory[memory[regF][i+1]][memory[regF][i+2]] = round(memory[regF][i+3] / memory[regF][i+4])
    
    for i in range(len(memory[regF])):
        if i %5 == 0:
            match memory[regF][i]:
                case 0:
                    break;

                case 1:
                    mov(i)
                    
                case 2:
                    add(i)
                    
                case 3:
                    sub(i)
                    
                case 4:
                    mul(i)
                    
                case 5:
                    div(i)


#Performs operation
operation()

#Prints program and data memory
print(memory[2])
print(memory[3])

#Initializes register values
regA = memory[1][0]
regB = memory[1][1]
regC = memory[1][2]
regD = memory[1][3]
regE = memory[1][4]

#Prints register values
print("A:", regA)
print("B:", regB)
print("C:", regC)
print("D:", regD)
print("E:", regE)

#Executes SysCall
interrupt()

exit()