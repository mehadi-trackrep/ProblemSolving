import sys
from demoproject.nested_package1.utils import hudai
from demoproject.scripts.samplescript import SampleScript

print(sys.path)
SampleScript.samplescript_func()
hudai()

