# 🖥️ Assembly Language Convertor 📝

This program is an Assembly Language Converot implemented in Python. <br>
It takes the assembly program in a specific input format from the standard input (stdin) and generates a binary code as an output text file(stdout). <br><br>
Here's how the program works:

📥 Input Format: <br>
The input to the assembler is a text file containing the assembly instructions. <br>
Each line of the text file may be of one of 3 types:
- Empty line: Ignore these lines
- A label
- An instruction
- A variable definition

Each of these entities has the following grammar:
- The syntax of all the supported instructions is given above. The fields of an instruction are whitespace separated. The instruction itself might also have whitespace before it. An instruction can be one of the following:
  - The opcode must be one of the supported mnemonics.
  - A register can be one of R0, R1, ... R6, and FLAGS.
  - A mem_addr in jump instructions must be a label.
  - An Imm must be a whole number <= 255 and >= 0.
  - A mem_addr in load and store must be a variable.
- A label marks a location in the code and must be followed by a colon (:). No spaces are allowed between the label name and colon (:).
- A variable definition is of the following format:
  - var xyz <br>
  which declares a 16-bit variable called xyz. <br>
  This variable name can be used in place of mem_addr fields in load and store instructions. All variables must be defined at the very beginning of the assembly program.

🔍 Functionality: <br>
The program expects input instructions in a specific format from the standard input. Each line should represent an instruction and should follow the following rules:
- Instructions should be space-separated.
- The last element of every line should be a newline character '\n'.
- The program supports the following types of instructions:
  - Arithmetic Instructions: add, sub, mul, xor, and, or
  - Register-Shift Instructions: rs, ls
  - Move Instruction: mov
  - Load Instruction: ld
  - Store Instruction: st
  - Division Instruction: div
  - Not Instruction: not
  - Comparison Instruction: cmp
  - Jump Instructions: jmp, jlt, jgt, je
  - Halt Instruction: hlt
  - Variable Definition: var (e.g., var x)
  - Label Definition: label_name: (e.g., loop:)
- The program also supports immediate values, variables, and labels.

⚙️ Usage:
  - Prepare a text file containing the input instructions in the specified format.
  - Run the program in the terminal or command prompt.
  - Redirect the input from the text file using the following command:
    - python main.py < input.txt
  - The program will process the input instructions and generate the intermediate code as output.

🔑 Key Features: <br>
The assembler is capable of:
  1. Handling all supported instructions.
  2. Handling labels.
  3. Handling variables.
  4. Making sure that any illegal instruction (any instruction or instruction usage which is not supported) results in a syntax error. <br>
     In particular, it handles:
     - Typos in instruction names or register names.
     - Use of undefined variables.
     - Use of undefined labels.
     - Illegal use of FLAGS register.
     - Illegal Immediate values (more than 8 bits).
     - Misuse of labels as variables or vice versa.
     - Variables not declared at the beginning.
     - Missing hlt instruction.
     - hlt not being used as the last instruction.
   You need to generate distinct readable errors for all these conditions. If you find any other illegal usage, you are required to generate a "General Syntax Error". The assembler must print out all these errors.
  5. If the code is error-free, then the corresponding binary is generated. The binary file is a text file in which each line is a 16-bit binary number written using 0s and 1s in ASCII. The assembler can write less than or equal to 256 lines.
