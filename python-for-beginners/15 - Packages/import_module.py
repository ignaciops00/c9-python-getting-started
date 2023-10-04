# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning',True)

# import specific items into current namespace
from helpers import display
display('Not a warning')