import my_module as module # we can add a alias to the module
from my_module import add # also we can get the function directly
import math # importing the default modules
from my_module import * # importing all the functions from the module. but this is not a good practice
if__name__="__main__"


print(module.add(10, 20))
print(add(10, 20))
print(math.pi)
print(math.factorial(10))
