import sys
sys.path.append('src')
import demoproject

all_modules = demoproject.ALL_MODULES

def test_sampleclient():
    print(sys.path)
    assert all_modules['sampleclient'].SampleClient.sampleclient_func() == 'sampleclient'
