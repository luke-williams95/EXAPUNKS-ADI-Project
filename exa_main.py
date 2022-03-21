"""exa_main.py"""
import exa

file_directory = {1: 'instructions_pt1.txt', 2: 'instructions_pt2.txt', 3: 'instructions_pt3.txt', 4: 'instructions2_pt4.txt'}
# file_select = int(input('Part 1, 2, 3, or 4?: '))
file_select = 3

instructions_pt1 = """COPY 647 X
MODI X 7 T
DIVI X T X
MULI T T T
MULI X T X
MULI T T T

ADDI X T X
DIVI T 9 T
ADDI X 3 X
ADDI T X T
ADDI T X X
SUBI X T T
SUBI X T X
SUBI X T X
"""

instructions_pt2 = """COPY 10 X
COPY X T
TEST X = T
SUBI X T T
TEST X > T
TEST T < 1
"""

instructions_pt3 = """COPY 1 X
COPY 7 T
MARK LOOP
MULI T X X
SUBI T 1 T
TJMP LOOP
"""

instructions_pt4 = """GRAB 400
COPY 1 X
MARK A
SEEK -9999
ADDI X 1 X
TEST X < 50
FJMP D
MARK B
TEST EOF
TJMP C
MODI X F T
FJMP A
JUMP B
MARK C
COPY X F
JUMP A
MARK D
DROP
"""

target_instructions = file_directory[file_select]

punk = exa.EXA()
punk.read_file(target_instructions)

# print(punk.line_split(instructions_pt1))