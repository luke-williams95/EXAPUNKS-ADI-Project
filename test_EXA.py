import cmd
from EXA import EXA

def test_parse_output():
    # Tests for basic functionality
    string = "ADDI 30 X T"
    assert EXA.parse(string)

def test_inspect():
    # Tests for basic functionality
    exa = EXA()
    exa.registers['X'] = 2
    exa.registers['T'] = 3
    assert exa.inspect('T') == 3
    assert exa.inspect('5') == 5

def test_ADDI():
    # Tests for basic functionality
    exa = EXA()
    cmd_list = ['5', '5', 'T']
    assert exa.ADDI(cmd_list) == 10
    assert exa.registers['T'] == 10


