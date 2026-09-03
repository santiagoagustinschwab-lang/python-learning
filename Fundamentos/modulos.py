import module

module.sumValue(1, 2, 3)
module.printValue("hopla")

from module import sumValue, printValue

sumValue(1, 2, 3)
printValue("hopla")

import math

from math import pi as PI_VALUE

print(PI_VALUE)