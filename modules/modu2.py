# import modu1

# inst1= modu1.Calc()
# inst1 = inst1.A
# inst2 = modu1.func1()
# inst3 = modu1.C

# print(inst1,inst2,inst3)

# from modu1 import Calc,func1,C

# inst1= Calc()
# inst1 = inst1.A
# inst2 = func1()
# inst3 = C

# print(inst1,inst2,inst3)

# from submodules import modu1

# inst1= modu1.Calc()
# inst1 = inst1.A
# inst2 = modu1.func1()
# inst3 = modu1.C

# print(inst1,inst2,inst3)

# from submodules.modu1 import Calc,func1,C

# inst1= Calc()
# inst1 = inst1.A
# inst2 = func1()
# inst3 = C

# print(inst1,inst2,inst3)

# import sys
# sys.path.append('c:\myweb')

# import modu1

# inst1= modu1.Calc()
# inst1 = inst1.A
# inst2 = modu1.func1()
# inst3 = modu1.C

# print(inst1,inst2,inst3)

import sys
sys.path.append('c:\myweb')
from modu1 import Calc,func1,C

inst1= Calc()
inst1 = inst1.A
inst2 = func1()
inst3 = C

print(inst1,inst2,inst3)