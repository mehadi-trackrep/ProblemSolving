from time import perf_counter
# from demoproject.nested_package1.helpers import AllHelperFunctions
# or, 
# from .helpers import AllHelperFunctions
from helpers import AllHelperFunctions

def hudai():
    stime = perf_counter()
    print(f'{AllHelperFunctions.helper_function1()}, hudai')
    etime = perf_counter()
    print(f"Taken total times - {etime - stime} seconds")