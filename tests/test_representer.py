
import test_appliance
from test_constructor import *

from yaml import *

class TestRepresenterTypes(test_appliance.TestAppliance):

    def _testTypes(self, test_name, data_filename, code_filename):
        data1 = eval(file(code_filename, 'rb').read())
        data2 = None
        output = None
        try:
            output = dump(data1, Dumper=MyDumper)
            data2 = load(output, Loader=MyLoader)
            self.failUnlessEqual(type(data1), type(data2))
            try:
                self.failUnlessEqual(data1, data2)
            except AssertionError:
                if isinstance(data1, dict):
                    data1 = [(repr(key), value) for key, value in data1.items()]
                    data1.sort()
                    data1 = repr(data1)
                    data2 = [(repr(key), value) for key, value in data2.items()]
                    data2.sort()
                    data2 = repr(data2)
                    if data1 != data2:
                        raise
                elif isinstance(data1, list):
                    self.failUnlessEqual(type(data1), type(data2))
                    self.failUnlessEqual(len(data1), len(data2))
                    for item1, item2 in zip(data1, data2):
                        self.failUnlessEqual(item1, item2)
                else:
                    raise
        except:
            print
            print "OUTPUT:"
            print output
            print "NATIVES1:", data1
            print "NATIVES2:", data2
            raise

TestRepresenterTypes.add_tests('testTypes', '.data', '.code')

