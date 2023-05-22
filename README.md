# 🖥️ Assembly Language Convertor 📝

This program is an Assembly Language Converot implemented in Python. It takes a specific input format from the standard input (stdin) and generates intermediate code as output. Here's how the program works:

📥 Input Format:
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

🔍 Functionality:
The program performs the following tasks:

  - Determines the type and opcode of each instruction based on the input.
  - Converts register names and values to their binary representation.
  - Assigns memory addresses to variables and labels.
  - Performs error checks for syntax, undefined variables/labels, invalid register usage, and more.
  - Generates intermediate code based on the provided input instructions.

⚙️ Usage:
  - Prepare a text file containing the input instructions in the specified format.
  - Run the program in the terminal or command prompt.
  - Redirect the input from the text file using the following command:
    - python main.py < input.txt
  - The program will process the input instructions and generate the intermediate code as output.

🔑 Key Features:
  - Error checking for syntax, undefined variables/labels, invalid register usage, and more.
  - Support for arithmetic operations, register shifts, jumps, variable definitions, and label definitions.
  - Clear separation of opcode determination, binary conversion, and intermediate code generation.
