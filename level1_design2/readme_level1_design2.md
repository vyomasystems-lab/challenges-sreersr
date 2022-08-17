
Title: Capture the Bug in Sequence detector of 1011 sequence
Submitted by: Sree Ranjani Rajendran
Abstract: For the given sequence detector circuit, the test cases are written with the provided COCOTB environment by using Vyoma’s UpTickPro framework. Furthermore, the bugs are identified and debugged with the help of the UpTickPro framework.
Verification strategy: CoCotb test bench is written for the given sequence detector, with this a functional verification is done for the specific input sequence and the bug is observed once the test case is FAILED in the test environment of the UpTickPro framework. The functional verification of a sequence detector for sequence 1011 is given in Table 1. The testbench is written in CoCotb concerning table 1.  

Bugs found:
As per the design constraints, while designing the sequential detector for the 1011 sequence, the below state table is obtained for the sequence detector of sequence 1011. 

Table 1: State Table for sequence detector to detect 1011 sequence. 
S.NoCurrent State	    Next state		      Output	
	Input=0	Input=1	    Input=0	Input=1
1	IDLE	IDLE	    SEQ_1	    0	        0
2	SEQ_1	SEQ_10	    IDLE	    0	        0
3	SEQ_10	IDLE	    SEQ_101	    0	        0
4	SEQ_101	SEQ_10	    SEQ_1011    0	        1
5	SEQ_1011SEQ_10	    IDLE	    0	        0

BUG1:So it is clear that the next_state values of input=0 0f S.No:4 should be SEQ_10 (So that the search begins for the next sequence) but in the design it is IDLE

BUG2: Similarly on S.No:5, the next state value is declared as IDLE, however as per the table for the error-free design the next_state value for input=0 is SEQ_10 and for input=1, it is SEQ_1.

Debug information:

The above bugs are debugged in the file name: seq_detect_1011_debug.v. the design can be tested using the same test case in test_seq_detect_1011.py by changing the design file name in the Makefile. 

The below changes are done in the debugged design:

 SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = SEQ_10;
      end
      SEQ_1011:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1;
        else
          next_state = SEQ_10;
      end


