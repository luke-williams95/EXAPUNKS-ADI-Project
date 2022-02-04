class EXA:
    # example: ADDI 30 X T
    def __init__(self):
        # rewrite as a dictionary, for every operation you can check to see if the operand is in the dictionary
        self.registers = {'X':0, 'T':0, 'F':0}
        # dict/map of all the known commands. 
        # Keys are the commands (str), the value pairs are a list that indicate each valid entry for an arugment
        self.functions = {
                    'COPY': (self.COPY, ['r/n', 'r'])
                    'ADDI': (self.ADDI, ['r/n', 'r/n', 'r'])
                    'SUBI': (self.SUBI, ['r/n', 'r/n', 'r'])
                    'MULI': (self.MULI, ['r/n', 'r/n', 'r'])
                    'DIVI': (self.DIVI, ['r/n', 'r/n', 'r'])
                    'TEST': (self.TEST, ['r/n', 'op', 'r/n'])
                    'MARK': (self.MARK, [])
                    'JUMP': (self.JUMP, [])
                    'TJMP': (self.TJMP, [])
                    'FJMP': (self.FJMP, [])
                }
                    
        
    # __main__ calls this first with the given input: 'ADDI 10 X T'
    def interpret(self, usr_in):
        cmd_tuple = EXA.parse(usr_in) # EXA.parsed 'ADDI arg0 arg1 arg2' --> ('ADDI', [arg0, arg1, arg2])
        if not self.check_input(cmd_tuple) # checks for valid argument entries
            print('Invalid input!')
            return self.function[
        self.functions[cmd_tuple[0]][0](cmd_tuple[1]) # this calls the appropriate command method and gives the arguments.
        
    @staticmethod
    def parse(usr_in): # Add a function call to a valid arg to check args in this.
            """Digests the user input to a useful format."""
            # "   ADDI   30  X T" ===> ("ADDI", ["30", "X", "T"])
            string_list = usr_in.strip().split(' ', 1) # Split the first string from usr_in using " " as your delimiter
            # print(string_list)
            op_type = string_list[0] # op_type now contains the type of operation being performed
            #print(op_type)
            operand_list = string_list[-1].strip().split() # Split the remainder of string_list into a list of words
            print(operand_list)
            return (op_type, operand_list)
    
    def check_input(self, cmd_tuple):
        """Accepts the cmd_tuple and outputs a list of tuples, 
        each tuple showing a valid argument entry and the given argument."""
        return True # pass this for now
        
        valid_args = self.functions(cmd_tuple[0])[1] # valid_args = ['r/n', 'r/n', 'r']
        given_args = cmd_tuple[1] # given_args = ['30', 'X', 'T']
        
        if len(valid_args) != len(given_args): # check first that there are the correct number of arguments.
            print('There are too many or too few arguments!')
            return False
        
        args_list = [(valid, given) for valid, given in zip(valid_args, given_args)] # make tuples of arg by arg comparison valid vs. given
        
        self.valid_input(args_list) # args_list = [('r/n', '30'),..., ('r', 'T')]
    
    def isregister(arg):
        """Returns True if argument is a valid register."""
        pass
        
    def valid_input(args_list):
        """checks each entry for valid argument."""
        for tup in args_list: # tup = ('r/n', 'X'), ('op', '='), etc.
        
            if tup[0] == 'r':
                if tup[1] not in self.registers
                    print('This is supposed to be a register')
                    return False
                    
            elif tup[0] == 'op':
                if tup[1] not in '<=>':
                    print('This has to be a comparison operator')
                    return False
                    
            else: # this is a 'r/n'
                if (type(tup[1]) != int) and (tup[1] not in self.registers)
                    print('This is neither a number or register... you did something wrong!')
                    return False
                    
            
        
    def inspect(self, operand):
        """Checks the registers to see if arguments match the dict keys, otherwise pass the args along"""
        if operand in self.registers:
            return self.registers[operand]
        else:
            return int(operand)
    
    def ADDI(self, cmd_list):
        """Add the register values or numbers and store result in register. Called from interpret()"""
        # At this point we expect cmd_list to be a properly formatted list object
        # inspects the command list and puts the proper values in the operand_list
        # Should crash if len(cmd_list) != 3
        # ['X', 50, 'X']
        # X = 20
        operand_list = [inspect(cmd_list[0]), inspect(cmd_list[1])]
        self.registers[cmd_list[2]] = operand_list[0] + operand_list[1] # update register value
        print(self.registers[cmd_list[2]]) # check that register value was updated
        return operand_list[0] + operand_list[1]

        
        

if __name__ == '__main__': # For local testing
    exa = EXA()
    string = 'ADDI 5 5 X'
    exa.interpret(string)
    print(exa.registers['X'])

    #exa = EXA()
    #exa.registers['X'] = 2
    #exa.registers['T'] = 3