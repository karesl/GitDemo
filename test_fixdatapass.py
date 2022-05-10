import pytest
@pytest.mark.usefixtures()
def test_TestExam(dataLoad):
    print(dataLoad)

@pytest.mark.usefixtures()
def test_TestExam1(crossBrowser):
    print(crossBrowser[1])





