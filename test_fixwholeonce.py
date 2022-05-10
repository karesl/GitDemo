import pytest
@pytest.mark.usefixtures("setup")

class TestExample:
    def test_fixdemo(self):
        print("I ll execute step 1")

    def test_fixdemo1(self):
        print("I ll execute step 2")

