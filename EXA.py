import string
import sys

class EXA:
    
    def __init__(self):
        self.registers = {'X': 0, 'T': 0, 'F': 0}
        self.file_cursor = {'NAME': '', 'POINTER': 0, 'LEN': 0} # Holds keys to the current file name and pointer location
        self.file_directory = {} # Loads in local files after initialization        
        self.marks = {} # Holds the MARK functions LABEL/file_point key/value pairs
        self.instruction_pointer = 0 # Tracks current location within instruction_list
        # Keys are the commands (str), the value pairs are a list that indicate each valid entry for an argument
        self.functions = {
            'COPY': (self.COPY, ['R/N', 'R']),
            'ADDI': (self.ADDI, ['R/N', 'R/N', 'R']),
            'SUBI': (self.SUBI, ['R/N', 'R/N', 'R']),
            'MULI': (self.MULI, ['R/N', 'R/N', 'R']),
            'DIVI': (self.DIVI, ['R/N', 'R/N', 'R']),
            'MODI': (self.MODI, ['R/N', 'R/N', 'R']),
            'TEST': (self.TEST, ['R/N', 'OP', 'R/N'], ['=', '<', '>']),
            'MARK': (self.MARK, ['L']),
            'JUMP': (self.JUMP, ['L']),
            'TJMP': (self.TJMP, ['L']),
            'FJMP': (self.FJMP, ['L']),
            'GRAB': (self.GRAB, ['R/N']),
            'FILE': (self.FILE, ['R']),
            'SEEK': (self.SEEK, ['R/N']),
            'VOID': (self.VOID, ['F']),
            'DROP': (self.DROP, []),
        }
        """Next time, use a dict of dicts, as it would have made the code more readable to write self.functions[COPY[EXECUTE]] 
        or self.functions['COPY'['FORMAT']] instead of self.functions['COPY'][0] or self.functions['COPY'][1] """
        
              
    def execute(self, usr_in: str):
        """Takes in a string and then attempts to parse and run that command"""
        if usr_in: # If not an empty string
            print(usr_in, end= '\n')
            cmd_tuple = EXA.parse(usr_in) # EXA.parsed 'ADDI arg0 arg1 arg2' --> ('ADDI', [arg0, arg1, arg2])
            self.check_input(cmd_tuple) # checks for valid argument entries
            self.functions[cmd_tuple[0]][0](cmd_tuple[1]) # this calls the appropriate command method and gives the arguments.
            self.print_reg()
            self.F_access_check(cmd_tuple[1])
            return
            

    def check_input(self, cmd_tuple: tuple):
        """Checks that the cmd_tuple contains valid entries for the given operation"""
        # ("ADDI", ["30", "X", "T"])
        
        error_count = 0
        
        if cmd_tuple[0] not in self.functions: # Checks to see that the OPCODE is valid. Valid opcode required for remaining checks
            print('OPCODE not recognized, please specify a valid operation')
            #sys.exit(1)
       
        # extract the valid format list from self.functions[OPCODE][1]
        # compare each element of cmd_tuple[1] with valid format list
        try: # For every operand in the cmd_tuple[1] portion of the tuple, compare it with the proper format found within self.functions[OPCODE][1]
            for cmd, format in zip(cmd_tuple[1], self.functions[cmd_tuple[0]][1]): 
                
                if format == 'R' and cmd not in self.registers: # If the format is Register, verifies that cmd is either 'X', 'T', or 'F' 
                    print('Invalid register in command')
                    error_count += 1
                if format == 'R/N' and cmd not in self.registers: # If the format is a register or number and cmd is not a register...
                    if cmd != 'EOF': # Check for end of file cmd. Handles the special 'TEST EOF' case, where len(cmd_tuple) != len(self.functions[OPCODE][1])
                        for char in cmd: # For every character in the string...
                            if char not in string.digits + '-': # verify that it's a digit or the minus symbol
                                print('Invalid register or number in command')
                                error_count += 1
                if format == 'OP' and cmd not in ('=', '<', '>'): # If the format is an operand, checks that cmd is either '=', '<', or '>'
                    print('Invalid operator in command')
                    error_count += 1
                if format == 'L' and type(cmd) != str: # If the format is a label, checks that the cmd is a string
                    print('Invalid operator in command')
                    error_count += 1
                if format == 'F' and cmd not in ('DROP','VOID'): # If the format is a file, checks that cmd is 'DROP' or 'VOID'
                    print('Invalid operator in command')
                    error_count += 1
        except Exception as error:
            print('Error:', error, type(error))
        
        if error_count: # Terminate program if entries were invalid
            print(f'Errors found in self.check_input\nError Count: {error_count}\nsys.exit(1)')
            sys.exit(1)
        
        return True
                    
    def inspect(self, operand):
        """Checks the registers to see if arguments match the dict keys, otherwise pass the args along"""
        if operand in self.registers:
            return self.registers[operand]
        else:
            return int(operand)

    def print_reg(self):
        """Prints the contents of the EXA registers in a readable format"""
        print(f"X:{self.registers['X']}\tT:{self.registers['T']}\tF:{self.registers['F']}\n")
        return
    
    def read_instructions(self, target_instructions):
        """Prompts the EXA to read instructions given as a string"""
        
        """
        with open(target_instructions, 'r') as self.instruction_pointer:
            line = self.instruction_pointer.readline()
            while line: # A for loop did not work here. Kept recieving an error saying cant use seek because next() on another line
                #if line == '\n':
                #    continue
                self.execute(line)
                print(line, end= '')
                self.print_reg()
                line = self.instruction_pointer.readline()
            self.instruction_pointer.close
        """
        self.instruction_pointer = 0 # Resets the instruction pointer to zero in case multiple read_instructions are called
        instruction_list = self.line_split(target_instructions) # Removes '\n' char from an extended string and returns a list of strings
        end_of_instructions = 0 # A flag to indicate the end of instructions
        
        while not end_of_instructions:
        #for line in instruction_list[self.instruction_pointer:]: # ***How can I refactor this iterable on every iteration***
            try:
                self.execute(instruction_list[self.instruction_pointer])
            except IndexError: # Using this exception indicate that the file end has been reached
                print('EOI')
                end_of_instructions += 1
            
            self.instruction_pointer += 1
        return

    def file_load(self, directory: dict):
        """Copies a file directory within the main_function() in the form of a dict"""
        self.file_directory = directory
        return

    def F_access_check(self, cmd_list):
        """Checks to see if the 'F' register was accessed"""
        if 'F' in cmd_list: # If 'F' was accessed
            if self.file_cursor['POINTER'] < self.file_cursor['LEN']: # And if pointer is not at the end of file
                self.file_cursor['POINTER'] += 1 # Increment the file pointer
            if self.file_directory[self.file_cursor['NAME']]: # If 'F' is not empty
                try:
                    self.registers['F'] = self.file_directory[self.file_cursor['NAME']][self.file_cursor['POINTER']] # Try and read the updated file pointer and store in 'F'
                except IndexError:
                    print('Index Error within "F_access_check"')
            if 'F' == cmd_list[-1]: # If 'F' was at the end of the cmd_list (i.e. was written to) or is the only entry
                self.file_directory[self.file_cursor['NAME']].append(self.registers['F']) # Append contents of F to end of file
            return True
        else:   
            return False
            
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
    
    @staticmethod
    def line_split(usr_in: str):
        """Takes an entire file string and returns a list of strings split at the newline char"""
        string_list = usr_in.split('\n')
        return string_list

    def ADDI(self, cmd_list: list):
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

    def SUBI(self, cmd_list: list):
        """Subtract the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        self.registers[cmd_list[-1]] = operand_list[0] - operand_list[1] # update register value
        return self.registers[cmd_list[-1]]

    def MULI(self, cmd_list: list):
        """Multiply the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        self.registers[cmd_list[-1]] = operand_list[0] * operand_list[1] # update register value
        return self.registers[cmd_list[-1]]

    def DIVI(self, cmd_list: list):
        """Integer Divide the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        try:
            self.registers[cmd_list[-1]] = operand_list[0] // operand_list[1] # update register value
        except ZeroDivisionError:
            print('Cannot Divide by Zero')
        return self.registers[cmd_list[-1]]

    def MODI(self, cmd_list: list):
        """Mod the register values and store result in register. Called from interpret()"""
        operand_list = [self.inspect(cmd_list[0]), self.inspect(cmd_list[1])]
        try:
            self.registers[cmd_list[-1]] = operand_list[0] % operand_list[1] # update register value
        except ZeroDivisionError:
            print('Cannot Divide by Zero')
        return self.registers[cmd_list[-1]]

    def COPY(self, cmd_list: list):
        """Copy the given value into the specified register"""
        self.registers[cmd_list[-1]] = self.inspect(cmd_list[0])
        return self.registers[cmd_list[-1]]

    def TEST(self, cmd_list: list):
        """Compare the value of the first operand to the value of the second operand. If the 
        operand is 'EOF', set the T register to 1 if the pointer is as the end of file"""
        if cmd_list[0] == 'EOF':
            self.registers['T'] = int(self.file_cursor['LEN'] == self.file_cursor['POINTER'])
            return self.registers['T']
        if cmd_list[1] == '=':
            self.registers['T'] = int(self.inspect(cmd_list[0]) == self.inspect(cmd_list[2]))
        if cmd_list[1] == '<':
            self.registers['T'] = int(self.inspect(cmd_list[0]) < self.inspect(cmd_list[2]))
        if cmd_list[1] == '>':
            self.registers['T'] = int(self.inspect(cmd_list[0]) > self.inspect(cmd_list[2]))
        return self.registers['T']
    
    def MARK(self, cmd_list: list):
        """Mark this line with the specified label. Mark is a psuedo-instruction and is not executed"""
        self.marks.update( {cmd_list[0]: self.instruction_pointer} )
        return

    def JUMP(self, cmd_list: list):
        """Jump to the specified label"""
        # self.instruction_pointer.seek(self.marks[cmd_list[0]])
        if self.marks.get(cmd_list[0]):
            self.instruction_pointer = self.marks[cmd_list[0]]
        return

    def TJMP(self, cmd_list: list):
        """Jump to the specified label if the T register equals 1 (or any value other than 0)"""
        if self.marks.get(cmd_list[0]):
            if self.registers['T']:
                self.instruction_pointer = self.marks[cmd_list[0]]
        return

    def FJMP(self, cmd_list: list):
        """Jump to the specified label if the T register equals 0"""
        if self.marks.get(cmd_list[0]):
            if not self.registers['T']:
                self.instruction_pointer = self.marks[cmd_list[0]]
        return

    def GRAB(self, cmd_list: list): # 'R/N'
        """Grab a file with the specified ID"""
        self.file_cursor['NAME'] = cmd_list[0] # Update file_cursor 'NAME' and 'POINTER' values
        self.file_cursor['POINTER'] = 0 # %
        self.file_cursor['LEN'] = len(self.file_directory[self.file_cursor['NAME']])
        if self.file_directory[self.file_cursor['NAME']]:
            self.registers['F'] = self.file_directory.get(self.file_cursor['NAME'])[self.file_cursor['POINTER']] # Write the first line of the file into the 'F' register
        return

    def FILE(self, cmd_list: list): # 'R'
        """Copy the ID of the file into the specified register"""
        self.registers[self.inspect(cmd_list[0])] = self.file_cursor['NAME'] # Stores the file_cursor{} NAME value into the specified register
        return 
        
    def SEEK(self, cmd_list: list): # 'R/N'
        """Move the file cursor forward (positive) or backwards (negative) by the specified number of values. 
        If SEEK would move the file cursor past the beginning or end of the file it will instead be clamped. 
        Thus, you can use values of -9999 or 9999 to reliably move to the beginning or end of a file."""
        if 0 < ( self.file_cursor['POINTER'] + self.inspect(cmd_list[0]) ) < self.file_cursor['LEN']: # If the pointer is placed within bounds
            self.file_cursor['POINTER'] += self.inspect(cmd_list[0]) # Add the specified value to the pointer
        elif self.inspect(cmd_list[0]) < 0: # Else, if negative move to begining of file
            self.file_cursor['POINTER'] = 0
        elif self.inspect(cmd_list[0]) > 0: # Else, if positive move to end of file
            self.file_cursor['POINTER'] = self.file_cursor['LEN'] - 1
        return
        
    def VOID(self, cmd_list: list):
        """Remove the value highlighted by the file cursor from the currently held file"""
        del self.file_directory[self.file_cursor['NAME']][self.file_cursor['POINTER']] # Deletes line from file
        return 
        
    def DROP(self, cmd_list: list):
        """Drop the currently held file"""
        self.file_cursor['NAME'] = ''
        self.file_cursor['POINTER'] = 0
        self.file_cursor['LEN'] = 0
        return