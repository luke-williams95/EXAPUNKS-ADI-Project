class EXA:
    # example: ADDI 30 X T
    def __init__(self):
        # rewrite as a dictionary, for every operation you can check to see if the operand is in the dictionary
        self.registers = {
          'X': 0
          'T': 0
          'F': 0
        }
    # register or number, register or number, register
    def inspect(self, ):
        """Checks the registers to see if arguments match the dict keys, otherwise pass the args along"""
        if register in self.registers
            print('valid inputs')
            return 
        
    def parse(self, ):
        """Checks for valid input."""
        if 
    
    def ADDI(self, reg_num1, reg_num2, register):
        """Multiply the register values or numbers and store result in register."""
        self.parse()
        if reg_num1 in self.registers:
            op1 = self.registers[reg_num1]
        else:
            op1 = reg_num1
        if reg_num2 in self.registers:
            op2 = self.registers[reg_num2]
        else:
            op2 = reg_num2
        
        self.registers[register] = op1 + op2
        return op1 + op2
        
        
    def SUBI(self, reg_num1, reg_num2, register):
        

    def MULI(self, reg_num1, reg_num2, register):
        """Multiply the register values or numbers and store result in register."""
        if reg_num1 in self.registers:
            op1 = self.registers[reg_num1]
        else:
            op1 = reg_num1
        if reg_num2 in self.registers:
            op2 = self.registers[reg_num2]
        else:
            op2 = reg_num2
        
        self.registers[register] = op1 * op2
        return op1 * op2

    def DIVI(self, reg_num1, reg_num2, register):

    def COPY(self, reg_num, register):
        """Store register value or number into a register."""
        # def checkinput
        if reg_num in self.registers:
            return register = self.registers[reg_num]
        return self.registers[register] = reg_num