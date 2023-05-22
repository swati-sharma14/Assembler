from sys import stdin
from sys import exit

# type of instruction
def find_type(inp):
    if (len(inp)==4):
        if(inp[0] not in typea):
            syntax_error()
        else: return 'A'
    elif (len(inp)==2):
        if(inp[0] not in typee):
            syntax_error()
        else: return 'E'
    elif (len(inp)==1):
        if(inp[0] != 'hlt'):
            syntax_error()
        else: return 'F'
    elif (inp[2][0]=='$'):
        if(inp[0] not in typeb):
            syntax_error()
        else: return 'B'
    elif (inp[2].lower() in registers.keys()):
        if(inp[0] not in typec):
            syntax_error()
        else: return 'C'
    else:
        if(inp[0] not in typed):
            syntax_error()
        else: return 'D'

# opcode of instruction    
def find_opcode(inp):
    if (inp[0] in opcodes.keys()):
        if(inp[0]=='mov'):
            t = find_type(inp)
            if(t=='B'):
                return opcodes[inp[0]][0]
            else:
                return opcodes[inp[0]][1]
        return opcodes[inp[0]]
    return -1

# binary representation of registers
def reg(key):
    if(key.lower() in registers.keys()):
        return registers[key.lower()]
    else:
        print('Invalid register name')
        print('Line: ', ' '.join(inp))
        exit()

# decimal to binary (returns 8 bit answer and outputs error for immediate value > 8 bits)
def dectobin(n):
    L=[]
    while(n!=0):
        temp=n%2 
        L.append(str(temp))
        n=n//2
    L.reverse()
    final = ''.join(L)
    check_immval(final)
    while(len(final)<8):
        final = '0' + final
    return final

# return memory address of label
def find_var(x):
    check_var(x)
    return variables[x]

# return memory address of label
def find_label(x):
    check_label(x)
    return labels[x]

# assign label memory addresses
def assign_labels(instructions):
    global labels
    for i in range (len(instructions)):
        inp = instructions[i]
        j = 0
        while (inp[j]!='' and inp[j][-1]==':'):
            if (inp[j][:len(inp[j])-1] in labels.keys()):
                print('Label defined more than one time')
                print('Line: ', ' '.join(inp))
                exit()
            labels[inp[j][:len(inp[j])-1]] = dectobin(i)
            j+=1
        # empty labels case
        if (inp[j]==''):
            print('Empty label defined')
            print('Line: ', ' '.join(instructions[i]))
            exit()
        while(j>0):
            inp.remove(inp[0])
            j-=1
    return instructions    
    

# checks all halt related errors
def check_hlt(instructions):
    if (instructions[-1]==['hl'] or instructions[-1]==['hlt']):
        if ['hlt'] not in instructions[:len(instructions)-1]:
            instructions[-1] = ['hlt']
            return
        else:
            print("Invalid 'hlt' usage")
            exit()
    elif ['hlt'] not in instructions:
        print('Missing hlt instruction')
        exit()
    else:
        print("'hlt' is not used as last instruction")
        exit()

# check for length of imm value > 8 bits
def check_immval(st):
    if (len(st)>8):
        print("Immediate value greater than 8 bits")
        print('Line: ', ' '.join(inp))
        exit()

# check for undefined variable
def check_var(x):
    if(x not in tmp_var):
        print("Variable not defined")
        print('Line: ', ' '.join(inp))
        exit()

# check for undefine label
def check_label(x):
    if(x not in labels):
        print("Label not defined")
        print('Line: ', ' '.join(inp))
        exit()

# check for illegal use of flags register
def check_flag(inp,t):
    if(t!='C'):
        if ('FLAGS' in inp):
            print('Illegal use of FLAGS register')
            print('Line: ', ' '.join(inp))
            exit()
    else:
        if (inp[2].upper()=='FLAGS'):
            print("Illegal use of FLAGS register")
            print('Line: ', ' '.join(inp))
            exit()

# syntax error
def syntax_error():
    print('Invalid syntax')
    print('Line: ', ' '.join(inp))
    exit()


# op, register, variable, labels, output 
opcodes = {"add":'10000', "sub":'10001', "mov":['10010','10011'], "ld":'10100', "st":'10101', "mul":'10110', "div":'10111', "rs":'11000', "ls":'11001', "xor":'11010', "or":'11011', "and":'11100', "not":'11101', "cmp":'11110', "jmp":'11111', "jlt":'01100', "jgt":'01101', "je":'01111', "hlt":'01010'}
registers = {"r0" : '000', "r1" : '001', "r2": '010', "r3": '011', "r4": '100', "r5":'101', "r6": '110', "flags": '111'}
out = []
tmp_var = []
variables = {}
labels = {}
typea=['add','sub','mul','xor','and','or']
typeb=['rs','ls','mov']
typec=['mov','div','not','cmp']
typed=['ld','st']
typee=['jmp','jlt','jgt','je']


# creates a list of lists of all inputs from stdin
# counts number of lines to assign memory after n lines
n = 0
instructions = []
for line in stdin:
    if(line=='\n'): continue
    # last element of every line from stdin is '\n' and is hence sliced
    inp = line[:len(line)-1].split(' ')
    
    if(inp[0]=='var'):
        inp.remove(inp[0])
        if(inp==[]):
            print("Invalid variable definition")
            print('Line: ', line[:len(line)-1])
            exit()
        tmp_var.append(inp[0])
        continue

    instructions.append(inp)
    n+=1


# assign all labels memory addresses of the lines they point to
instructions = assign_labels(instructions)

# check for invalid 'hlt' usage
check_hlt(instructions)

# assigns memory locations to variables
for i in range(len(tmp_var)):
    variables[tmp_var[i]] = dectobin(n+i)


# output loop
for i in range(len(instructions)):
    inp = instructions[i]

    ans = find_opcode(inp)
    if(ans==-1):
        syntax_error()

    t = find_type(inp)
    check_flag(inp,t)

    if (t=='A'):
        ans = ans + '00' + reg(inp[1]) + reg(inp[2]) + reg(inp[3])
    elif (t=='B'):
        x = int(inp[2][1:])
        ans = ans + reg(inp[1]) + dectobin(x)
    elif (t=='C'):
        ans = ans + '00000' + reg(inp[1]) + reg(inp[2])
    elif (t=='D'):
        ans = ans + reg(inp[1]) + find_var(inp[2])
    elif (t=='E'):
        ans = ans + '000' + find_label(inp[1])
    else:
        ans = ans + '00000000000'
    out.append(ans)

print('\n'.join(out))
