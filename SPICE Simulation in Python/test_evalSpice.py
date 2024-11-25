import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
import ast
from evalSpice import evalSpice

# Path to the test data folder - end with / 
testdata = r"C:/Users/shand/Apalam/a2-spice/testdata/"

# Things to be tested
# - Invalid filename: correct message with FileNotFoundError
# - Invalid circuit elements: TypeError with message "Unknown element type"

def test_invalid_file():
    with pytest.raises(FileNotFoundError) as exc_info:
        evalSpice("")
    assert str(exc_info.value) == 'Please give the name of a valid SPICE file as input'

def test_invalid_element():
    with pytest.raises(ValueError) as exc_info:
        evalSpice(testdata + "test_invalid_element.ckt")
    assert str(exc_info.value) == 'Only V, I, R elements are permitted'

def test_malformed():
    with pytest.raises(ValueError) as exc_info:
        evalSpice(testdata + "test_malformed.ckt")
    assert str(exc_info.value) == 'Malformed circuit file'

def test_voltage_loop():
    with pytest.raises(ValueError) as exc_info:
        evalSpice(testdata + "test_v_loop.ckt")
    assert str(exc_info.value) == 'Circuit error: no solution'

def test_current_node():
    with pytest.raises(ValueError) as exc_info:
        evalSpice(testdata + "test_i_node.ckt")
    assert str(exc_info.value) == 'Circuit error: no solution'

testparams = [
    ("test_1.ckt", "test_1.exp"),
    ("test_2.ckt", "test_2.exp"),
    ("test_3.ckt", "test_3.exp"),
    ("test_4.ckt", "test_4.exp"),
    ("parallel.ckt","parallel.exp"),
    ("mul_dc.ckt","mul_dc.exp"),
    ("supernode.ckt","supernode.exp")   
   ]
print("meow")

def checkdiff(Vout, Iout, expFile):
    """expected outputs are in `expFile`.  Read and compare."""
    with open(testdata + expFile) as f:
        data = f.read()
    (Vexp, Iexp) = ast.literal_eval(data)
    s = 0
    for i in Vexp.keys():
        print(f"Vexp[{i}] = {Vexp[i]}")
        s += abs(Vexp[i] - Vout[i])
    for i in Iexp.keys():
        print(f"Iexp[{i}] = {Iexp[i]}")
        s += abs(Iexp[i] - Iout[i])
    return s

@pytest.mark.parametrize("inFile, expFile", testparams)
def test_spice(inFile, expFile):
    """Test with various input combinations."""
    (Vout, Iout) = evalSpice(testdata + inFile)
    assert checkdiff(Vout, Iout, expFile) <= 0.001
    
    
if __name__ == "__main__":
    pytest.main()


filename=r"C:\Users\shand\Apalam\a2-spice\testdata\sexil.ckt"
evalSpice(filename)