from pyModbusTCP.utils import set_bit
from pyModbusTCP.utils import reset_bit
from pyModbusTCP.utils import test_bit

def setBitValue(value, c, register, bit):
    regs_2 = c.read_holding_registers(register, 1)
    if bool(regs_2):
        for write_reg in regs_2:
            if (value == True):
                write_reg = set_bit(write_reg, bit)
            elif (value == False):
                write_reg = reset_bit(write_reg, bit)
            c.write_single_register(register, write_reg)
        
def getBitValue(c, register, bit):
    package = getPackage(c, register, 1)
    if test_bit(package, bit):
        return True
    else:
        return False
    
def getPackage(c, startRegister, amount):
    regs_l = c.read_holding_registers(startRegister, amount)
    if amount == 1:
        for package in regs_l:
            return package
    elif amount > 1:
        return regs_l    