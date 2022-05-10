import pytest
@pytest.mark.usefixtures()
def test_fix(setup):
    print("a")
def test_fix1(setup):
    print("b")
