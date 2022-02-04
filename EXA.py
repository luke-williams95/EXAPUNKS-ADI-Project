class EXA:
    # example: ADDI 30 X T
    def __init__(self):
        # rewrite as a dictionary, for every operation you can check to see if the operand is in the dictionary
        self.registers = {'X':0, 'T':0, 'F':0}
        # dict/map of all the known commands. 
        # Keys are the commands (str), the value pairs are a list that indicate each valid entry for an arugment
        self.functions = {
                    'ADDI': ['r/n', 'r/n', 'r']
                    'COPY': ['r/n', 'r']
                    ....
                }
                    
        
    def interpret(self, usr_in:str):
        # EXAobj = EXA(input('put your command here:'))
        # EXAobj --> 'ADDI X X 5' which has self.registers, self.functions
        cmd_tuple = EXA.parse(usr_in)
        # self.parsed --> ('ADDI', [arg0, arg1, arg2])
        
        self.valid_input(self.arg_compare(cmd_tuple))
        #
        # 'ADDI' --> valid_args_for_ADDI = reg_num, reg_num, reg_only
    
    def parse(usr_in: str): # This works within the EXA class as long as there is no 'self' argument. Ask Dave about where to put this
            """Checks for valid input."""
            # "   ADDI   30  X T" ===> ("ADDI", ["30", "X", "T"])
            string_list = usr_in.strip().split(' ', 1) # Split the first string from usr_in using " " as your delimiter
            # print(string_list)
            op_type = string_list[0] # op_type now contains the type of operation being performed
            #print(op_type)
            operand_list = string_list[-1].strip().split() # Split the remainder of string_list into a list of words
            print(operand_list)
            return (op_type, operand_list)
    
    def arg_compare(self, cmd_tuple):
        """Accepts the cmd_tuple and outputs a list of tuples, 
        each tuple showing a valid argument entry and the given argument."""
        valid_args = self.functions(cmd_tuple[0])
        given_args = cmd_tuple[1]
        # valid_args = ['r/n', 'r/n', 'r']
        # given_args = ['30', 'X', 'T']
        args_list = [(valid, given) for valid, given in zip(valid_args, given_args)]
        return args_list
        # args_list = [('r/n', '30'),..., ('r', 'T')]
    
    def valid_input(args_list):
        """checks each entry for valid argument."""
        for tup in args_list:
        # tup = ('r/n', 'X')
            if tup[0] == 'r/n':
                if tup[1] in self.registers:
                    
            
        
    def inspect(self, operand):
        """Checks the registers to see if arguments match the dict keys, otherwise pass the args along"""
        if operand in self.registers:
            return self.registers[operand]
        else:
            return int(operand)
    
    def ADDI(self, cmd_list):
        return self.registers[
        
        
        
        """Add the register values or numbers and store result in register. Called from interpret()"""
        # At this point we expect cmd_list to be a properly formatted list object
        # inspects the command list and puts the proper values in the operand_list
        # Should crash if len(cmd_list) != 3
        operand_list = [[cmd] for cmd in cmd_list
                                  self.inspect(cmd)]
        
        self.registers[operand_list[2]] = operand_list[0] + operand_list[1]
         
        return operand_list[0] + operand_list[1]

        
        

if __name__ == '__main__': # For local testing
    op_tuple = EXA.parse("   ADDI  30  X     T")
    #print(op_tuple)

    #exa = EXA()
    #exa.registers['X'] = 2
    #exa.registers['T'] = 3