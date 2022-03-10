import string
import sys

class EXA:
    
    def __init__(self):
        self.registers = {'X':0, 'T':0, 'F':0}
        # dict/map of all the known commands. 
        # Keys are the commands (str), the value pairs are a list that indicate each valid entry for an arugment
        self.functions = {
                    'COPY': (self.COPY, ['r/n', 'r']),
                    'ADDI': (self.ADDI, ['r/n', 'r/n', 'r']),
                    'SUBI': (self.SUBI, ['r/n', 'r/n', 'r']),
                    'MULI': (self.MULI, ['r/n', 'r/n', 'r']),
                    'DIVI': (self.DIVI, ['r/n', 'r/n', 'r']),
                    'MODI': (self.MODI, ['r/n', 'r/n', 'r']),
                    'TEST': (self.TEST, ['r/n', 'op', 'r/n'], ['=', '<', '>']),
                    'MARK': (self.MARK, []),
                    'JUMP': (self.JUMP, []),
                    'TJMP': (self.TJMP, []),
                    'FJMP': (self.FJMP, []),
                }
                    
    def execute(self, usr_in: str):
        """Takes in a string and then attempts to parse and run that command"""
        cmd_tuple = EXA.parse(usr_in) # EXA.parsed 'ADDI arg0 arg1 arg2' --> ('ADDI', [arg0, arg1, arg2])
        self.check_input(cmd_tuple) # checks for valid argument entries
        self.functions[cmd_tuple[0]][0](cmd_tuple[1]) # this calls the appropriate command method and gives the arguments.
        
    @staticmethod
    def parse(usr_in: str): # Add a function call to a valid arg to check args in this.
            """Digests the user input into a defined format, known as the command tuple (cmd_tuple)"""
            # "   ADDI   30  X T" ===> ("ADDI", ["30", "X", "T"])
            try:
                string_list = usr_in.strip().split(' ', 1) # Split the first string from usr_in using " " as your delimiter
                op_code = string_list[0] # op_code now contains the type of operation being performed
            except Exception as error:
                print(error, type(error))
            try:
                operand_list = string_list[-1].strip().split() # Split the remainder of string_list into a list of words
            except Exception as error:
                print(error, type(error))
            
            return (op_code, operand_list)
    
    def check_input(self, cmd_tuple: tuple):
        """Checks that the cmd_tuple contains valid entries for the given operation"""
        # ("ADDI", ["30", "X", "T"])
        
        error_count = 0
        
        if cmd_tuple[0] not in self.functions:
            print('OPCODE not recognized, please specify a valid operation')
            #sys.exit(1)
        # extract the valid format list from self.functions[OPCODE][1]
        # compare each element of cmd_tuple[1] with valid format list

        try:
            for cmd, format in zip(cmd_tuple[1], self.functions[cmd_tuple[0]][1]):
                
                if format == 'r' and cmd not in ('X', 'T', 'F'):
                    print('Invalid register in command')
                    error_count += 1
                if format == 'r/n' and cmd not in ('X', 'T', 'F'):
                    for char in cmd:
                        if char not in string.digits:
                            print('Invalid register or number in command')
                            error_count += 1
                if format == 'op' and cmd not in ('=', '<', '>'):
                    print('Invalid operator in command')
                    error_count += 1
        except Exception as error:
            print('Error:', error, type(error))
        
        if error_count:
            sys.exit(1)
        
        return True
                    
    def inspect(self, operand):
        """Checks the registers to see if arguments match the dict keys, otherwise pass the args along"""
        if operand in self.registers:
            return self.registers[operand]
        else:
            return int(operand)


    def print_reg(self):
        print(f"X:{self.registers['X']}\tT:{self.registers['T']}\tF:{self.registers['F']}\n")
        return
    
    def read_file(self, target_instructions):
        """Prompts the EXA to read a target instruction file. Will skip empty lines"""
        with open(target_instructions, 'r') as f:
            for line in f:
                if line == '\n':
                    continue
                self.execute(line)
                print(line, end= '')
                self.print_reg()
            f.close

    def ADDI(self, cmd_list):
        """Add the register values and store result in register. Called from interpret()"""
        # At this point we expect cmd_list to be a properly formatted list object
        # inspects the command list and puts the proper values in the operand_list
        # Should crash if len(cmd_list) != 3
        # ['X', 50, 'X']
        # X = 20
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        self.registers[cmd_list[-1]] = operand_list[0] + operand_list[1] # update register value
        # print(self.registers[cmd_list[2]]) # check that register value was updated
        return self.registers[cmd_list[-1]]


    def SUBI(self, cmd_list):
        """Subtract the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        self.registers[cmd_list[-1]] = operand_list[0] - operand_list[1] # update register value
        return self.registers[cmd_list[-1]]

    def MULI(self, cmd_list):
        """Multiply the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        self.registers[cmd_list[-1]] = operand_list[0] * operand_list[1] # update register value
        return self.registers[cmd_list[-1]]

    def DIVI(self, cmd_list):
        """Integer Divide the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        self.registers[cmd_list[-1]] = operand_list[0] // operand_list[1] # update register value
        return self.registers[cmd_list[-1]]

    def MODI(self, cmd_list):
        """Mod the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        self.registers[cmd_list[-1]] = operand_list[0] % operand_list[1] # update register value
        return self.registers[cmd_list[-1]]

    def COPY(self, cmd_list):
        """Copy the given value into the specified register"""
        self.registers[cmd_list[-1]] = self.inspect(cmd_list[0])
        return self.registers[cmd_list[-1]]

    def MARK(self, cmd_list):
        pass
    def TEST(self, cmd_list):
        pass
    def JUMP(self, cmd_list):
        pass
    def TJMP(self, cmd_list):
        pass
    def FJMP(self, cmd_list):
        pass
