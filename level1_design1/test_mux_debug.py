# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_mux_debug(dut):
   in1 = 0
   in2 = 0
   sel = 0

   dut.inp0.value = in1
   dut.inp1.value = in2
   dut.inp2.value = in1
   dut.inp3.value = in2
   dut.inp4.value = in1
   dut.inp5.value = in2
   dut.inp6.value = in1
   dut.inp7.value = in2
   dut.inp8.value = in1
   dut.inp9.value = in2
   dut.inp10.value = in1
   dut.inp11.value = in2
   dut.inp12.value = in1
   dut.inp13.value = in2
   dut.inp14.value = in1
   dut.inp15.value = in2
   dut.inp16.value = in1
   dut.inp17.value = in2
   dut.inp18.value = in1
   dut.inp19.value = in2
   dut.inp20.value = in1
   dut.inp21.value = in2
   dut.inp22.value = in1
   dut.inp23.value = in2
   dut.inp24.value = in1
   dut.inp25.value = in2
   dut.inp26.value = in1
   dut.inp27.value = in2
   dut.inp28.value = in1
   dut.inp29.value = in2
   dut.inp30.value = in1
   dut.inp31.value = in2
   dut.sel.value= 0b11110
     
   await Timer(2, units='ns')
    
    #assert dut.o1.value == sel1, "Result is incorrect: i1 != sel1, expected value={EXP}".format(
            #A=int(dut.i1.value), B=int(dut.i2.value), sel1=int(dut.o1.value), EXP=A)
   
   #assert dut.out.value == ((sel) & inp12) , f"output result is incorrect: Data_out != sel,"
   assert dut.out.value == (((~sel) & in1) | (sel & in2)), f"output result is incorrect: out != dut.sel.value"
    #cocotb.log.info('##### CTB: Develop your test here ########')
    #dut._log.info(f'DUT={int(dut.o1.value):sel1}')
    #assert dut.o1.value == sel1, "Test failed with: o1 != sel1".format(o1 =dut.sel1.value)
