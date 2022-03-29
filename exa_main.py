"""exa_main.py"""
import exa

file_directory = {
                    '100': [1,1,1,1,1,1,1,1,1,1],
                    '200': [],
                    '400': [],
                    }

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

instructions_pt4 = """GRAB 100
MARK FILE_READ
ADDI F X X
TEST EOF
FJMP FILE_READ
DROP
GRAB 200
COPY X F
DROP
"""

punk = exa.EXA()
punk.file_load(file_directory)
punk.read_instructions(instructions_pt4)
print(punk.file_directory)

# print(punk.line_split(instructions_pt1))