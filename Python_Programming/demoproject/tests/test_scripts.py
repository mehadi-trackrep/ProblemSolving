import sys
sys.path.append('src')
import demoproject

all_modules = demoproject.ALL_MODULES

def test_sampleclient():
    assert all_modules['samplescript'].SampleScript.samplescript_func() == 'samplescript'
