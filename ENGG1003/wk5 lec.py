# IMPORTING THINGIES

import numpy as np
import sys


#mymodule.py
def greet(name):
    return f"Hello, {name}. You're a freaking loser."

#main.py
import mymodule
print(mymodule.greet("Loser"))

# Importing your own files connects functions from self created libraries

# Import an entire module
import numpy
a = numpy.sin(3)    # Use module_name.func_name()

from numpy import sin, cos, tan # etc...
b = sin(3)      # Can directly use function name

# Import with an alias
import numpy as np
c = np.sin(3)

#WILDCARDS
from math import #*
from numpy import *                        # #imports all fuhnctions
# Both math and numpy have a sin function
d = sin(3) # Which module does this come from??

# When importing all functions the function does not have tn be referred to by module name




#IMPORTING FROM BUILT IN MODULES