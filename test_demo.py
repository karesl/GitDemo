import pytest as pytest

@pytest.mark.smoke
def test_firstprogram():
    print("Hello")
@pytest.mark.skip
def test_SecondCreditCard():
    a=0
    b=8
    sum = a+b
    assert sum==1
@pytest.mark.xfail
def test_thirddemo():
    print("Sample to skip this step")