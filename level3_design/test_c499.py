# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_c499(dut):
   #in1 = 1
   #in2 = 0
  
   N1=dut.N1 
   N5=dut.N5 
   N9=dut.N9 
   N13=dut.N13 
   N17=dut.N17 
   N21=dut.N21 
   N25=dut.N25 
   N29=dut.N29 
   N33=dut.N33 
   N37=dut.N37 
   N41=dut.N41 
   N45=dut.N45 
   N49=dut.N49 
   N53=dut.N53 
   N57=dut.N57 
   N61=dut.N61 
   N65=dut.N65 
   N69=dut.N69 
   N73=dut.N73 
   N77=dut.N77 
   N81=dut.N81 
   N85=dut.N85 
   N89=dut.N89 
   N93=dut.N93 
   N97=dut.N97 
   N101=dut.N101 
   N105=dut.N105 
   N109=dut.N109 
   N113=dut.N113 
   N117=dut.N117 
   N121=dut.N121 
   N125=dut.N125 
   N129=dut.N129 
   N130=dut.N130 
   N131=dut.N131 
   N132=dut.N132 
   N133=dut.N133 
   N134=dut.N134 
   N135=dut.N135 
   N136=dut.N136 
   N137=dut.N137
   S0 = ( (N1 != N17 != N33 != N49 ) != (N65 != N69 != N73 != N77) != (N81 != N85 != N89 != N93) != (N137 & N129))
   S1 = ( (N5 != N21 != N37 != N53) != (N97 != N101 != N105 != N109) != (N113 != N117 != N121 != N125) != (N137 & N130))
   S2 = ((N9 != N25 != N41 != N57) != (N65 != N69 != N73 != N77) != (N97 != N101 != N105 != N109) != (N137 & N131))
   S3 = ((N13 != N29 != N45 != N61) != (N81 != N85 != N89 != N93) != (N113 != N117 != N121 != N125) != (N137 & N132))
   S4 = ((N65 != N81 != N97 != N113) != (N1 != N5 != N9 != N13) != (N17 != N21 != N25 != N29) != (N137 & N133))
   S5 = ((N69 != N85 != N101 != N117) != (N33 != N37 != N41 != N45) != (N49 != N53 != N57 != N61) != (N137 & N134))
   S6 = ((N73 != N89 != N105 != N121) != (N1 != N5 != N9 != N13) != (N33 != N37 != N41 != N45) != (N137 != N135))
   S7 = ((N77 != N93 != N109 != N125) != (N17 != N21 != N25 != N29) != (N49 != N53 != N57 != N61) != (N137 != N136))
   
   #N1-N125-> ID00-ID31
   dut.N1.value = 1
   dut.N5.value = 0
   dut.N9.value = 0
   dut.N13.value = 0
   dut.N17.value = 0
   dut.N21.value = 0
   dut.N25.value = 0
   dut.N29.value = 0
   dut.N33.value = 0
   dut.N37.value = 0
   dut.N41.value = 0
   dut.N45.value = 0
   dut.N49.value = 0
   dut.N53.value = 0
   dut.N57.value = 0
   dut.N61.value = 0
   dut.N65.value = 0
   dut.N69.value = 0
   dut.N73.value = 0
   dut.N77.value = 0
   dut.N81.value = 0
   dut.N85.value = 0
   dut.N89.value = 0
   dut.N93.value = 0
   dut.N97.value = 0
   dut.N101.value = 0
   dut.N105.value = 0
   dut.N109.value = 0
   dut.N113.value = 0
   dut.N117.value = 0
   dut.N121.value = 0
   dut.N125.value = 0
   #N129-N136 -> IC0-IC7
   dut.N129.value = 0
   dut.N130.value = 1
   dut.N131.value = 0
   dut.N132.value = 0
   dut.N133.value = 0
   dut.N134.value = 0
   dut.N135.value = 0
   dut.N136.value = 0
   #N137->R
   dut.N137.value = 1

   
   await Timer(2, units='ns')
   
   assert dut.N724.value == ( (S0 & ~S1 & ~S2 & ~S3 & S4 & ~S5 & S6 & ~S7) != N1),f"output result is incorrect: dut.N724.value != N724"
   assert dut.N725.value == ( (~S0 & S1 & ~S2 & ~S3 & S4 & ~S5 & S6 & ~S7) != N5),f"output result is incorrect: dut.N725.value != N725"
   assert dut.N726.value == ( (~S0 & ~S1 & S2 & ~S3 & S4 & ~S5 & S6 & ~S7) != N9),f"output result is incorrect: dut.N726.value != N726"
   assert dut.N727.value == ( (~S0 & ~S1 & ~S2 & ~S3 & S4 & ~S5 & S6 & ~S7) != N13),f"output result is incorrect: dut.N727.value != N727"
   assert dut.N728.value == ( (S0 & ~S1 & ~S2 & ~S3 & S4 & ~S5 & ~S6 & S7) != N17),f"output result is incorrect: dut.N728.value != N728"
   assert dut.N729.value == ( (~S0 & S1 & ~S2 & ~S3 & S4 & ~S5 & ~S6 & S7) != N21),f"output result is incorrect: dut.N729.value != N729"
   assert dut.N730.value == ( (~S0 & ~S1 & S2 & ~S3 & S4 & ~S5 & ~S6 & ~S7) != N25),f"output result is incorrect: dut.N730.value != N730"
   assert dut.N731.value == ( (~S0 & ~S1 & ~S2 & S3 & S4 & ~S5 & ~S6 & S7) != N29),f"output result is incorrect: dut.N731.value != N731"
   assert dut.N732.value == ( (S0 & ~S1 & ~S2 & ~S3 & ~S4 & S5 & S6 & ~S7) != N33),f"output result is incorrect: dut.N732.value != N732"
   assert dut.N733.value == ( (~S0 & ~S1 & ~S2 & ~S3 & ~S4 & S5 & S6 & ~S7) != N37),f"output result is incorrect: dut.N733.value != N733"
   assert dut.N734.value == ( (~S0 & ~S1 & S2 & ~S3 & ~S4 & S5 & S6 & ~S7) != N41),f"output result is incorrect: dut.N734.value != N734"
   assert dut.N735.value == ( (~S0 & ~S1 & ~S2 & S3 & ~S4 & S5 & S6 & ~S7) != N45),f"output result is incorrect: dut.N735.value != N735"
   assert dut.N736.value == ( (S0 & ~S1 & ~S2 & ~S3 & ~S4 & S5 & ~S6 & S7) != N49),f"output result is incorrect: dut.N736.value != N736"
   assert dut.N737.value == ( (~S0 & S1 & ~S2 & ~S3 & ~S4 & S5 & ~S6 & S7) != N53),f"output result is incorrect: dut.N737.value != N737"
   assert dut.N738.value == ( (~S0 & ~S1 & S2 & ~S3 & ~S4 & S5 & ~S6 & S7) != N57),f"output result is incorrect: dut.N738.value != N738"
   assert dut.N739.value == ( (~S0 & ~S1 & ~S2 & S3 & ~S4 & S5 & ~S6 & S7) != N61),f"output result is incorrect: dut.N739.value != N739"
   assert dut.N740.value == ( (S4 & ~S5 & ~S6 & ~S7 & S0 & ~S1 & S2 & ~S3) != N65),f"output result is incorrect: dut.N740.value != N740"
   assert dut.N741.value == ( (~S4 & S5 & ~S6 & ~S7 & S0 & ~S1 & S2 & ~S3) != N69),f"output result is incorrect: dut.N741.value != N741"
   assert dut.N742.value == ( (~S4 & ~S5 & S6 & ~S7 & S0 & ~S1 & S2 & ~S3) != N73),f"output result is incorrect: dut.N742.value != N742"
   assert dut.N743.value == ( (~S4 & ~S5 & ~S6 & ~S7 & S0 & ~S1 & S2 & ~S3) != N77),f"output result is incorrect: dut.N743.value != N743"
   assert dut.N744.value == ( (S4 & ~S5 & ~S6 & ~S7 & S0 & ~S1 & ~S2 & S3) != N81),f"output result is incorrect: dut.N744.value != N744"
   assert dut.N745.value == ( (~S4 & S5 & ~S6 & ~S7 & S0 & ~S1 & ~S2 & S3) != N85),f"output result is incorrect: dut.N745.value != N745"
   assert dut.N746.value == ( (~S4 & ~S5 & S6 & ~S7 & S0 & ~S1 & ~S2 & ~S3) != N89),f"output result is incorrect: dut.N746.value != N746"
   assert dut.N747.value == ( (~S4 & ~S5 & ~S6 & S7 & S0 & ~S1 & ~S2 & S3) != N93),f"output result is incorrect: dut.N747.value != N747"
   assert dut.N748.value == ( (S4 & ~S5 & ~S6 & ~S7 & ~S0 & S1 & S2 & ~S3) != N97),f"output result is incorrect: dut.N748.value != N748"
   assert dut.N749.value == ( (~S4 & S5 & ~S6 & ~S7 & ~S0 & S1 & S2 & ~S3) != N101),f"output result is incorrect: dut.N749.value != N749"
   assert dut.N750.value == ( (~S4 & ~S5 & S6 & ~S7 & ~S0 & S1 & S2 & ~S3) != N105),f"output result is incorrect: dut.N750.value != N750"
   assert dut.N751.value == ( (~S4 & ~S5 & ~S6 & S7 & ~S0 & S1 & S2 & ~S3) != N109),f"output result is incorrect: dut.N751.value != N751"
   assert dut.N752.value == ( (S4 & ~S5 & ~S6 & ~S7 & ~S0 & S1 & ~S2 & S3) != N113),f"output result is incorrect: dut.N752.value != N752"
   assert dut.N753.value == ( (~S4 & S5 & ~S6 & ~S7 & ~S0 & S1 & ~S2 & S3) != N117),f"output result is incorrect: dut.N753.value != N753"
   assert dut.N754.value == ( (~S4 & ~S5 & S6 & ~S7 & ~S0 & S1 & ~S2 & S3) != N121),f"output result is incorrect: dut.N754.value != N754"
   assert dut.N755.value == ( (~S4 & ~S5 & ~S6 & S7 & ~S0 & S1 & ~S2 & S3) != N125),f"output result is incorrect: dut.N755.value != N755"
