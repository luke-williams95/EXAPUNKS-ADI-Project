class EXA:

    # Singleton

    # example: ADDI 30 X T
    def __init__(self):
        # Use dunder init to create stuff you only want to create once, i.e func_mapper
        # rewrite as a dictionary, for every operation you can check to see if the operand is in the dictionary
        self.registers = {'X':0, 'T':0, 'F':0}
    # register or number, register or number, register
    
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
        operand_list = []
        for cmd in cmd_list:
            operand_list.append(self.inspect(cmd))
        
        self.registers[operand_list[2]] = operand_list[0] + operand_list[1]
         
        return operand_list[0] + operand_list[1]


    def interpret(self, usr_in:str):
        
        cmd_tuple = EXA.parse(usr_in)
        # func_mapper = {'ADDI': self.ADDI, 'SUBI': self.SUBI ....
        
        if cmd_tuple[0] == 'ADDI':
            self.ADDI(cmd_tuple[1]) 
        else:
            print('Command not recognised')

        """
        if cmd_tuple[0] == 'SUBI':
            EXA.SUBI(cmd_tuple[1]) 
        
        if cmd_tuple[0] == 'MULI':
            EXA.MULI(cmd_tuple[1])

        if cmd_tuple[0] == 'DIVI':
            EXA.DIVI(cmd_tuple[1])

        if cmd_tuple[0] == 'COPI':
            EXA.COPI(cmd_tuple[1])
        """

    """Non 'EXA' Functions"""
    #look up later. staticmethods, class methods
    @staticmethod
    def parse(usr_in: str):
            """Parses user input into the 'cmd_tuple' with the following format ('operation', ['op', 'op', 'op'])"""
            # "   ADDI   30  X T" ===> ("ADDI", [30, "X", "T"])
            string_list = usr_in.strip().split(' ', 1) # Split the first string from usr_in using " " as your delimiter
            # print(string_list)
            op_type = string_list[0] # op_type now contains the type of operation being performed
            #print(op_type)
            operand_list = string_list[-1].strip().split() # Split the remainder of string_list into a list of words
            #print(operand_list)
            return (op_type, operand_list)

if __name__ == '__main__': # For local testing
    exa = EXA()
    op_tuple = EXA.parse("   ADDI  30  X     T")
    print(op_tuple)
    #string = "ADDI 5 5 T"
    #print(exa.interpret(string))
    #exa.registers['X'] = 2
    #exa.registers['T'] = 3
