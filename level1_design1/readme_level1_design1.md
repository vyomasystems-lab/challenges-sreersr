There are 4 bugs in the mux.v, level1_design1 

bug1-> sel of inp12 is wrong
To Prove: run make file to capture the bug @ line 45 --> dut.sel.value= dut.sel.value= 0b01100
bug2 -> inp30 is not assigned 
To Prove: run make file to capture the bug @ line 45 --> dut.sel.value= dut.sel.value= 0b11110
bug3 -> inp31 is not assigned 
To Prove: run make file to capture the bug @ line 45 --> dut.sel.value= dut.sel.value= 0b11111
bug 4 -> default condition is not requied in a mux, 

The debugged mux design is stored in file name: mux_debug.v
test_mux_debug.py --> contains the test case for bug free mux.

run makefile_mux_debug for the bug free design
